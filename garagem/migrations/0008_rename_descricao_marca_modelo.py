# Generated by Django 4.2.1 on 2023-05-09 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0007_remove_veiculo_modelo_marca_descricao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marca',
            old_name='descricao',
            new_name='modelo',
        ),
    ]