def handler(request):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/plain"
        },
        "body": "✅ Fastwater callback active"
    }


Fix the final handler for Vercel

