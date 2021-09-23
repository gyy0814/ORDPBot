import json
# import blhx
import socket
import time

import requests
import logging
import ORDP
from concurrent.futures import ThreadPoolExecutor
from ws4py.client.threadedclient import WebSocketClient

def msg_test():
    msg = "系统信息\n" \
          f"系统时间:{str(time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()))}\n" \
          f"本机名称:{socket.gethostname()}\n" \
          f"本机IP:{socket.gethostbyname(socket.gethostname())}\n" \
          "运行状态:良好\n"\
          "版本号:V7.5\n"
    return(msg)


def post(url, data):
    """自动三次重连"""
    i = 0
    while i < 3:
        try:
            req = requests.post(url=url, data=data)
            if req.status_code == 200:
                return req
            else:
                raise Exception(f"code:{req.status_code}")
        except Exception as a:
            i += 1
            logging.warning(f"通讯失败 原因{a}")
            logging.warning(f"正在重试第{i}次")
    else:
        logging.error(f"url:{url}\r\ndata:{data}\r\n通讯失败")


def message(msg):
    if msg['type'] == 'GroupMessage':
        group_message(msg['messageChain'], msg['sender'])
    elif msg['type'] == 'FriendMessage':
        friend_message(msg['messageChain'], msg['sender'])


def friend_message(msg, sender):
    if sender['id'] == 2691325401:
        pass


def group_message(msg, sender):
    if sender['group']['id'] == 813400992 or 907860435:
        send_msg = ordp(msg)
        if send_msg:
            Mirai.add_plain(send_msg)
            Mirai.send(Mirai.Group, sender['group']['id'])
        pass

        pass
    elif sender['group']['id'] == 000:
        pass


def ordp(msg):
    msg_plain = ""
    table = [['查询局长', ORDP.sql_jzcx],
             ['今日信息', ORDP.sql_gdcx],
             ['查询监管', ORDP.sql_jycx],
             ['查询部调', ORDP.sql_bdcx],
             ['系统信息', msg_test],
             ['查询端口', ORDP.sql_dkxx]]
    table2 = [['查询机车', ORDP.sql_jcxx],
              ['查询图定信息', ORDP.sql_tdxx],
              ['查询图定详情', ORDP.sql_tdxc],
              ['查询图定奖励', ORDP.sql_tdjl],
              ['月信息', ORDP.sql_yxx],
              ['查询放风司机', ORDP.sql_sjff],
              ['查询放风机车', ORDP.sql_jcff],
              ['查询运量', ORDP.sql_ylb],
              ['查询司机', ORDP.sql_sjxx]]
    table3 = [['调度指引', ORDP.DDZY_Str],
              ['配属指引', ORDP.PSZY_Str],
              ['监管指引', ORDP.JGZY_Str],
              ['积分指引', ORDP.JFZY_Str],
              ['强拍指引', ORDP.QPZY_Str],
              ['调动指引', ORDP.DDOZY_Str],
              ['图定指引', ORDP.FDZY_Str],
              ['运监指引', ORDP.LKJZY_Str],
              ['编组指引', ORDP.BZZY_Str],
              ['菜单', ORDP.CD_Str]]
    for msg in msg:
        if msg['type'] == 'Plain':
            msg_plain += msg['text']
    if msg_plain.startswith("#"):
        msg_plain = msg_plain.replace("#", '')
        for i in table:
            if i[0] in msg_plain:
                return i[1]()
        for i in table2:
            if i[0] in msg_plain:
                return i[1](msg_plain.replace(i[0], ''))
        for i in table3:
            if i[0] in msg_plain:
                return i[1]
        if msg_plain.startswith("音乐"):
            return None
        else:
            return "命令错误"
    else:
        return None


class WSClient(WebSocketClient):

    def opened(self):
        logging.info("ws已连接")

    def closed(self, code, reason=None):
        print("Closed down:", code, reason)

    def received_message(self, resp):
        resp = json.loads(str(resp))
        pool.submit(message, resp)
        # message(resp)


