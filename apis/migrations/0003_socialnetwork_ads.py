# Generated by Django 4.2.4 on 2023-09-02 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_alter_customer_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ['created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=150)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('caption', models.TextField(blank=True, null=True)),
                ('customer_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='apis.customergroup')),
                ('social_network', models.ManyToManyField(to='apis.socialnetwork')),
            ],
            options={
                'ordering': ['created'],
                'abstract': False,
            },
        ),
    ]
