from django import forms
from . import models


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Books
        fields = [
            "title",
            "description"
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ("text",)

        widgets = {
            "text": forms.Textarea(attrs={"class": "form-control"})
        }

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('text',)
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs['class'] = 'form-control'
#         self.fields['text'].widget = Textarea(attrs={'rows':5})