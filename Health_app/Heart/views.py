from django.shortcuts import render
import numpy as np
import joblib
from .forms import HeartForm

# Create your views here.
def Heart(request):
    forms=HeartForm(request.POST)
    return render(request,'Heart/heart.html',{'forms':forms})

def result(request):
    if request.method=='POST':
        cp = request.POST['Chest_Pain_Type']
        trestbps=request.POST['Resting_Blood_Pressure_in_mm_Hg']
        chol = request.POST['Serum_Cholestoral_in_mg_dl']
        fbs=request.POST['Fasting_Blood_Sugar']
        restecg = request.POST['Resting_Electro_cardiographic_Result']
        thalach= request.POST['Maximum_Heart_Rate_Achieved']
        oldpeak= request.POST['Slope_of_the_peak']
        ca=request.POST['Coronary_artery']
        l=[cp,trestbps,chol,fbs,restecg,thalach,oldpeak,ca]
        # to_predict = np.array([0.15200, 1265.0, 20.60, 140.10, 0.35140]).reshape(1, size)
        to_predict = np.array([l])
        loaded_model = joblib.load('Heart_Model.pkl')
        result = loaded_model.predict(to_predict)
        a = result[0]

        if (int(result) == 1):
            prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
        else:
            prediction = "No need to fear. You have no dangerous symptoms of the disease"

    return render(request,'Heart/result.html',{'prediction_text':a,'prediction':prediction})

