#!/bin/bash/python3

def lambda_handler(event, context):

    body = """
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Lambda Test Page</title>
                </head>
                <body>
                    <h1>Hello Lambda!</h1>
                </body>
            </html>
            """

    return {
        "statusCode": 200,
        "body": body,
        "headers": {
        'Content-Type': 'text/html',
        }
    }
