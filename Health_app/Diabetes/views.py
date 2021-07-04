from django.shortcuts import render
import numpy as np
import joblib
from .forms import DiabeticForm

def Diabetes(request):
    forms=DiabeticForm()
    return render(request,'Diabetes/diabetes.html',{'forms':forms})

def result(request):
    if request.method=='POST':
        g = request.POST['Glucose_Level']
        bp=request.POST['Current_Blood_Pressure']
        bmi = request.POST['Enter_the_Body_Mass_Index']
        a= request.POST['Age']
        l=[g,bp,bmi,a]
        to_predict = np.array([l])
        loaded_model = joblib.load('Diabetes_Model.pkl')
        result = loaded_model.predict(to_predict)
        a = result[0]

        if(int(result)==1):
            prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
        else:
            prediction = "No need to fear. You have no dangerous symptoms of the disease"
    return render(request,'Diabetes/result.html',{'prediction_text':a,'prediction':prediction})
