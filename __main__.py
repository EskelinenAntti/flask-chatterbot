from flask import Flask
from chatterbot import ChatBot
from flask import request
from flask import abort

app = Flask(__name__)
bot = ChatBot("Pertti Bottinen")

@app.route("/messages", methods = ["POST"])
def messages():

    message = request.get_json()["text"]

    if message:
        return {"text": str(bot.get_response(message))}
    else:
        abort(400)

if __name__ == '__main__':
    app.run(debug=True)