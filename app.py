from flask import *
from dbModel import *
from datetime import datetime

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import psycopg2
conn = psycopg2.connect(database="d3l8u727fkdhuh",user="uskhmdlztebice",password="5714697bd569731729daa365947918c513374d064055ec40fd3644ed56963f0f",host="ec2-107-20-237-78.compute-1.amazonaws.com",port="5432")
cur = conn.cursor()

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('UGtou7UM2W+SYqoffaZx2dKmRGRc/H6vqz6PLHyR5ot/PsHpMLod/sGdlKkRt6aM1VO/UVNhlRm23Hf6+GhxS+wAW1vT5mSsCJERfo8yxelOPtPcrG/0y2I1Sjw7FVNyUNPiXMdpe5tXDkZxWf/C7wdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('55dbfadd5f83fefc85864563e62c189e')

def get_data():
    cur.execute("SELECT * FROM howhow;")
	rows = cur.fetchall()
	return rows[1]
	
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

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = get_data()
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
	
