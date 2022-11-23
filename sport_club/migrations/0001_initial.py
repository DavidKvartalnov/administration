# Generated by Django 4.0 on 2022-11-22 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('surname', models.CharField(max_length=32)),
                ('patronymic', models.CharField(max_length=16)),
                ('age', models.IntegerField()),
                ('person_sail', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('surname', models.CharField(max_length=32)),
                ('patronymic', models.CharField(max_length=16)),
                ('age', models.IntegerField()),
                ('post', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='SectionKind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('lessons_month_quantity', models.IntegerField()),
                ('single_lesson_price', models.IntegerField()),
                ('customer', models.ManyToManyField(to='sport_club.Customer')),
                ('kind', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sport_club.sectionkind')),
                ('trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sport_club.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('activation_time', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sport_club.customer')),
                ('purchase', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sport_club.section')),
            ],
        ),
    ]