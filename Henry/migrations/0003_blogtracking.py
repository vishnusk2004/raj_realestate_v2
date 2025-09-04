# Generated manually for BlogTracking model

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Henry', '0002_sellingcontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogTracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_code', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('blog_post_id', models.IntegerField(help_text='ID of the blog post being tracked')),
                ('member_name', models.CharField(help_text='Name of the member receiving the link', max_length=200)),
                ('member_email', models.EmailField(help_text='Email of the member receiving the link', max_length=254)),
                ('member_phone', models.CharField(blank=True, help_text='Phone number of the member', max_length=20, null=True)),
                ('crm_reference', models.CharField(blank=True, help_text='Reference from CRM system', max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('opened_at', models.DateTimeField(blank=True, help_text='When the link was first opened', null=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, help_text='IP address of the opener', null=True)),
                ('user_agent', models.TextField(blank=True, help_text='Browser/device information', null=True)),
                ('is_opened', models.BooleanField(default=False, help_text='Whether the link has been opened')),
            ],
            options={
                'verbose_name': 'Blog Tracking',
                'verbose_name_plural': 'Blog Trackings',
                'ordering': ['-created_at'],
            },
        ),
    ]
