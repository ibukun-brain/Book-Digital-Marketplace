# Generated by Django 3.2.7 on 2023-01-02 13:56

from django.db import migrations, models
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_solution_solution_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='solution',
            options={'base_manager_name': 'prefetch_manager', 'ordering': ['name', 'created_at']},
        ),
        migrations.AlterModelManagers(
            name='solution',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='solution',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solution',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
