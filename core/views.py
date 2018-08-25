from django.views import View
from django.shortcuts import render
from django.contrib import messages

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from core.models import Questionaire, QuestionLink
from core.utils import notify_interviewer, notify_interviewee


class QuestionView(View):
    def get(self, request, *args, **kwargs):
        questionaire = Questionaire.objects.filter(id=kwargs.get("id", 0))
        if not questionaire.exists():
            return HttpResponse("Invalid Page")
        questionaire = questionaire.first()
        return render(request, "workflow.html", {"question_links": questionaire.questionlink_set.all()})

    def post(self, request, *args, **kwargs):
        questionaire = None
        print(request.POST)
        for id in request.POST.keys():
            try:
                q_id = int(id)
            except ValueError:
                continue
            else:
                q = QuestionLink.objects.get(id=id)
                questionaire = q.questionaire
                q.answer = request.POST.get(id)
                q.save()
        notify_interviewer(questionaire)
        return render(request, "success.html")


class RequestAnswerView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            id = request.GET.get("id", -1)
            questionaire = Questionaire.objects.filter(id=id)
            if not questionaire.exists():
                return HttpResponseRedirect("/admin/core/")
            questionaire = questionaire.first()
            for question_link in questionaire.questionlink_set.all():
                question_link.answer = ""
                question_link.save()
            # request email sent
            notify_interviewee(questionaire)
            messages.add_message(request, messages.INFO, 'Email sent successfully')
            return HttpResponseRedirect("/admin/core/questionaire/{}".format(id))
        return HttpResponseForbidden("Unauthorised Access.")