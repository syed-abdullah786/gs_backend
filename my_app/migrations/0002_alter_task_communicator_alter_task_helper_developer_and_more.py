# Generated by Django 4.1.2 on 2023-07-14 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='communicator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='communicator', to='my_app.employee'),
        ),
        migrations.AlterField(
            model_name='task',
            name='helper_developer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='helper', to='my_app.employee'),
        ),
        migrations.AlterField(
            model_name='task',
            name='main_developer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='developer', to='my_app.employee'),
        ),
    ]