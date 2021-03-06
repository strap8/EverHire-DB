# Generated by Django 2.1.2 on 2018-11-20 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250, null=True)),
                ('image', models.TextField(blank=True)),
                ('title', models.CharField(max_length=250, null=True)),
                ('description', models.TextField(null=True)),
                ('lat', models.DecimalField(decimal_places=14, max_digits=17)),
                ('lng', models.DecimalField(decimal_places=14, max_digits=17)),
                ('phone_number', models.CharField(max_length=12, null=True)),
                ('tags', models.CharField(blank=True, max_length=128)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('status', models.SmallIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobAuthorName', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobModifier', to=settings.AUTH_USER_MODEL)),
                ('worker', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='jobWorker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
