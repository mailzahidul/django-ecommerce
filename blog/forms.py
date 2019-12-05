from django import forms
from .models import BlogCrete

class BlogCreteForm(forms.ModelForm):
    class Meta:
        model = BlogCrete
        fields = ('__all__')
        widgets = {
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.SelectMultiple(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'feature_img':forms.TextInput(attrs={'class':'form-control'}),
        }