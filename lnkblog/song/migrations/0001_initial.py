# Generated by Django 2.0.4 on 2018-04-30 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicNotations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_notation', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Scale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=2)),
                ('pattern', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.FileField(null=True, upload_to='media')),
                ('lyrics', models.TextField()),
                ('lyrics_syllables', models.TextField()),
                ('scale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='song.Scale')),
            ],
        ),
        migrations.AddField(
            model_name='musicnotations',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='song.Song'),
        ),
    ]