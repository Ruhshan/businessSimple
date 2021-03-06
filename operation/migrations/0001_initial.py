# Generated by Django 3.0.7 on 2020-07-08 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogue', '0004_product'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Receive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('version', models.IntegerField(default=0)),
                ('is_locked', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('code', models.CharField(max_length=255, unique=True)),
                ('unit', models.IntegerField(verbose_name='Units')),
                ('date', models.DateField(verbose_name='Receive Date')),
                ('receipt_no', models.CharField(blank=True, max_length=100, null=True, verbose_name='Receipt No.')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='catalogue.Product')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Receive Product',
                'verbose_name_plural': 'Received Products',
                'ordering': ['code'],
                'get_latest_by': 'created_at',
            },
        ),
    ]
