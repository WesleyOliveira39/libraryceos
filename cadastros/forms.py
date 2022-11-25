from django.forms import Form, ModelForm
from .models import *
from sys import prefix
from django import forms
from numpy import require
from cadastros import models
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget

class AutorForm(forms.ModelForm):
    required_css_class = 'required'

    data_nascimento = forms.DateField(
        label='Data',
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
            }),
        input_formats=('%Y-%m-%d',),
    )
    
    class Meta:
        model = Autor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AutorForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class SaveBorrow(forms.ModelForm):
    user = forms.CharField(max_length=250)
    exemplar = forms.CharField(max_length=250)
    borrowing_date = forms.DateField()
    return_date = forms.DateField()
    status = forms.CharField(max_length=2)

    class Meta:
        model = models.Borrow
        fields = ('user', 'exemplar', 'borrowing_date',
                  'return_date', 'status', )


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['comentario']
        
    
