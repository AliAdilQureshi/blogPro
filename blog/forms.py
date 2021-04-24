from django import forms

from .models import Post


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, label='username')
    contact_email = forms.EmailField(required=True,  label='Email')
    content = forms.CharField(required=True, max_length=2000, widget=forms.Textarea(), label='Message')
    

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

        widgets = {
            'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }
