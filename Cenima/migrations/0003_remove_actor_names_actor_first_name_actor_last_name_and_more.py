# Generated by Django 4.1.5 on 2023-03-21 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cenima', '0002_actor_avatar_alter_movie_genre_alter_movie_imdb_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='names',
        ),
        migrations.AddField(
            model_name='actor',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='actor',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='actor',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=450),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(),
        ),
    ]
