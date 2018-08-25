from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Question(models.Model):
    question = models.CharField(max_length=256)

    def __str__(self):
        return self.question


class Questionaire(models.Model):
    name = models.CharField(max_length=128)
    interviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questionaires")
    interviewee_email = models.EmailField()
    questions = models.ManyToManyField(Question, through="QuestionLink", related_name="question_links")
    status = models.CharField(max_length=20, choices=[
        ("Pending Review", "Pending Review"), ("Accepted", "Accepted"), ("Rejected", "Rejected")
    ], default="Pending Review")

    def __str__(self):
        return "{} - {}".format(self.interviewer.email, self.interviewee_email)


class QuestionLink(models.Model):
    type = models.CharField(max_length=25, choices=[("text", "text"), ("binary", "binary")])
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=2048, blank=True, default='')
    questionaire = models.ForeignKey(Questionaire, on_delete=models.CASCADE)

