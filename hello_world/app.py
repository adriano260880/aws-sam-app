import json
def lamba_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello world')
    }
