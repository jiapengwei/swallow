# Generated by Django 2.1 on 2019-02-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_auto_20190212_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cpu',
            name='Server',
        ),
        migrations.AddField(
            model_name='server',
            name='cpu_core_count',
            field=models.SmallIntegerField(default=1, help_text='CPU核数', verbose_name='CPU核数'),
        ),
        migrations.AddField(
            model_name='server',
            name='cpu_logic_count',
            field=models.SmallIntegerField(default=1, help_text='逻辑CPU个数', verbose_name='逻辑CPU个数'),
        ),
        migrations.AddField(
            model_name='server',
            name='cpu_model',
            field=models.CharField(default='a', help_text='CPU型号', max_length=32, verbose_name='CPU型号'),
        ),
        migrations.AddField(
            model_name='server',
            name='cpu_physics_count',
            field=models.SmallIntegerField(default=1, help_text='物理CPU个数', verbose_name='物理CPU个数'),
        ),
        migrations.DeleteModel(
            name='Cpu',
        ),
    ]