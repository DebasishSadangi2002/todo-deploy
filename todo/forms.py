from django import forms
from .models import Task

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'compleated']

        def __init__(self, *args, **kwargs):
            super(TodoItemForm, self).__init__(*args, **kwargs)
            self.fields['description'].required = False
