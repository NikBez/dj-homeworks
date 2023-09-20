from django.urls import path

from measurement.views import SensorListCreateView, SensorRetrieveUpdateDestroyView, MeasurementListCreateView, \
    MeasurementRetrieveUpdateDestroyView

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view()),
    path('sensors/<pk>/', SensorRetrieveUpdateDestroyView.as_view()),

    path('measurement/', MeasurementListCreateView.as_view()),
    path('measurement/<pk>/', MeasurementRetrieveUpdateDestroyView.as_view())
]