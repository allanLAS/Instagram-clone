from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.sign_up, name= 'sign up'),
]