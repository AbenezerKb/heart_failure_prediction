from django.shortcuts import render

# Create your views here.
import numpy as np
import pandas as pd
from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response


class DeathPrediction(APIView):
    def post(self, request):
        data = request.data
        #age,anaemia,creatinine_phosphokinase,diabetes,ejection_fraction,high_blood_pressure,platelets,serum_creatinine,serum_sodium,sex,smoking,time
        age = data['age']
        anaemie = data['anaemia']
        creatinine_phosphokinase = data['creatinine_phosphokinase']
        diabetes = data['diabetes']
        ejection_fraction = data['ejection_fraction']
        high_blood_pressure = data['high_blood_pressure']
        platelets = data['platelets']
        serum_creatinine = data['serum_creatinine']
        serum_sodium = data['serum_sodium']
        smoking = data['smoking']
        sex = data['sex']
        time = data['time']
        #age = data['age']
        # if gender == 'Male':
        #     gender = 0
        # elif gender == 'Female':
        #     gender = 1
        # else:
        #     return Response("Gender field is invalid", status=400)
        lin_reg_model = ApiConfig.model
        death_predicted = lin_reg_model.predict([[age, anaemie, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking, time]])[0][0]
        death_predicted = np.round(death_predicted, 1)
        response_dict = {"Prediction Shows: ": death_predicted}
        return Response(response_dict, status=200)