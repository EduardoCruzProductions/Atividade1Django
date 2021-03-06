# Generated by Django 2.2 on 2019-08-09 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('versao', models.CharField(max_length=5)),
                ('dataLancamento', models.DateField(auto_now=True, verbose_name='Data de Lançamento')),
                ('descricao', models.TextField(verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataCompra', models.DateField(auto_now=True, verbose_name='Data de Compra')),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('desconto', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('dataLancamento', models.DateField(auto_now=True, verbose_name='Data de Lançamento')),
                ('versao', models.CharField(max_length=5)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Preço')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Produto')),
            ],
        ),
        migrations.CreateModel(
            name='ItensVenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('desconto', models.DecimalField(decimal_places=2, max_digits=6)),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Modulo')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Venda')),
            ],
        ),
    ]
