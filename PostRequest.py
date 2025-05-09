from flask import Flask, request, abort
from linebot.exceptions import (
    InvalidSignatureError
)
def post_handler(handler,app):
    # 監聽所有來自 /callback 的 Post Request
    @app.route("/")
    def awake():
        return "Alive"
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