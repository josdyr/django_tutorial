from django.contrib import admin

from .models import Choice, Question, HowTo, Step

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date information',    {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


class StepInline(admin.TabularInline):
    model = Step
    extra = 3


class HowToAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title Information', {'fields': ['title'], 'classes': ['intro']}),
        ('Intro', {'fields': ['intro']}),
    ]
    inlines = [StepInline]
    list_display = ('title', 'intro')


admin.site.register(HowTo, HowToAdmin)
# admin.site.register(Question, QuestionAdmin)
