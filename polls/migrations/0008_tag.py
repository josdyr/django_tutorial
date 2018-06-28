# Generated by Django 2.0.6 on 2018-06-28 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20180628_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=18)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.HowTo')),
            ],
        ),
    ]