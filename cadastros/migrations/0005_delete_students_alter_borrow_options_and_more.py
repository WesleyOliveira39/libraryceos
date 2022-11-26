# Generated by Django 4.0.3 on 2022-11-26 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0004_alter_borrow_book_alter_borrow_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Students',
        ),
        migrations.AlterModelOptions(
            name='borrow',
            options={'verbose_name_plural': 'Empréstimos'},
        ),
        migrations.AlterField(
            model_name='borrow',
            name='status',
            field=models.CharField(choices=[('1', 'Pendente'), ('2', 'OK')], default=1, max_length=2),
        ),
    ]