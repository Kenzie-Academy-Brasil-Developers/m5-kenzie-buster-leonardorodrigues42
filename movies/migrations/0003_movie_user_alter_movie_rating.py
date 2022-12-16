# Generated by Django 4.1.4 on 2022-12-13 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0002_alter_movie_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.CharField(choices=[('G', 'G'), ('PG', 'Pg'), ('PG-13', 'Pg 13'), ('R', 'R'), ('NC-17', 'Nc 17')], default='G', max_length=20, null=True),
        ),
    ]