# Generated by Django 3.1 on 2020-08-27 21:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appliances', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=1000)),
                ('model_number', models.CharField(max_length=50)),
                ('serial_number', models.CharField(max_length=50)),
                ('rating', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('purchase_date', models.DateTimeField(blank=True, null=True)),
                ('notes', models.TextField(max_length=10000)),
                ('appliance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appliances.appliance')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]