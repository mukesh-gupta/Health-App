from django.shortcuts import render
import numpy as np
import joblib
from .forms import KidneyForm

# Create your views here.
def Kidney(request):
    forms=KidneyForm()
    return render(request,'Kidney/kidney.html',{'forms':forms})

def result(request):
    if request.method=='POST':
        bp = request.POST['Blood_Pressure']
        sg=request.POST['Specific_Gravity']
        al = request.POST['Albumin']
        su=request.POST['Blood_Sugar_Level']
        rbc = request.POST['Red_Blood_Cells_Count']
        pc= request.POST['Pus_Cell_Count']
        pcc= request.POST['Pus_Cell_Clumps']
        l=[bp,sg,al,su,rbc,pc,pcc]
        # to_predict = np.array([0.15200, 1265.0, 20.60, 140.10, 0.35140]).reshape(1, size)
        to_predict = np.array([l])
        loaded_model = joblib.load('Kidney_Model.pkl')
        result = loaded_model.predict(to_predict)
        a = result[0]

        if (int(result) == 1):
            prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
        else:
            prediction = "No need to fear. You have no dangerous symptoms of the disease"

    return render(request,'Diabetes/result.html',{'prediction_text':a,'prediction':prediction})


