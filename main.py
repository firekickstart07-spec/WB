from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "WhatsApp Bot is Live!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Received:", data)
    return "OK", 200

if __name__ == '__main__':
    app.run()
