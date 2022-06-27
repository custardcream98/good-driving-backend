from django.urls import path
from .views import UploadGPX

urlpatterns = [

    path('upload', UploadGPX.as_view()),

]
