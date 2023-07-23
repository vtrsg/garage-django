# Generated by Django 4.2.3 on 2023-07-23 00:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('BrandId', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ModelType',
            fields=[
                ('ModelId', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(blank=True, max_length=100)),
                ('Phone', models.CharField(max_length=50)),
                ('Cpf', models.CharField(max_length=11, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('YearId', models.AutoField(primary_key=True, serialize=False)),
                ('YearName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('CarId', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Location', models.PositiveSmallIntegerField(choices=[(0, 'Minas Gerais'), (1, 'Rio de Janeiro'), (2, 'São Paulo')])),
                ('Transmission', models.PositiveSmallIntegerField(choices=[(0, 'Automático'), (1, 'Manual')])),
                ('Price', models.FloatField()),
                ('DiscountPrice', models.FloatField(blank=True, null=True)),
                ('Mileage', models.FloatField()),
                ('Color', models.CharField(max_length=100)),
                ('Seat', models.PositiveSmallIntegerField(choices=[(0, '2'), (1, '4'), (2, '5'), (3, '7')])),
                ('Fuel', models.PositiveSmallIntegerField(choices=[(0, 'Diesel'), (1, 'Flex'), (2, 'Gasolina'), (3, 'Gasolina Regular'), (2, 'Elétrico'), (2, 'Híbrido')])),
                ('CreatedDate', models.DateField(default=django.utils.timezone.now)),
                ('Brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.brand')),
                ('Model', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.modeltype')),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.user')),
                ('Year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.year')),
            ],
        ),
    ]
