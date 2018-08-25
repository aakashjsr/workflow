from django.forms import ModelForm
from core.models import Question


class QuestionForm(ModelForm):
    class Meta:
        model = Question
