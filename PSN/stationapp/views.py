from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Station, History, Repair
from .forms import HistoryForm, RepairReportForm, StationForm
from django.db.models import Q

from django.views.generic import (TemplateView,ListView,DetailView,CreateView)
from django.urls import reverse_lazy

# Create your views here.
class StaffCtrlStnListView(ListView):
    template_name = 'stationapp/station_scss_list.html'
    model = Station

    def get_queryset(self):
        return Station.objects.filter(Q(code__endswith='B')|Q(code__endswith='S')).order_by('code')

class StationListView(ListView):
    template_name = 'stationapp/station_list.html'
    model = Station

    def get_queryset(self):
        byte = Station.objects.count()
        return Station.objects.order_by('code')

class CreateStationView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'stationapp/station_detail.html'

    form_class = StationForm

    model = Station

class SatTelStnListView(ListView):
    model = Station
    template_name = 'stationapp/station_stss_list.html'
    def get_queryset(self):
        return Station.objects.filter(~Q(Q(code__endswith='S')|Q(code__endswith='B'))).order_by('code')

class StationProfileDetailView(DetailView):
    model = Station

class RepairReportDetailView(DetailView):
    model = Repair

class StndView(TemplateView):
    template_name = 'stationapp/stnd.html'


@login_required
def add_history_to_station(request, pk):
    station = get_object_or_404(Station, pk=pk)
    if request.method == "POST":
        form = HistoryForm(request.POST)
        if form.is_valid():
            history = form.save(commit=False)
            history.station = station
            history.save()
            history.log()
            return redirect('station_detail', pk=station.pk)
    else:
        form = HistoryForm()
    return render(request, 'stationapp/history_form.html', {'form': form})

def add_repair_report(request, pk):
    station =get_object_or_404(Station, pk=pk)
    if request.method == "POST":
        form = RepairReportForm(request.POST)
        if form.is_valid():
            repair = form.save(commit=False)
            repair.station = station
            repair.save()
            return redirect('station_detail', pk=station.pk)
    else:
        form = RepairReportForm()
    return render(request, 'stationapp/repair_report_form.html', {'form': form})
