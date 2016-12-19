from django.shortcuts import render
from NextGenStream.utils.constants import *

streamer_list = [
    {
        'name': 'huloog',
        'channels': {
            'cl': 'rtmp://46.101.172.142/llive/huloo-sl.sdp',
            'ch': 'ch2',
            'sl': 'sl1',
            'sh': 'sh1'
        }
    },
    {
        'name': 'name2',
        'channels': {
            'cl': 'rtmp://54.255.176.172/live/newsnation_360p',
            'ch': 'ch2',
            'sl': 'sl1',
            'sh': 'sh1'
        }
    }
]

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
    return render(req, 'NextGenStream/home.html', {'streamer_list': streamer_list})
