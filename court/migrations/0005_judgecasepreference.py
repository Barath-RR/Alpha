# Generated by Django 4.0.3 on 2022-09-20 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('court', '0004_fixedcasedate'),
    ]

    operations = [
        migrations.CreateModel(
            name='JudgeCasePreference',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('section', models.CharField(max_length=250)),
                ('preference_order', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='court.user')),
            ],
        ),
    ]