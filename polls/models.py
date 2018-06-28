import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Document(models.Model):
    title = models.CharField(max_length=80)
    # author = ?
    pub_date = models.DateTimeField('publish on')
    slug = models.CharField(max_length=80)

    class Meta:
        abstract = True


class HowTo(Document):
    intro = models.CharField(max_length=500)

    def __str__(self):
        return '(title:"' + self.title + '"), (' + 'intro:"' + self.intro + '")'


class Step(models.Model):
    how_to = models.ForeignKey(HowTo, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    markdown_content = models.CharField(max_length=5000) # chang the length


class Tag(models.Model):
    how_to = models.ForeignKey(HowTo, on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=18)


# class TheoreticalArticle(models.Model):
