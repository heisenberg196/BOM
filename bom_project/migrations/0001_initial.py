# Generated by Django 3.0.7 on 2020-08-17 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=120, unique=True, verbose_name='Project Name')),
                ('project_desc', models.TextField(blank=True, null=True, verbose_name='Project Description')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_number', models.SlugField(unique=True)),
                ('part_desc', models.TextField()),
                ('status', models.CharField(choices=[('done', 'Done'), ('improve', 'Needs Improvement'), ('pending', 'Pending'), ('discuss', 'Discuss Later')], default='pending', max_length=10)),
                ('parent_part', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_assembly', to='bom_project.Part')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='bom_project.Project')),
            ],
        ),
    ]
