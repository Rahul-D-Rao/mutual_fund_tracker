# Mutual Fund Tracker

This project is a **Mutual Fund Tracker** that processes mutual fund data, cleans it, filters based on specific criteria, groups it, and aggregates performance metrics. It then exports the results to a CSV file and uploads it to an AWS S3 bucket. The project also integrates with AWS Bedrock to interact with generative AI models for summarizing mutual fund performance.

---

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Windows Setup](#windows-setup)
  - [Linux Setup](#linux-setup)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Running the Script](#running-the-script)
- [AWS Configuration](#aws-configuration)
- [Troubleshooting](#troubleshooting)

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10+**
- **pip** (Python package installer)
- **AWS CLI** (for AWS configuration)
- **AWS SDK for Python (Boto3)**

---

## Installation

### Windows Setup

1. **Install Python 3.10+**
   - Download and install Python from the [official website](https://www.python.org/downloads/).
   - During installation, ensure that **Add Python to PATH** is checked.

2. **Install Python dependencies:**
   - Open **Command Prompt** (cmd) or **PowerShell**.
   - Install required libraries using `pip`:
   
   ```bash
   pip install -r requirements.txt
   ```

3. **Install AWS CLI (if not installed):**
   - Download and install AWS CLI from the [AWS CLI website](https://aws.amazon.com/cli/).
   - After installation, configure your AWS credentials using:
   
   ```bash
   aws configure
   ```

   You’ll need to input your **AWS Access Key**, **Secret Access Key**, and set the default region (e.g., `us-east-2`).

4. **Ensure AWS SDK (Boto3) is installed:**
   ```bash
   pip install boto3
   ```

5. **Run the project:**
   - Navigate to the `src` directory and execute:
   
   ```bash
   python main.py
   ```

### Linux Setup

1. **Install Python 3.10+**
   - For Ubuntu/Debian-based systems:
   
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

2. **Install Python dependencies:**
   - Navigate to the project directory and run:
   
   ```bash
   pip install -r requirements.txt
   ```

3. **Install AWS CLI (if not installed):**
   - On Ubuntu/Debian:
   
   ```bash
   sudo apt install awscli
   ```

   - After installation, configure your AWS CLI:
   
   ```bash
   aws configure
   ```

4. **Ensure AWS SDK (Boto3) is installed:**
   ```bash
   pip install boto3
   ```

5. **Run the project:**
   - Navigate to the `src` directory and execute:
   
   ```bash
   python3 main.py
   ```

---

## Configuration

1. **`config.yaml`**:
   - This file contains the paths for the input data, output data, and AWS configuration.
   
   Example configuration:
   
   ```yaml
   file_paths:
     input_data: "../datasets/mutual_fund_data.csv"
     output_results: "../datasets/output_results.csv"
   
   aws:
     s3_bucket: "mutual-fund-tracker-demo"
     bedrock_model_id: "arn:aws:bedrock:us-east-2:183631345329:inference-profile/us.amazon.nova-lite-v1:0"
   ```

2. **`aws_credentials.json`**:
   - Store your **AWS Access Key ID** and **Secret Access Key** here.
   
   Example `aws_credentials.json`:
   
   ```json
   {
       "aws_access_key_id": "YOUR_ACCESS_KEY",
       "aws_secret_access_key": "YOUR_SECRET_KEY"
   }
   ```

---

## Usage

### Running the Script

To run the **Mutual Fund Tracker** script, follow these steps:

1. **Prepare your input data** (CSV file with mutual fund information) in the path specified in `config.yaml`.
2. **Run the script**:
   - For Windows:

   ```bash
   python main.py
   ```

   - For Linux:

   ```bash
   python3 main.py
   ```

3. **Output:**
   - The processed data will be saved as `output_results.csv` in the path specified in `config.yaml`.
   - The results will be uploaded to the AWS S3 bucket specified in the configuration.
   - The script will also interact with AWS Bedrock and return a summary response based on the mutual fund data.

---

## AWS Configuration

To interact with **AWS Bedrock** and **S3**, you need to configure your AWS credentials.

1. **Set up AWS CLI:**
   - Run the following command to configure your AWS credentials:
   
   ```bash
   aws configure
   ```

2. **Ensure correct permissions:**
   - Your AWS IAM user should have the necessary permissions to:
     - Upload files to the specified S3 bucket.
     - Access and invoke models via AWS Bedrock.

---

## Troubleshooting

If you encounter any errors, here are some common solutions:

1. **Issue with AWS Credentials:**
   - Ensure that your **AWS Access Key** and **Secret Access Key** are correctly configured and have the right permissions.
   - Check the IAM policy and permissions for accessing AWS Bedrock and S3.

2. **Model Input Format Error (ValidationException):**
   - Ensure that the input provided to the AWS Bedrock API is correctly formatted as per the model requirements. The content should be a **JSON object**.

3. **File Not Found:**
   - Check if the input data file (`mutual_fund_data.csv`) exists at the specified location and the path is correct in `config.yaml`.