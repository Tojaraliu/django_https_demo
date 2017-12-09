from django.conf.urls import url

import demo1.views as views

urlpatterns = [
    url(r'^test/', views.test_view),
]