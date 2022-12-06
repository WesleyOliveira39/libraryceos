from django.forms import Form, ModelForm
from .models import *
from sys import prefix
from django import forms
from numpy import require
from cadastros import models
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['comentario']

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
    student = forms.CharField(max_length=250)
    book = forms.CharField(max_length=250)
    borrowing_date = forms.DateField()
    return_date = forms.DateField()
    status = forms.CharField(max_length=2)

    class Meta:
        model = models.Borrow
        fields = ('student', 'book', 'borrowing_date',
                  'return_date', 'status', )

    def clean_student(self):
        student = int(self.data['student']) if (
            self.data['student']).isnumeric() else 0
        try:
            student = models.User.objects.get(id=student)
            return student
        except:
            raise forms.ValidationError("Invalid student.")

    def clean_book(self):
        book = int(self.data['book']) if (self.data['book']).isnumeric() else 0
        try:
            book = models.Exemplar.objects.get(id=book)
            return book
        except:
            raise forms.ValidationError("Invalid Book.")


       
        


    
