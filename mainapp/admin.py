from django.contrib import admin

from mainapp.models import TestCategory, Test, Answer, Question


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    fields = ('title', 'description', ('category', ))
    search_fields = ('title', )
    ordering = ('title', )


@admin.register(TestCategory)
class TestCategory(admin.ModelAdmin):
    list_display = ('name', 'description')


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ("pk", "short_description")
    list_display_links = ("short_description",)


class AnswerAdmin(admin.ModelAdmin):
    model = Answer
    list_display = ("pk", "short_text", "question_id")
    list_display_links = ("short_text",)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
