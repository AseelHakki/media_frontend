# Generated by Django 4.2.8 on 2023-12-20 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('security_media_app', '0002_alter_mediaatt_id_relt_alter_mediaifad_id_relb'),
        ('core', '0003_remove_user_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.ForeignKey(default='b3663c255db3486682933bd74c764890', on_delete=django.db.models.deletion.DO_NOTHING, to='security_media_app.department'),
            preserve_default=False,
        ),
    ]
