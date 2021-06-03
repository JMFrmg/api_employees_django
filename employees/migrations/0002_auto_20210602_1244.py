# Generated by Django 3.1.6 on 2021-06-02 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('floor', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='age',
            field=models.SmallIntegerField(default=30),
        ),
        migrations.AddField(
            model_name='employee',
            name='city',
            field=models.CharField(default='paris', max_length=200),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.CharField(default='cadre', max_length=200),
        ),
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.SmallIntegerField(default=30000),
        ),
    ]
