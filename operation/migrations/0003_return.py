# Generated by Django 3.0.7 on 2020-07-10 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_product'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operation', '0002_issue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Return',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('version', models.IntegerField(default=0)),
                ('is_locked', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('code', models.CharField(max_length=255, unique=True)),
                ('unit', models.IntegerField(verbose_name='Units')),
                ('date', models.DateField(verbose_name='Return Date')),
                ('receipt_no', models.CharField(blank=True, max_length=100, null=True, verbose_name='Receipt No.')),
                ('customer', models.CharField(blank=True, max_length=100, null=True, verbose_name='Customer Name')),
                ('remarks', models.TextField(blank=True, null=True, verbose_name='Remarks')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='catalogue.Product')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Returned Product',
                'verbose_name_plural': 'Returned Products',
                'ordering': ['code'],
                'get_latest_by': 'date',
            },
        ),
    ]
