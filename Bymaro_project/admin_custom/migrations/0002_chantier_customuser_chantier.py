# Generated by Django 5.0.7 on 2024-07-22 10:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_custom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chantier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='chantier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CustomUser', to='admin_custom.chantier'),
        ),
    ]
