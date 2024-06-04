# Generated by Django 5.0.6 on 2024-06-04 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apporion', '0005_alter_detalhes_usuarios_id_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='CNAE_PRINCIPAL_CODIGO',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='CNAE_PRINCIPAL_CODIGO',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='operadoras',
            name='CNAE_PRINCIPAL_CODIGO',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='DATA_ABERTURA',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='FOTO',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='detalhes_usuarios',
            name='FOTO',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='DATA_ABERTURA',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='LOGOMARCA',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='operadoras',
            name='DATA_ABERTURA',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='operadoras',
            name='LOGOMARCA',
            field=models.TextField(null=True),
        ),
    ]
