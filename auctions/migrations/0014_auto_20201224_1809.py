# Generated by Django 3.1.2 on 2020-12-24 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20201224_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='bids',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='last_bid',
        ),
        migrations.AddField(
            model_name='listing',
            name='latestbid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lastest_bid', to='auctions.bid'),
        ),
    ]
