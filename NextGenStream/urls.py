from django.conf.urls import url
from NextGenStream.controllers import stream

urlpatterns = [
    url(r'^init_stream', stream.init_stream),
    url(r'^remove_stream', stream.remove_stream),
    url(r'', stream.get_streamers)
]
