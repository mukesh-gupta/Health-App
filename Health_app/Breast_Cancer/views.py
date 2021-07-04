from django.shortcuts import render
import numpy as np
import joblib
from .forms import BreastCancerForm

# Create your views here.

def home(request):
    return render(request,'index.html')

def Cancer(request):
    forms = BreastCancerForm(request.POST)
    return render(request,'Breast_Cancer/cancer.html',{'forms':forms})

def result(request):
    if request.method=='POST':
        cpm=request.POST['Mean_of_the_Concave_Points']
        am = request.POST['Mean_of_the_Area']
        rdm=request.POST['Mean_of_the_Radius']
        pm = request.POST['Mean_of_the_Perimeters']
        cm = request.POST['Mean_of_the_Concavity']
        l=[cpm,am,rdm,pm,cm]
        # to_predict = np.array([0.15200, 1265.0, 20.60, 140.10, 0.35140]).reshape(1, size)
        to_predict = np.array([l])
        loaded_model = joblib.load('Cancer_Model.pkl')
        result = loaded_model.predict(to_predict)
        a = result[0]

        if (int(a) == 1):
            prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
        else:
            prediction = "No need to fear. You have no dangerous symptoms of the disease"
    return render(request,'Breast_Cancer/result.html',{'prediction_text':a,'prediction':prediction})
