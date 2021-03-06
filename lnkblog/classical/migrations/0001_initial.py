# Generated by Django 2.0.4 on 2018-04-26 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('design', '0002_auto_20180424_1157'),
        ('plans', '0001_initial'),
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guitar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voice_sample', models.FileField(null=True, upload_to='media')),
                ('back_plates_and_sides', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guitar_back', to='materials.Wood')),
                ('braces', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guitar_braces', to='materials.Wood')),
                ('neck_joint', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='neck_to_body_joint', to='design.NeckBodyJoint')),
                ('neck_wood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guitar_neck', to='materials.Wood')),
                ('plan_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plans.Plan')),
                ('top_plates', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guitar_top', to='materials.Wood')),
            ],
        ),
        migrations.CreateModel(
            name='GuitarImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='media')),
                ('guitar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='classical.Guitar')),
            ],
        ),
    ]
