from django.urls import path
from .transport.rest import handlers
from .transport.rest.handlers import GetData, AddData

urlpatterns = [
    path('me/<pk>', GetData.as_view()),
    path('set_phone/', AddData.as_view())
]
