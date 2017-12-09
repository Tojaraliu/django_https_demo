from django.conf.urls import url, include

import helloworld.views

urlpatterns = [
    url(r'^helloworld/', helloworld.views.helloworld),
]
