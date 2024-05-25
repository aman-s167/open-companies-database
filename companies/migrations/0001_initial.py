# Generated by Django 4.2.13 on 2024-05-20 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("website_domain", models.TextField(blank=True, null=True)),
                ("linkedin_id", models.CharField(blank=True, max_length=64, null=True)),
                ("name", models.TextField(blank=True, null=True)),
                ("linkedin_profile_url", models.TextField(blank=True, null=True)),
                ("year_founded", models.DateField(blank=True, null=True)),
                ("logo_url", models.TextField(blank=True, null=True)),
                ("short_description", models.TextField(blank=True, null=True)),
                ("long_description", models.TextField(blank=True, null=True)),
                ("linkedin_description", models.TextField(blank=True, null=True)),
                ("linkedin_specialities", models.TextField(blank=True, null=True)),
                ("linkedin_industries", models.TextField(blank=True, null=True)),
                ("categories", models.TextField(blank=True, null=True)),
                ("competitor_website_domains", models.TextField(blank=True, null=True)),
                ("hq_country", models.TextField(blank=True, null=True)),
                ("largest_headcount_country", models.TextField(blank=True, null=True)),
                ("hq_street_address_and_city", models.TextField(blank=True, null=True)),
                ("all_office_addresses", models.TextField(blank=True, null=True)),
                ("markets", models.TextField(blank=True, null=True)),
                (
                    "acquisition_status",
                    models.CharField(blank=True, max_length=64, null=True),
                ),
                ("last_funding_round_type", models.TextField(blank=True, null=True)),
                ("valuation_usd", models.BigIntegerField(blank=True, null=True)),
                ("valuation_date", models.DateField(blank=True, null=True)),
                ("investors", models.TextField(blank=True, null=True)),
                ("total_investment_usd", models.BigIntegerField(blank=True, null=True)),
                (
                    "days_since_last_fundraise",
                    models.IntegerField(blank=True, null=True),
                ),
                (
                    "last_funding_round_investment_usd",
                    models.BigIntegerField(blank=True, null=True),
                ),
                (
                    "valuation_lower_bound_usd",
                    models.BigIntegerField(blank=True, null=True),
                ),
            ],
            options={
                "unique_together": {("website_domain", "linkedin_id")},
            },
        ),
    ]
