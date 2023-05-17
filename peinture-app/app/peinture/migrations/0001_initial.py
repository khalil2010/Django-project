# Generated by Django 4.2.1 on 2023-05-16 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Base_Couleur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color_code', models.CharField(max_length=7)),
                ('hex_code', models.CharField(default='', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='couleur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hex_code', models.CharField(max_length=7, unique=True)),
                ('color_code', models.CharField(default='', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='marque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='voiture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('annee', models.IntegerField()),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peinture.couleur')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peinture.marque')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Formule_Base_Couleur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qte', models.DecimalField(decimal_places=2, max_digits=5)),
                ('base_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peinture.base_couleur')),
                ('formule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peinture.couleur')),
            ],
        ),
    ]
