from django import forms
from cadastros.models import Comentario
'''
class ComentarioForm(forms.ModelForm):
    comentario = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Deixe seu comentário aqui.',
        'rows':'4',}))
    
    class Meta:
        model = Comentario
        fields = ('comentario',)'''
