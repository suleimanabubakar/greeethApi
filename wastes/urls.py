from django.contrib import admin
from .views import *
from django.urls import path,include

urlpatterns = [
    path('types',WasteTypesList.as_view()),
    path('create',CreateWaste.as_view()),
    path('bid',BidWaste.as_view()),
    path('bid/react/<int:pk>',BidStatusUpdate.as_view()),
    path('sale',SaleWaste.as_view()),
    path('available',PendingWaste.as_view()),
]
