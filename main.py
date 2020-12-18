from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage,TextSendMessage
import os

app = Flask(__name__)
#環境変数の取得
YOUR_CHANNELL_ACCESS_TOKEN="4dbf9d8b-0e12-4ae7-9ef4-9baffd53fb03"
YOUR_CHANNELL_SEACRET="caeba1884c9abd18661fafd22f88bd33"
line_bot_api=LineBotApi(YOUR_CHANNELL_ACCESS_TOKEN)
handler=WebhookHandler(YOUR_CHANNELL_SEACRET)

@app.route("/caooback",method=["POST"])
def callback():
    signature=request.headers["X-Line-Signature"]

    body=request.get_data(as_texy=True)
    app.logger.info("Request body" + body)

    try:
        handler.handle(body,signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"

@handle.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__=="__main__":
    port=int(os.getenv("PORT",5000))
    app.run(host="0.0.0.0",port=port)