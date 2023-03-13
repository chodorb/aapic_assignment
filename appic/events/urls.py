from django.urls import path 
from events.views import EventDetailAPIView, EventListAPIView,EventPerformancesDetailAPIView,EventExportAPIView
from performances.views import PerformanceListApiView

urlpatterns = [
    path('',EventListAPIView.as_view()),
    path('/<int:pk>/',EventDetailAPIView.as_view()),
    path('/<int:pk>/withperformances/',EventPerformancesDetailAPIView.as_view()),
    path('/<int:event_id>/performances/',PerformanceListApiView.as_view()),
    path('/export/',EventExportAPIView.as_view())
]