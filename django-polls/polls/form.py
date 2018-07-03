from django import forms
from .models import Question, Choice

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        labels = {'Question': ''}

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']
        labels = {'Choice': ''}



