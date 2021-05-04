from django.shortcuts import render, get_object_or_404
from .models import Location, Datapoint
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


def socket_test(request):
    location_list = Location.objects.all
    required_location = get_object_or_404(Location, id=1)
    required_location_name = required_location.location_name
    show_information_list = required_location.datapoint_set.all()
    # 这里虽然是个列表，但是其实只有一项，就是location id匹配的那个datapoint
    show_information = show_information_list[0]
    return render(request, 'main/test.html', locals())









