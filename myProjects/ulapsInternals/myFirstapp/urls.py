
from django.urls import path

from . import views

urlpatterns = [
    path ('',views.home,name='home'), #or the index.html, then define in views.py
    path ('add',views.add, name='add')#ito ay local path natin need sya lagi maconnect sa main url.py
]
