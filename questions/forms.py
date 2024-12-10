from django import forms
from .models import ProgrammingQuestion

class ProgrammingQuestionForm(forms.ModelForm):
    class Meta:
        model = ProgrammingQuestion
        fields = ['title', 'description', 'input_example', 'output_example', 'difficulty']
