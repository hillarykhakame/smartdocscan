# Generated by Django 5.1 on 2024-08-15 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_document_document_name_document_document_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='extracted_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]