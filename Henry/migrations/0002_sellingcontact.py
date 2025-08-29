# Generated manually

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Henry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellingContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('property_address', models.TextField(blank=True, null=True)),
                ('property_type', models.CharField(blank=True, max_length=50, null=True)),
                ('estimated_value', models.CharField(blank=True, max_length=50, null=True)),
                ('timeline', models.CharField(blank=True, max_length=50, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]


