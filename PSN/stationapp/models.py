from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Station(models.Model):
    code = models.CharField(max_length=4,null='False',default='XXXX')
    location = models.CharField(max_length=200,null='False', default='Phivolcs bldg, C.P. Garcia St., Diliman, Q.C')
    installation_date = models.DateField(blank=True, default=timezone.now)
    sensor_model = models.CharField(max_length=50,null='False',default='Trillium120')
    transceiver_model = models.CharField(max_length=50,null='False',default='Cygnus205')
    battery_start_date = models.DateField(blank=True, default=timezone.now)

    sensor_sn = models.CharField(max_length=50,null='False',default='0000')
    digitizer_sn = models.CharField(max_length=50,null='False',default='0000')
    lnb_sn = models.CharField(max_length=50,null='False',default='0000')
    sspb_sn = models.CharField(max_length=50,null='False',default='0000')
    transceiver_sn = models.CharField(max_length=50,null='False',default='0000')

    def post(self):
        self.save()

    def get_absolute_url(self):
        return reverse("station_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.code



class History(models.Model):
    station = models.ForeignKey('stationapp.Station', related_name='histories',on_delete=models.CASCADE)
    personnel = models.CharField(max_length=7, default='GFG')
    text = models.CharField(max_length=500, default='enter text here')
    repair_date = models.DateField(blank=True, default=timezone.now)
    save_history = models.BooleanField(default=False)
    #
    def log(self):
        self.save_history = True
        self.save()

    def get_absolute_url(self):
        return reverse("station_stss_list")

    def __str__(self):
        return self.text


class Repair(models.Model):
    station = models.ForeignKey('stationapp.Station', related_name='repair_requests',on_delete=models.CASCADE)
    reported_by = models.CharField(max_length=20, default='G.Ganipan')
    date_filed = models.DateField(blank=True, default=timezone.now)

    REPORT_TYPE = [
        ('RQ', 'Request'),
        ('IN', 'Information')
    ]
    report_type_field = models.CharField(max_length=2, choices = REPORT_TYPE, default= 'IN')
    PROBLEM_TYPE = [
        ('WV', 'No Waveform Display'),
        ('DT', 'No Data Record'),
        ('NN', 'No Network Connection'),
        ('PS', 'Power Supply/Source'),
        ('SR', 'Sensor'),
        ('VZ', 'Vandalism'),
        ('SD', 'Structural Damage'),
    ]
    problem_type_field = models.CharField(max_length=2, choices = PROBLEM_TYPE, default= 'WV')
    STATION_TYPE = [
        ('ST', 'STSS'),
        ('SC', 'SCSS'),
        ('TA', 'Tsunami "TEWS" Alerting'),
        ('TD', 'Tsunami "TEWS" Detection'),
        ('TW', 'Tsunami "JICA" TWD'),
        ('DT', 'Tsunami "JICA" DTS'),
        ('IS', 'Intensity Meter SATREPS'),
        ('IJ', 'Intensity Meter JICA2'),
        ('SM', 'Strong Motion'),
        ('MO', 'Main Office')
    ]
    station_type_field = models.CharField(max_length=2, choices = STATION_TYPE, default= 'MO')
    REPAIR_TYPE = [
        ('ST', 'DRC'),
        ('ST', 'Remote Access'),
        ('ST', 'On Site Visit'),
        ('ST', 'Phone Call/SMS'),

    ]
    repair_type_field = models.CharField(max_length=2, choices = REPAIR_TYPE, default= 'MO')
    OPERATION = [
        ('OP', 'Operational'),
        ('NO', 'Not Operational')
    ]
    operation_field = models.CharField(max_length=2, choices = OPERATION, default= 'MO')
    observation = models.TextField()
    repaired_by = models.CharField(max_length=20, default='G.Ganipan')
    analysis = models.TextField(default='')
    repair_procedure = models.TextField(default='')


    def __str__(self):
        return self.observation
