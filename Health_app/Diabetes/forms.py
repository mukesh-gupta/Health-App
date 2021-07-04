from django import forms

class DiabeticForm(forms.Form):
    #Pregnancies=forms.FloatField()
    Glucose_Level=forms.FloatField()
    Current_Blood_Pressure=forms.FloatField()
    Enter_the_Body_Mass_Index=forms.FloatField()
    #Diabetes_Pedigree_Function=forms.FloatField()
    Age= forms.FloatField()
