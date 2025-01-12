# Generated by Django 3.2.12 on 2024-06-28 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0001_initial'),
        ('interests', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userservice',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='service',
            name='interests',
            field=models.ManyToManyField(blank=True, related_name='services', to='interests.Interest'),
        ),
        migrations.AddField(
            model_name='service',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='categories.subcategory'),
        ),
        migrations.AlterUniqueTogether(
            name='userservice',
            unique_together={('user', 'service')},
        ),
    ]
