from django.conf.urls import url 
from . import views as blog

urlpatterns = [
    url(r'^$', blog.home, name='home'),
]
