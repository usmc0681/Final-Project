from django.db import models

class approval(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    RACE_CHOICES = (
        ('WHITE', 'White'),
        ('BLACK', 'Black')
    )
    GANG_CHOICES = (
        ('TRUE', 'True'),
        ('FALSE', 'False')
    )
    FIRST_CHOICES = (
        ('Standard', 'Standard'),
        ('Specialized', 'Specialized'),
        ('High', 'High')
    )
    ED_CHOICES = (
        ('Less than HS Diploma', 'Less than HS Diploma'),
        ('High School Diploma', 'High School Diploma'),
        ('At least some college', 'At least some college')
    )
    PRISON_CHOICES = (
        ('Drug', 'Drug'),
        ('Property', 'Property'),
        ('Violent/Non-Sex', 'Violent/Non-Sex'),
        ('Violent/Sex', 'Violent/Sex'),
        ('Other', 'Other')
    )
    YEARS_CHOICES = (
        ('1-2 years', '1-2 years'),
        ('Less than 1 year', 'Less than 1 year'),
        ('Greater than 2 to 3 years', 'Greater than 2 to 3 years'),
        ('More than 3 years', 'More than 3 years')
    )
    EMPLOY_CHOICES = (
        ('FALSE', 'False'),
        ('TRUE', 'True')
    )

    firstname = models.CharField(max_length= 15)
    lastname = models.CharField(max_length= 15)
    gender = models.CharField(max_length= 15, choices= GENDER_CHOICES)
    race = models.CharField(max_length= 10, choices= RACE_CHOICES)
    releaseage = models.IntegerField(default=0)
    gangaffilation = models.CharField(max_length= 15, choices= GANG_CHOICES)
    riskscore = models.IntegerField(default=0)
    firstlevel = models.CharField(max_length= 15, choices= FIRST_CHOICES)
    edlevel = models.CharField(max_length=25, choices= ED_CHOICES)
    dependents = models.IntegerField(default=0)
    prisonoffense = models.CharField(max_length= 20, choices= PRISON_CHOICES)
    prisonyears = models.CharField(max_length= 25, choices= YEARS_CHOICES)
    priorarrestfelony = models.IntegerField(default=0)
    priorarrestmisd = models.IntegerField(default=0)
    priorarrestsvio = models.IntegerField(default=0)
    priorarrestsprop = models.IntegerField(default=0)
    priorarrestsdrug = models.IntegerField(default=0)
    priorpvcharges = models.IntegerField(default=0)
    priorconvprop = models.IntegerField(default=0)
    priorconvdrug = models.IntegerField(default=0)
    delenqreports = models.IntegerField(default=0)
    progattend = models.IntegerField(default=0)
    progunexabs = models.IntegerField(default=0)
    residchanges = models.IntegerField(default=0)
    avgdayperdrugtest = models.FloatField(default=0)
    positivethc = models.FloatField(default=0)
    positivecocaine = models.FloatField(default=0)
    positivemeth = models.FloatField(default=0)
    positiveother = models.FloatField(default=0)
    percentemp = models.FloatField(default=0)
    jobsperyear = models.FloatField(default=0)
    empexempt = models.CharField(max_length= 15, choices= EMPLOY_CHOICES)

    def __str__(self):
        return '{}, {}'.format(self.lastname, self.firstname)