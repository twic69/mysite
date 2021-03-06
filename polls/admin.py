from django.contrib import admin
from .models import Question, Choice

class ChoiceAdmin(admin.StackedInline):
    model = Choice
    extra = 3

    fieldsets =[
        ("Answers", {"fields" : ["text", "votes"]} ),
    ]

class QuestionAdmin(admin.ModelAdmin):
    fieldsets =[
    ("Text", {"fields" : ["text"]} ),

    ("Publish date", {"fields" : ["pub_date"]} ),
    ]
    inlines = [ChoiceAdmin]
    list_filter = ["pub_date"]
    search_fields = ["text"]

admin.site.register(Question, QuestionAdmin)