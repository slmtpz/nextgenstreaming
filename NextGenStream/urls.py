from django.conf.urls import url
from NextGenStream.controllers import stream

urlpatterns = [
    url(r'', stream.get_stream),
]
