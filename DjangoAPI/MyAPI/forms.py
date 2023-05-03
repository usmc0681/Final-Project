from django import forms
from . models import approval

class MyForm(forms.Form):
	firstname = forms.CharField(max_length=15)
	lastname = forms.CharField(max_length=15)
	gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
	race = forms.ChoiceField(choices=[('WHITE', 'White'), ('BLACK', 'Black')])
	releaseage = forms.IntegerField()
	gangaffilation = forms.ChoiceField(choices=[('TRUE', 'True'), ('FALSE', 'False')])
	riskscore = forms.IntegerField()
	firstlevel = forms.ChoiceField(choices=[('Standard', 'Standard'), ('Specialized', 'Specialized'), ('High', 'High')])
	edlevel = forms.ChoiceField(choices=[('Less than HS Diploma', 'Less than HS Diploma'),
										 ('High School Diploma', 'High School Diploma'),
										 ('At least some college', 'At least some college')])
	dependents = forms.IntegerField()
	prisonoffense = forms.ChoiceField(choices=[('Drug', 'Drug'), ('Property', 'Property'),
											   ('Violent/Non-Sex', 'Violent/Non-Sex'), ('Violent/Sex', 'Violent/Sex'),
											   ('Other', 'Other')])
	prisonyears = forms.ChoiceField(choices=[('1-2 years', '1-2 years'), ('Less than 1 year', 'Less than 1 year'),
											 ('Greater than 2 to 3 years', 'Greater than 2 to 3 years'),
											 ('More than 3 years', 'More than 3 years')])
	priorarrestfelony = forms.IntegerField()
	priorarrestmisd = forms.IntegerField()
	priorarrestsvio = forms.IntegerField()
	priorarrestsprop = forms.IntegerField()
	priorarrestsdrug = forms.IntegerField()
	priorpvcharges = forms.IntegerField()
	priorconvprop = forms.IntegerField()
	priorconvdrug = forms.IntegerField()
	delenqreports = forms.IntegerField()
	progattend = forms.IntegerField()
	progunexabs = forms.IntegerField()
	residchanges = forms.IntegerField()
	avgdayperdrugtest = forms.FloatField()
	positivethc = forms.FloatField()
	positivecocaine = forms.FloatField()
	positivemeth = forms.FloatField()
	positiveother = forms.FloatField()
	percentemp = forms.FloatField()
	jobsperyear = forms.FloatField()
	empexempt = forms.ChoiceField(choices=[('TRUE', 'True'), ('FALSE', 'False')])