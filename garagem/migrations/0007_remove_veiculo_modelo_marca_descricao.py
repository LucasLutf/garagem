# Generated by Django 4.2.1 on 2023-05-09 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0006_remove_marca_modelo_veiculo_modelo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculo',
            name='modelo',
        ),
        migrations.AddField(
            model_name='marca',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
    ]
