import os
import sys
import yaml
import pandas as pd
import markdown
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Ensure we are in the `src` directory
current_dir = os.path.dirname(__file__)
os.chdir(current_dir)

# Add specific subdirectories to sys.path
sys.path.append(os.path.abspath(os.path.join(current_dir, 'data_processing')))

# Import modules
from load_data import load_mutual_fund_data
from transform_data_and_filter import clean_data, filter_by_date
from group_by_fund import group_data_by_fund_and_month
from export_results import export_to_csv

sys.path.append(os.path.abspath(os.path.join(current_dir, 'services')))
from aws_s3_service import upload_to_s3
from aws_bedrock_service import interact_with_bedrock

def markdown_to_pdf(markdown_text, pdf_file):
    """
    Convert Markdown text to a PDF file using reportlab.
    Args:
        markdown_text (str): Markdown formatted text.
        pdf_file (str): Path to save the PDF file.
    """
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_text)

    # Split HTML content into paragraphs
    paragraphs = html_content.split('\n')
    for paragraph in paragraphs:
        if paragraph.strip():  # Avoid adding empty lines
            elements.append(Paragraph(paragraph, styles['Normal']))
            elements.append(Spacer(1, 12))  # Add some space between paragraphs

    doc.build(elements)

def main():
    # Load configuration
    with open("../config/config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)
    input_file = config['file_paths']['input_data']
    output_file = config['file_paths']['output_results']
    s3_bucket = config['aws']['s3_bucket']
    bedrock_model_id = config['aws']['bedrock_model_id']
    
    # Step 1: Load data
    print("Loading data...")
    df = pd.read_csv(input_file)
    
    # Step 2: Clean and preprocess data
    print("Cleaning data...")
    df = df.drop(columns=["#"], errors="ignore")  # Remove redundant column
    df = df.dropna(subset=["return_5yr"])  # Remove rows with missing 5-year returns
    
    # Step 3: Filter by category and risk type (example: Equity and Very High Risk)
    category_filter = "Equity"
    risk_type_filter = "Very High Risk"
    df = df[(df["category"] == category_filter) & (df["risk_type"] == risk_type_filter)]
    
    # Step 4: Group by mutual fund and aggregate performance metrics
    print("Aggregating data by mutual fund and month...")
    df_grouped = df.groupby(["AMC_name", "Mutual Fund Name"]).agg(
        return_1yr_avg=("return_1yr", "mean"),
        return_3yr_avg=("return_3yr", "mean"),
        return_5yr_avg=("return_5yr", "mean")
    ).reset_index()
    
    # Step 5: Export results locally
    print("Exporting results...")
    export_to_csv(df_grouped, output_file)
    
    # Step 6: Upload results to S3
    print(f"Uploading {output_file} to S3 bucket {s3_bucket}...")
    upload_to_s3(output_file, s3_bucket, os.path.basename(output_file))
    
    # Read the CSV file content as a string
    with open(output_file, 'r') as f:
        csv_content = f.read()
    
    # Combine the input text with the CSV content
    input_text = f"Summarize the performance of mutual funds in India.\nCSV Content:\n{csv_content}"
    
    # Step 7: Interact with AWS Bedrock
    print("Interacting with AWS Bedrock...")
    bedrock_response = interact_with_bedrock(input_text)
    print("Bedrock Response:")
    #print(bedrock_response)
    
    # Save the response to a Markdown file
    markdown_file = "../datasets/output_summary.md"
    with open(markdown_file, 'w', encoding='utf-8') as md_file:
        md_file.write(bedrock_response)
    
    # Convert the Markdown to PDF using reportlab
    pdf_file = "../datasets/output_summary.pdf"
    markdown_to_pdf(bedrock_response, pdf_file)
    
    print(f"Markdown file saved to {markdown_file}")
    print(f"PDF file saved to {pdf_file}")

if __name__ == "__main__":
    main()