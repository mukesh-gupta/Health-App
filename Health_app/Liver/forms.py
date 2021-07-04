from django import forms

class LiverForm(forms.Form):
    Total_Bilirubin=forms.FloatField()
    Direct_Bilirubin=forms.FloatField()
    Alkaline_Phosphotase=forms.FloatField()
    Alamine_Aminotransferase=forms.FloatField()
    Total_Protiens= forms.FloatField()
    Albumin= forms.FloatField()
    Albumin_and_Globulin_Ratio=forms.FloatField()
