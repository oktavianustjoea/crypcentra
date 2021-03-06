# Generated by Django 3.2.6 on 2021-09-01 03:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BidWindow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Bid Name')),
                ('total_tokens', models.IntegerField(verbose_name='Total Tokens')),
                ('start_time', models.DateTimeField(verbose_name='Start Time')),
                ('end_time', models.DateTimeField(verbose_name='End Time')),
                ('is_auctioned', models.BooleanField(default=False, verbose_name='Auction?')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_tokens', models.IntegerField(verbose_name='Number of Tokens')),
                ('bidding_price', models.DecimalField(decimal_places=2, max_digits=32, verbose_name='Bidding Price')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')),
                ('success_tokens', models.IntegerField(blank=True, null=True, verbose_name='Number of Success Tokens')),
                ('bid_window', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='window_bids', to='ico.bidwindow')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bids', to=settings.AUTH_USER_MODEL, verbose_name='Bids')),
            ],
        ),
    ]
