# 载入flask套件来架设服务器
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

#token 权杖, access 存取秘密
line_bot_api = LineBotApi('tK115PnaTqyDpVhla/ARuEXrWnQT2PXdy9KaLGSGlr7c/WnJ5vH/cgO2se2jZ3UX2Ft1Pj9WkQR7DpYhrDWgYyePUKQoojOkgguoFxLo9pzlYhHe71LBOXl2WyxZuZf1hbzOFMMtJvpFDsa7DV0bJwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f3f9fed0a25365a20e683c847c490d57')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '很抱歉，我看不懂你说什么'

    if msg in ['hi','Hi']:
        r = '嗨'
    elif msg == '你吃饭了吗':
        r = '还没'
    elif msg == '你是谁':
        r = '我是机器人'
    elif '订位' in msg:
        r = '您想订位，是吗?'

    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(
    package_id='1',
    sticker_id='1'
))


if __name__ == "__main__":
    app.run()