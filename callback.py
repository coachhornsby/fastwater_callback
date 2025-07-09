from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    if code:
        print(f"Authorization code received: {code}")
        return Response(f"✅ Authorization code received!<br><br>{code}<br><br>You can close this window.", mimetype="text/html")
    else:
        return Response("❌ No code received.", mimetype="text/html")

# Required so Vercel knows it's a serverless function
app.run = lambda *args, **kwargs: None
