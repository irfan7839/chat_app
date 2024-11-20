from django.urls import path

from .views import MessagesApiView

urlpatterns = [
    path('messages', MessagesApiView.as_view())
]