# Generated by Django 2.2.12 on 2021-11-27 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0019_remove_genero_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='genero',
            name='descricao',
            field=models.CharField(default=0, max_length=20, verbose_name='Descrição'),
        ),
    ]
