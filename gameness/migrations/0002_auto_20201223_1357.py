# Generated by Django 3.1.4 on 2020-12-23 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameness', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='suspected',
            field=models.BooleanField(default=False, verbose_name='This game is suspected'),
        ),
        migrations.AlterField(
            model_name='suspectedgame',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='suspects', to='gameness.game'),
        ),
    ]