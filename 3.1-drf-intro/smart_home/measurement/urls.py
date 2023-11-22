from django.urls import path

from measurement.views import SensorList, SensorDetail, MeasurementCreate

urlpatterns = [
    path('sensors/', SensorList.as_view()),
    path('sensors/<int:pk>/', SensorDetail.as_view()),
    path('measurements/', MeasurementCreate.as_view()),
]
