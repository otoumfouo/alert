# Generated by Django 3.2.9 on 2022-01-11 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rapport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction', models.CharField(max_length=90)),
                ('conlusion', models.CharField(max_length=90)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Requerant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=90)),
                ('contacts', models.CharField(max_length=90)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Requistion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_requistion', models.CharField(max_length=90)),
                ('objet', models.CharField(max_length=90)),
                ('dpll', models.FileField(blank=True, max_length=300, null=True, upload_to='static/media/requisition/', verbose_name='fichier')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('date_demande', models.DateField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('requerant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requerants', to='requisition.requerant')),
            ],
        ),
        migrations.CreateModel(
            name='RapportImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, max_length=300, null=True, upload_to='static/media/requisition/', verbose_name='fichier')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('rapport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rapport_requ_simage', to='requisition.rapport')),
            ],
        ),
        migrations.CreateModel(
            name='RapportDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mise_en_cause', models.CharField(max_length=90)),
                ('observation', models.CharField(max_length=90)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='camera_requ', to='event.camera')),
                ('rapport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rapport_requ', to='requisition.rapport')),
            ],
        ),
        migrations.AddField(
            model_name='rapport',
            name='requistion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requerant_requ', to='requisition.requistion'),
        ),
    ]
