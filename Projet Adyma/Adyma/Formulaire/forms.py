from django import forms
from .models import Snippet, Beneficiaire, FicheTest, PsychoSocial, Residence, Ehpad, Etablissement
from .models import Coach, Groupe
from django.forms import ModelForm




class BeneficiaireForm(ModelForm):

    class Meta:
        model = Beneficiaire
        fields = '__all__'

class FicheTestForm(ModelForm):

    class Meta:
        model = FicheTest
        fields = '__all__'

class PsychoSocialForm(ModelForm):
    class Meta:
        model = PsychoSocial
        fields = '__all__'


class ResidenceForm(ModelForm):
    class Meta:
        model = Residence
        fields = '__all__'       

class EhpadForm(ModelForm):
    class Meta:
        model = Ehpad
        fields = '__all__'   

class EtablissementForm(ModelForm):
    class Meta:
        model = Etablissement
        fields = '__all__'    

class CoachForm(ModelForm):
    class Meta:
        model = Coach
        fields = '__all__' 

class GroupForm(ModelForm):
    class Meta:
        model = Groupe
        fields = '__all__'   

        

        