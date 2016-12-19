from django.shortcuts import render
from NextGenStream.utils.constants import *
import json

streamer_list = []

@csrf_exempt
def init_stream(req):
    stream_dict = req.POST.dict()
    streamer_name = stream_dict(Constants.streamer_name)
    streamer_channels = stream_dict(Constants.streamer_channels)

    streamer_dict = {
        Constants.streamer_name: streamer_name,
        Constants.streamer_channels: streamer_channels
    }
    streamer_list.append(streamer_dict)


def remove_stream(req):
    stream_dict = req.POST.dict()
    streamer_name = stream_dict(Constants.streamer_name)

    for streamer in streamer_list:
        if streamer[Constants.streamer_name] == streamer_name:
            streamer_list.remove(streamer)


def get_streamers(req):
    return render(req, 'NextGenStream/home.html', json.dumps(streamer_list))
