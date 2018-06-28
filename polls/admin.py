from django.contrib import admin

# from .models import Choice, Question
from .models import HowTo, Step
# from .models import Tag

# Register your models here.
# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3
#
#
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,                  {'fields': ['question_text']}),
#         ('Date information',    {'fields': ['pub_date']}),
#     ]
#     inlines = [ChoiceInline]
#     list_display = ('question_text', 'pub_date', 'was_published_recently')
#     list_filter = ['pub_date']
#     search_fields = ['question_text']


# class TagInline(admin.TabularInline):
#     model = Tag
#     extra = 3


class StepInline(admin.TabularInline):
    model = Step
    extra = 3


class HowToAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title Information', {'fields': ['title']}),
        ('Time of Publishing', {'fields': ['pub_date']}),
        ('Intro, Slug', {'fields': ['intro', 'slug']}),
        (None, {'fields': ['tags']}),
    ]
    inlines = [StepInline]
    # inlines = [TagInline]
    list_display = ('title', 'pub_date', 'intro')
    search_fields = ['title']


# class TheoreticalArticle(admin.ModelAdmin):
#     pass


# admin.site.register(Question, QuestionAdmin)
admin.site.register(HowTo, HowToAdmin)
# admin.site.register(TheoreticalArticle, TheoreticalArticleAdmin)
