from django import forms
from . models import Comment
from mptt.forms import TreeNodeChoiceField


class CommentForm(forms.ModelForm):
    # parent = TreeNodeChoiceField(queryset=Comment.objects.all())
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['parent'].required = False
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.TextInput(attrs={'class':'form-control'})
        }
