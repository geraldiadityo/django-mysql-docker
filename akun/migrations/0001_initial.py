# Generated by Django 3.2.11 on 2022-04-13 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Akun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_akun', models.CharField(blank=True, max_length=200, null=True)),
                ('kode_akun', models.CharField(blank=True, max_length=20, null=True)),
                ('kategori', models.CharField(choices=[('Kredit', 'Kredit'), ('Debit', 'Debit')], max_length=10, null=True)),
            ],
        ),
    ]
