from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URITemplateAction,
    PostbackTemplateAction, DatetimePickerTemplateAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('LGop1Mv+IDEI1AH8PiC0KL4EPB4NQvLF6mCtcLGJ1rMOKCj7QyRGz9EgQoFqlvnmBJPABhj7/9HoEq/GRrP2ipVTOnlGmOSQaiUQ361nQOaHxVOuHu3WOLSjFCPSMHbnAFYloM2wb99KwbN4zClNcgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('6656e2a268d134c41c47d0ed5bd5597d')

# 監聽所有來自 /callback 的 Post Request
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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # message = TextSendMessage(text=event.message.text)
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     message)
    k = event.message.text
    if k ='test':
        message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://example.com/image.jpg',
                title='Who is Yi-Han Chen?',
                text='Student from NTUST, Taiwan . Familiar with Python and Java',
                actions=[
                    PostbackTemplateAction(
                        label='postback',
                        text="you just sned ",
                        data='action=buy&itemid=1'
                    ),
                    MessageTemplateAction(
                        label='What is my side project recently?',
                        text='side project'
                    ),
                    URITemplateAction(
                        label='My Linkedin',
                        uri='https://www.linkedin.com/in/hannah-chen-326918101/'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
