# Generated by Django 3.0.3 on 2020-02-11 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0047_add_workflow_models'),
        ('tests', '0052_custom_doc_image_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleTask',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Task')),
            ],
            bases=('wagtailcore.task',),
        ),
    ]
