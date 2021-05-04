import json
from channels.generic.websocket import WebsocketConsumer
from django.shortcuts import get_object_or_404
from main.models import Location, Datapoint
from time import sleep
from random import random
from datetime import datetime, timezone
from decimal import Decimal
import time


class DatapointUpdate(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    # def receive(self, text_data=None, bytes_data=None):
    #     text_data_python = json.loads(text_data)
    #     # loads函数将json对象转为python对象
    #     message = '小仓优香' + text_data_python['message']
    #
    #     self.send(text_data=json.dumps(
    #         {
    #             'message': message
    #         }
    #     )
    #
    #     )

    def receive(self, text_data=None, bytes_data=None):
        location_id_python = json.loads(text_data)
        # loads函数将json对象转为python对象,是个字典
        location_id = location_id_python['id']
        required_location = get_object_or_404(Location, id=location_id)
        datapoint_list = required_location.datapoint_set.all()
        datapoint = datapoint_list[0]

        # self.send(text_data=json.dumps(
        #         {
        #             # 'humidity': datapoint.humidity+5,
        #             # 'temperature': datapoint.temperature+5,
        #             'temperature': 'sss',
        #             'humidity': str(datapoint.humidity),
        #             # 必须要转一下格式，因为python字典不支持decimal格式，可以转成字符串
        #             # 在html页面解析时数据格式可能会出问题
        #         }
        #     )
        #
        #     )

        while True:
            value = round(22 + random() * 3, 1)
            datapoint.temperature = round(Decimal.from_float(value), 1)
            datapoint.humidity = round(Decimal.from_float(value+20), 1)
            # 格式化成2016-03-20 11:45:39形式
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            self.send(text_data=json.dumps(
                {
                    'humidity': str(datapoint.humidity),
                    'temperature': str(datapoint.temperature),
                    'time': str(current_time),
                }
            )

            )

            datapoint.save()

            sleep(5)

            # datapoint.save 可以写在send之前吗，也就是说save之后，当前的datapoint会被关闭吗，还可以继续操作码？
            # 在send函数中 text_data 参数可以换成别的吗？为什么跟接收到的函数是一样的？？
            # 必须要转一下格式，因为python字典不支持decimal格式，可以转成字符串

