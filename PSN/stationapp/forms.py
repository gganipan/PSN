from django import forms
from . models import History, Station, Repair

class StationForm(forms.ModelForm):

    class Meta:
        model = Station
        fields = ('code', 'location', 'sensor_model', 'installation_date', 'transceiver_model', 'sensor_sn', 'digitizer_sn', 'lnb_sn', 'sspb_sn', 'transceiver_sn', 'battery_start_date')

        widgets = {
            'code':forms.TextInput(attrs={'class': 'textinputclass'}),
            'location': forms.TextInput(attrs={'class': 'textinputclass'}),
            'sensor_model': forms.TextInput(attrs={'class': 'textinputclass'}),
            'installation_date': forms.SelectDateWidget(),
            'transceiver_model': forms.TextInput(attrs={'class': 'textinputclass'}),
            'sensor_sn':forms.TextInput(attrs={'class': 'textinputclass'}),
            'digitizer_sn':forms.TextInput(attrs={'class': 'textinputclass'}),
            'lnb_sn':forms.TextInput(attrs={'class': 'textinputclass'}),
            'sspb_sn':forms.TextInput(attrs={'class': 'textinputclass'}),
            'transceiver_sn':forms.TextInput(attrs={'class': 'textinputclass'}),
            'battery_start_date': forms.SelectDateWidget(),
        }

class HistoryForm(forms.ModelForm):

    class Meta:
        model = History
        fields = ('personnel', 'text', 'repair_date')

        widgets = {
            'personnel': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable' 'medium-editor-textarea'}),
            'repair_date': forms.SelectDateWidget(),
        }

class RepairReportForm(forms.ModelForm):

    class Meta:
        model = Repair
        fields = ('reported_by', 'observation', 'station_type_field',
                'report_type_field', 'date_filed', 'problem_type_field',
                'repair_type_field', 'operation_field', 'repaired_by',
                'analysis', 'repair_procedure',
         )

        widgets = {
            'report_type_field': forms.RadioSelect(),
            'station_type_field': forms.RadioSelect(),
            'problem_type_field': forms.RadioSelect(),
            'observation': forms.Textarea(attrs={'class': 'editable' 'medium-editor-textarea'}),
            'reported_by': forms.TextInput(attrs={'class': 'textinputclass'}),
            'date_filed' : forms.SelectDateWidget(),
            'analysis'   : forms.Textarea(attrs={'class': 'editable' 'medium-editor-textarea'}),
            'repair_type_field': forms.RadioSelect(),
            'repair_procedure' : forms.Textarea(attrs={'class': 'editable' 'medium-editor-textarea'}),
            'repaired_by': forms.TextInput(attrs={'class': 'textinputclass'}),
            'station_type_field': forms.RadioSelect(),
        }
