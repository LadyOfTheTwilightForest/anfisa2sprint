# Generated by Django 3.2.16 on 2024-04-14 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='icecream',
            options={'verbose_name': 'мороженное', 'verbose_name_plural': 'Мороженные'},
        ),
        migrations.AlterModelOptions(
            name='topping',
            options={'verbose_name': 'топпинг', 'verbose_name_plural': 'Топпинги'},
        ),
        migrations.AlterModelOptions(
            name='wrapper',
            options={'verbose_name': 'обёртка', 'verbose_name_plural': 'Обёртки'},
        ),
        migrations.AlterField(
            model_name='category',
            name='output_order',
            field=models.PositiveSmallIntegerField(default=100, verbose_name='Порядок отображения'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=64, unique=True, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ice_creams', to='ice_cream.category', verbose_name='Категория'),
        ),
    ]