class BotWS:
    def __init__(self, server_host, server_port, authkey):
        self.HOST = str(server_host)  # 服务器的IP地址
        self.PORT = str(server_port)  # 服务器的端口
        self.authkey = authkey
        self.ws_connect()

    def ws_connect(self):
        url = f'http://{self.HOST}:{self.PORT}//config'
        data = '{"sessionKey":"' + self.authkey + '","enableWebsocket":' + 'true' + '}'
        requests.post(url, data=data)  # 开启Websocket
        ws = WSClient(f'ws://{self.HOST}:{self.PORT}/message?sessionKey={self.authkey}')
        ws.connect()
        ws.run_forever()


class Bot:
    def __init__(self, server_host, server_port, bot_qq, server_apikey):
        self.HOST = str(server_host)  # 服务器的IP地址
        self.PORT = str(server_port)  # 服务器的端口
        self.QQ = str(bot_qq)  # 服务器上登陆的QQ号
        self.ApiKey = str(server_apikey)  # 服务器的apikey
        self.messageChain = []
        self.authkey = self.auth()
        self.Group = "GroupMessage"
        self.Friend = "FriendMessage"

    def auth(self):
        logging.info("获取Mirai Authkey...")
        url = f'http://{self.HOST}:{self.PORT}//auth'
        data = {"authKey": self.ApiKey}
        req = post(url=url, data=json.dumps(data))  # Mirai服务器获取authkey
        authkey = json.loads(req.text)["session"]
        logging.info("校验Mirai Authkey...")
        url = f'http://{self.HOST}:{self.PORT}//verify'
        data = {"sessionKey": authkey, "qq": self.QQ}
        req = post(url=url, data=json.dumps(data))  # Mirai服务器校验authkey
        if json.loads(req.text)["code"] == 0:
            logging.info("校验成功")
            return authkey
        else:
            logging.error("authkey获取失败")
            return

    def add_image(self, url):
        self.messageChain.append({"type": "Image", "url": str(url)})

    def add_image_file(self, file, to):
        img_body = {"sessionKey": self.authkey, "type": str(to)}
        files = {'img': ('send.png', open(file, 'rb'), 'image/png', {})}
        req = requests.request("POST", 'http://' + self.HOST + ':' + self.PORT + '/uploadImage',
                               data=img_body, files=files)
        if req.status_code == 200:
            url = json.loads(req.text)['url']
            self.messageChain.append({"type": "Image", "url": str(url)})

    def add_plain(self, text):
        self.messageChain.append({"type": "Plain", "text": str(text)})

    def add_at(self, target):
        self.messageChain.append({"type": "At", "target": int(target)})

    def add_face(self, target):
        self.messageChain.append({"type": "Face", "faceId": int(target)})

    def send(self, msg_to, to_id):
        url = f'http://{self.HOST}:{self.PORT}/send{msg_to}'
        data = {"sessionKey": self.authkey, "target": int(to_id), "messageChain": self.messageChain}
        data = json.dumps(data)
        post(url, data=data.encode('utf-8'))
        self.messageChain = []


bot_QQ = "3185789685"  # 机器人的QQ号
bot_APIKey = "8866666688"  # 设定的APIKey

# bot_host = "192.168.3.73"  # 使用内网地址
# bot_host = "127.0.0.1"  # 使用本机地址
bot_host = "mengxin.pro"  # 使用外网地址

bot_port = "8880"  # 本地端口
LOG_FORMAT = "%(asctime)s [%(levelname)s][line %(lineno)s] - %(message)s "
DATE_FORMAT = "%Y/%m/%d %H:%M:%S"

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)
pool = ThreadPoolExecutor(max_workers=50)
Mirai = Bot(bot_host, bot_port, bot_QQ, bot_APIKey)
BotWS(bot_host, bot_port, Mirai.authkey)
