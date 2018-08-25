from django.contrib import admin
from core.models import *


class QuestionLinkInline(admin.TabularInline):
    model = QuestionLink
    extra = 2 # how many rows to show


class QuestionaireAdmin(admin.ModelAdmin):
    inlines = (QuestionLinkInline,)
    list_filter = ("status", )
    list_display = ("name", "interviewer", "status")


admin.site.register(User)
admin.site.register(Questionaire, QuestionaireAdmin)
admin.site.register(Question)
