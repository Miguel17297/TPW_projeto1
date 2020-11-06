from django import forms


class accountForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=40)
    nmec = forms.IntegerField()
    nome = forms.CharField(max_length=70)
    cc = forms.IntegerField()
    especialidade = forms.CharField(max_length=40,required=False)
    gabinte = forms.IntegerField(required=False)
    cedula = forms.IntegerField()
