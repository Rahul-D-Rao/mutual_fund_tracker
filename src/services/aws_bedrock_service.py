import boto3
import json
import os
import botocore

def interact_with_bedrock(input_text):
    """
    Interact with AWS Bedrock for generative AI tasks.
    Args:
        input_text (str): Input text to send to AWS Bedrock.
    Returns:
        str: Response from AWS Bedrock.
    """
    try:
        # Load AWS credentials from JSON file
        credentials_path = os.path.join("../config", "aws_credentials.json")
        with open(credentials_path, "r") as f:
            credentials = json.load(f)
        
        # Create a Bedrock Runtime client
        client = boto3.client(
            'bedrock-runtime',
            region_name="us-east-2",  # Ensure this is the correct region
            aws_access_key_id=credentials["aws_access_key_id"],
            aws_secret_access_key=credentials["aws_secret_access_key"]
        )
        
        # Use the full ARN for the model (example ARN, replace with actual ARN)
        model_arn = "arn:aws:bedrock:us-east-2:183631345329:inference-profile/us.amazon.nova-lite-v1:0" # Please replace with your model_arn I am using amazon nova lite 
        
        # Prepare the payload with 'user' role and content as an array of JSON objects
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"text": input_text}
                    ]
                }
            ]
        }
        
        # Convert the payload to JSON
        payload_json = json.dumps(payload)
        
        # Invoke the Bedrock model
        response = client.invoke_model(
            modelId=model_arn,  # Using the model ARN instead of just the model ID
            body=payload_json,
            contentType="application/json",
            accept="application/json",
        )
        
        # Parse the response
        response_body = response["body"].read().decode("utf-8")
        #print("Raw Response Body:", response_body)  # Debugging statement
        
        result = json.loads(response_body)
        
        # Correctly parse the outputText from the response
        if 'output' in result and 'message' in result['output'] and 'content' in result['output']['message']:
            for item in result['output']['message']['content']:
                if 'text' in item:
                    return item['text']
        
        return "No response received from the model."
    
    except botocore.exceptions.ClientError as e:
        raise RuntimeError(f"Client error interacting with AWS Bedrock: {e}")
    except Exception as e:
        raise RuntimeError(f"Failed to interact with AWS Bedrock: {e}")
