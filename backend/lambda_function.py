# import json
import boto3
from botocore.exceptions import ClientError
from prompts import SYSTEM_PROMPT

def lambda_handler(event, context):

    Bucket = "nova-bedrock"

    client = boto3.client("bedrock-runtime", region_name = "us-west-2")
    system=[
        {
            'text': SYSTEM_PROMPT
        }
    ]

    uri = event['uri']
    ext = uri.split('.')[-1]
    if ext not in ['png', 'jpeg', 'gif', 'webp']:
        return {
            'statusCode': 400, 
            'body': f'ERROR: Invalid image format {ext}.'
        }

    # Set the model ID, e.g., Amazon Nova Lite.
    model_id = "us.amazon.nova-lite-v1:0"
    # Start a conversation with the user message.
    user_message = "Describe this image"
    conversation = [
        {
            "role": "user",
            "content": [{
                # "text": user_message,
                'image': {
                    'format': ext, # 'png'|'jpeg'|'gif'|'webp'
                    'source': {
                        # 'bytes': b'bytes',
                        's3Location': {
                            'uri': uri,
                            'bucketOwner': "589622200547"
                        }
                    }
                },
            }]
        }
    ]

    try:
        # Send the message to the model, using a basic inference configuration.
        response = client.converse(
            modelId = model_id,
            messages = conversation,
            system = system,
            inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9}
        )

        # Extract and print the response text.
        response_text = response["output"]["message"]["content"][0]["text"]
        
    except (ClientError, Exception) as e:
        response_text = f"ERROR: Can't invoke '{model_id}'. Reason: {e}"
    
    return {
        'statusCode': 200,
        "response": response_text
    }