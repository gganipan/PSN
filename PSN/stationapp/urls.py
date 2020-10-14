from django.urls import path
from . import views

urlpatterns = [
    path('',views.StationListView.as_view(), name='station_list'),
    path('stnd/', views.StndView.as_view(), name='stnd'),
    path('station/new/', views.CreateStationView.as_view(), name='station_new'),
    path('staff-controlled/', views.StaffCtrlStnListView.as_view(), name='station_scss_list'),
    path('station/<int:pk>', views.StationProfileDetailView.as_view(), name='station_detail'),
    path('satellite-telemetered/', views.SatTelStnListView.as_view(), name='station_stss_list'),
    path('station/<int:pk>/history/', views.add_history_to_station, name='add_history_to_station'),
    path('station/<int:pk>/repair-request/', views.add_repair_report, name='add_repair_report'),
    path('station/<int:pk>/repair/', views.RepairReportDetailView.as_view(), name='repair_report_detail'),

]
