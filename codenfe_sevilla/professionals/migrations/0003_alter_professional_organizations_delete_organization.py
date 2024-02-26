# Generated by Django 4.2.7 on 2024-02-26 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '__first__'),
        ('professionals', '0002_professional_organizations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional',
            name='organizations',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profesionals', to='organizations.organization'),
        ),
        migrations.DeleteModel(
            name='Organization',
        ),
    ]
