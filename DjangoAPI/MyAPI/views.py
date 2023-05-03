from django.shortcuts import render
from . forms import MyForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from sklearn.preprocessing import LabelEncoder
from rest_framework.parsers import JSONParser

from .forms import MyForm
from . models import approval
from . serializers import approvalSerializers
import pickle
import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd


class ApprovalsView(viewsets.ModelViewSet):
	queryset = approval.objects.all()
	serializer_class = approvalSerializers

def ohevalues(df):
    ohe_col = joblib.load(("C:/Users/Tim/recidivism_model.pkl"))
    cat_columns = ['Gender', 'Race', 'Gang_Affiliated', 'Supervision_Level_First', 'Education_Level', 'Prison_Offense',
                   'Prison_Years', 'Employment_Exempt']
    df_processed = [col for col in cat_columns.columns if cat_columns[col].dtype == 'object' or cat_columns[col].dtype == 'bool']
    for col in df_processed:
        le = LabelEncoder()
        le.fit(cat_columns[col])
        cat_columns[col] = le.transform(cat_columns[col])
    newdf = pd.DataFrame(newdict)
    return(newdf)


@api_view(["POST"])
def approvereject(request):
    try:
        mdl = joblib.load("C:/Users/Tim/recidivism_model.pkl")
        mydata = pd.read_csv('C:/Users/Tim/small_rec_dataset.csv')
        mydata = request.data
        unit = np.array(list(mydata.values()))
        unit = unit.reshape(1, -1)
        y_pred = mdl.predict(unit)
        y_pred = (y_pred > 0.58)
        newdf = pd.DataFrame(y_pred, columns=['Status'])
        newdf = newdf.replace({1: 'High Recidivism Risk', 0: 'Low Recidivism Risk'})
        return JsonResponse('Your Status is {}'.format(newdf), safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'GET'])
def cxcontact(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            gender = form.cleaned_data['gender']
            race = form.cleaned_data['race']
            releaseage = form.cleaned_data['releaseage']
            gangaffilation = form.cleaned_data['gangaffilation']
            riskscore = form.cleaned_data['riskscore']
            edlevel = form.cleaned_data['edlevel']
            dependents = form.cleaned_data['dependents']
            prisonoffense = form.cleaned_data['prisonoffense']
            prisonyears = form.cleaned_data['prisonyears']
            priorarrestfelony = form.cleaned_data['priorarrestfelony']
            priorarrestmisd = form.cleaned_data['priorarrestmisd']
            priorarrestsvio = form.cleaned_data['priorarrestsvio']
            priorarrestsprop = form.cleaned_data['priorarrestsprop']
            priorarrestsdrug = form.cleaned_data['priorarrestsdrug']
            priorpvcharges = form.cleaned_data['priorpvcharges']
            priorconvprop = form.cleaned_data['priorconvprop']
            priorconvdrug = form.cleaned_data['priorconvdrug']
            delenqreports = form.cleaned_data['delenqreports']
            progattend = form.cleaned_data['progattend']
            progunexabs = form.cleaned_data['progunexabs']
            residchanges = form.cleaned_data['residchanges']
            avgdayperdrugtest = form.cleaned_data['avgdayperdrugtest']
            positivethc = form.cleaned_data['positivethc']
            positivecocaine = form.cleaned_data['positivecocaine']
            positivemeth = form.cleaned_data['positivemeth']
            positiveother = form.cleaned_data['positiveother']
            percentemp = form.cleaned_data['percentemp']
            jobsperyear = form.cleaned_data['jobsperyear']
            empexempt = form.cleaned_data['empexempt']
            myDict = (request.POST).dict()
            df = pd.DataFrame(myDict, index = [0])
            answer = approvereject(ohevalue(df))
            messages.success(request, 'Recidivism Risk: {}'.format(answer))

            print(firstname, lastname, releaseage, gangaffilation, dependents)

    form = approvereject()

    return renderers(request, 'myform/cxform.html', {'form':form})