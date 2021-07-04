from django import forms

class KidneyForm(forms.Form):
    CHOICES_AL = ((0, 1,), (1, 2,), (2, 3,), (3, 4,), (4, 5,))
    CHOICES_BSL =((0,'Blood Sugar < 140 mg/dl'),
                (1,'Blood Sugar > 140 mg/dl',))
    CHOICES_RBC = ((0,'Red Blood Cell Count (4.7 to 6.1 [cell/mcl]'),
                (1,'Red Blood Cell Count (less then 4.7 or greater then 6.1 [cell/mcl]',))
    CHOICES_PC = ((0,'5 to 8'),
                (1,'less then 5 or graeter then 8',))
    CHOICES_PCC = ((0,'6 to 10'),
                (1,'less then 6 or graeter then 10',))

    Blood_Pressure = forms.FloatField()
    Specific_Gravity = forms.FloatField()
    Albumin= forms.ChoiceField(choices=CHOICES_AL)
    Blood_Sugar_Level = forms.ChoiceField(choices=CHOICES_BSL)
    Red_Blood_Cells_Count = forms.ChoiceField(choices=CHOICES_RBC)
    Pus_Cell_Count = forms.ChoiceField(choices=CHOICES_PC)
    Pus_Cell_Clumps = forms.ChoiceField(choices=CHOICES_PCC)