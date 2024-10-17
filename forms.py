from django.forms import ModelForm
from .models import *
class Movies_Form(ModelForm):
     class Meta :
         model =  todoitem_movie
         fields = '__all__'
