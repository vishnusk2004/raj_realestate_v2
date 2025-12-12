from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Raj', '0025_openhouse_open_house_end_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertylisting',
            name='property_status',
            field=models.CharField(choices=[('coming_soon', 'Coming Soon'), ('just_listed', 'Just Listed'), ('for_sale', 'For Sale'), ('for_lease', 'For Lease'), ('under_contract', 'Under-Contract'), ('just_sold', 'Just Sold')], default='for_sale', help_text='Marketing status of the listing', max_length=20),
        ),
        migrations.AddField(
            model_name='propertylisting',
            name='listing_agent_image',
            field=models.ImageField(blank=True, help_text='Optional image of the listing agent', null=True, upload_to='listing_agents/'),
        ),
        migrations.AddField(
            model_name='propertylisting',
            name='listing_agent_name',
            field=models.CharField(blank=True, help_text='Name of the listing agent for courtesy credit', max_length=200, null=True),
        ),
    ]

