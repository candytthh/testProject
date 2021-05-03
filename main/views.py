from django.shortcuts import render, get_object_or_404
# from django.template import loader
from .models import Location, Datapoint
from random import random
from time import sleep
import time
# Create your views here.


# from dwebsocket.decorators import accept_websocket
#
#
# @accept_websocket
# def path(request):
#     if request.is_websocket():
#         print(1)
#         request.websocket.send('succeed'.encode('utf-8'))


def index(request):
    location_list = Location.objects.all
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    return render(request, 'main/base.html', locals())


def detail(request, location_id):
    location_list = Location.objects.all
    required_location = get_object_or_404(Location, id=location_id)
    required_location_name = required_location.location_name
    show_information_list = required_location.datapoint_set.all()
    show_information = show_information_list[0]
    # 格式化成2016-03-20 11:45:39形式
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # temperature_show = required_location.
    return render(request, 'main/location.html', locals())
    # return render(request, 'main/base.html', locals())


def push_data(self):
    pass


def detail1(request, location_id):
    location_list = Location.objects.all
    required_location = get_object_or_404(Location, id=location_id)
    required_location_name = required_location.location_name
    # 拿到datapoint表中的所有实例，因为前面指定了location，所以其实只有一个，但是返回是个列表，所以该列表只有一个数据。
    show_information_list = required_location.datapoint_set.all()
    # 显示出这个列表中的第一个数据，也就是唯一的数据
    show_information = show_information_list[0]
    # 格式化成2016-03-20 11:45:39形式
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # current_time 也需要用websocket 来实时显示啊

    while True:
        value = round(22 + random() * 3, 1)
        # timestamp_as_dt = datetime.utcnow().astimezone(timezone.utc)
        show_information.temperature = value
        show_information.save(update_fields=["temperature"])


        sleep(5)

    # temperature_show = required_location.
    return render(request, 'main/location.html', locals())








