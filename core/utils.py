import logging

from django.template.loader import get_template
from django.core.mail import send_mail
from django.conf import settings
from smtplib import SMTPException


def send_email(template_name, subject, to, context):
    """
    Sends email using the specified template.
    :param template_name: name of template
    :param subject: subject for email
    :param to: recipient of email
    :param context: data to be passed into template
    :return: status of whether the email was sent or not
    """
    html_template = get_template("{}.html".format(template_name))
    send_mail(
        subject=subject,
        message=html_template.render(context),
        html_message=html_template.render(context),
        from_email=settings.EMAIL_FROM,
        recipient_list=[to],
        fail_silently=False
    )


def notify_interviewer(questionaire):
    send_email(
        "notify_interviewer",
        "Received Answers",
        questionaire.interviewer.email,
        {"id": questionaire.id, "email": questionaire.interviewee_email}
    )


def notify_interviewee(questionaire):
    send_email(
        "notify_interviewee",
        "Request for answers",
        questionaire.interviewee_email,
        {"id": questionaire.id}
    )


def reject_notification(questionaire):
    send_email(
        "rejected",
        "Answers Rejected",
        questionaire.interviewer.email,
        {"id": questionaire.id, "email": questionaire.interviewee_email}
    )