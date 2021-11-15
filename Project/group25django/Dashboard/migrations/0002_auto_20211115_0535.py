# Generated by Django 3.2.9 on 2021-11-15 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Macro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('currentWeight', models.IntegerField(blank=True, null=True, verbose_name='Weight (lb):')),
                ('calories', models.IntegerField(verbose_name='Calories:')),
                ('protein', models.IntegerField(verbose_name='Protein (g):')),
                ('fat', models.IntegerField(verbose_name='Total fat (g):')),
                ('carbs', models.IntegerField(verbose_name='Total carbohydrates (g):')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.user')),
            ],
        ),
        migrations.CreateModel(
            name='store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField(verbose_name='Height')),
                ('weight', models.IntegerField(verbose_name='Weight')),
            ],
        ),
        migrations.DeleteModel(
            name='Macros',
        ),
    ]
