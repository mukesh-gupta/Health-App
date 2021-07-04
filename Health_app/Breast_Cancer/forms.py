from django import forms

class BreastCancerForm(forms.Form):
    Mean_of_the_Concave_Points=forms.FloatField(required=True)
    Mean_of_the_Area=forms.FloatField()
    Mean_of_the_Radius=forms.FloatField()
    Mean_of_the_Perimeters=forms.FloatField()
    Mean_of_the_Concavity=forms.FloatField()
