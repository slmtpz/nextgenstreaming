from django.conf.urls import url
from NextGenStream.controllers import stream

urlpatterns = [
    url(r'^get_stream', stream.get_stream),
]
