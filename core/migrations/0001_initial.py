# Generated by Django 2.2.2 on 2019-06-25 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('autor', models.CharField(max_length=100, verbose_name='Autor')),
                ('preço', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Preço')),
                ('imagem', models.ImageField(upload_to='media/', verbose_name='Imagem')),
            ],
        ),
    ]
