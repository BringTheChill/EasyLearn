# Generated by Django 3.0.7 on 2020-06-08 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0019_auto_20200608_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teachers',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_teacher': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teachers_to_courses', to=settings.AUTH_USER_MODEL),
        ),
    ]