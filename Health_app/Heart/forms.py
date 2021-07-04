from django import forms

class HeartForm(forms.Form):
    CHOICES=((0,'Typical Angina'),(1,'Atypical Angina'),
             (2,'Non-Anginal Pain'),(3,'Asymptomatic',))
    CHOICES_FBS=((0,'Fasting Blood Sugar < 120 mg/dl'),
                (1,'Fasting Blood Sugar > 120 mg/dl',))
    CHOICES_REST=((0,'Normal',),(1,'having ST-T wave abnormality',),
                  (2,'showing probable or definite left ventricular hypertrophy'))
    CHOICES_EXANG = ((0,0,),(1,1,),(2,2,),(3,3,),(4,4,))
    Chest_Pain_Type=forms.ChoiceField(choices=CHOICES)
    Resting_Blood_Pressure_in_mm_Hg=forms.FloatField()
    Serum_Cholestoral_in_mg_dl=forms.FloatField()
    Fasting_Blood_Sugar=forms.ChoiceField(choices=CHOICES_FBS)
    Resting_Electro_cardiographic_Result=forms.ChoiceField(choices=CHOICES_REST)
    Maximum_Heart_Rate_Achieved= forms.FloatField()
    Slope_of_the_peak=forms.FloatField()
    Coronary_artery= forms.ChoiceField(choices=CHOICES_EXANG)