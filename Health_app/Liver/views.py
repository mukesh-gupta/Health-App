from django.shortcuts import render
import numpy as np
import joblib
from .forms import LiverForm

# Create your views here.
def Liver(request):
    forms=LiverForm()
    return render(request,'Liver/liver.html',{'forms':forms})

def result(request):
    if request.method=='POST':
        tb=request.POST['Total_Bilirubin']
        db = request.POST['Direct_Bilirubin']
        ap=request.POST['Alkaline_Phosphotase']
        aa = request.POST['Alamine_Aminotransferase']
        tp= request.POST['Total_Protiens']
        a= request.POST['Albumin']
        agr = request.POST['Albumin_and_Globulin_Ratio']
        l=[tb,db,ap,aa,tp,a,agr]
        # to_predict = np.array([0.15200, 1265.0, 20.60, 140.10, 0.35140]).reshape(1, size)
        to_predict = np.array([l])
        loaded_model = joblib.load('Liver_Model.pkl')
        result = loaded_model.predict(to_predict)
        a = result[0]

        if(int(result)==1):
            prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
        else:
            prediction = "No need to fear. You have no dangerous symptoms of the disease"
    return render(request,'Diabetes/result.html',{'prediction_text':a,'prediction':prediction})
