# Generated by Django 4.2 on 2023-04-14 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="approval",
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
                ("firstname", models.CharField(max_length=15)),
                ("lastname", models.CharField(max_length=15)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")], max_length=15
                    ),
                ),
                (
                    "race",
                    models.CharField(
                        choices=[("WHITE", "White"), ("BLACK", "Black")], max_length=10
                    ),
                ),
                ("releaseage", models.IntegerField(default=0)),
                (
                    "gangaffilation",
                    models.CharField(
                        choices=[("TRUE", "True"), ("FALSE", "False")], max_length=15
                    ),
                ),
                ("riskscore", models.IntegerField(default=0)),
                (
                    "firstlevel",
                    models.CharField(
                        choices=[
                            ("Standard", "Standard"),
                            ("Specialized", "Specialized"),
                            ("High", "High"),
                        ],
                        max_length=15,
                    ),
                ),
                (
                    "edlevel",
                    models.CharField(
                        choices=[
                            ("Less than HS Diploma", "Less than HS Diploma"),
                            ("High School Diploma", "High School Diploma"),
                            ("At least some college", "At least some college"),
                        ],
                        max_length=25,
                    ),
                ),
                ("dependents", models.IntegerField(default=0)),
                (
                    "prisonoffense",
                    models.CharField(
                        choices=[
                            ("Drug", "Drug"),
                            ("Property", "Property"),
                            ("Violent/Non-Sex", "Violent/Non-Sex"),
                            ("Violent/Sex", "Violent/Sex"),
                            ("Other", "Other"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "prisonyears",
                    models.CharField(
                        choices=[
                            ("1-2 years", "1-2 years"),
                            ("Less than 1 year", "Less than 1 year"),
                            ("Greater than 2 to 3 years", "Greater than 2 to 3 years"),
                            ("More than 3 years", "More than 3 years"),
                        ],
                        max_length=25,
                    ),
                ),
                ("priorarrestfelony", models.IntegerField(default=0)),
                ("priorarrestmisd", models.IntegerField(default=0)),
                ("priorarrestsvio", models.IntegerField(default=0)),
                ("priorarrestsprop", models.IntegerField(default=0)),
                ("priorarrestsdrug", models.IntegerField(default=0)),
                ("priorpvcharges", models.IntegerField(default=0)),
                ("priorconvprop", models.IntegerField(default=0)),
                ("priorconvdrug", models.IntegerField(default=0)),
                ("delenqreports", models.IntegerField(default=0)),
                ("progattend", models.IntegerField(default=0)),
                ("progunexabs", models.IntegerField(default=0)),
                ("residchanges", models.IntegerField(default=0)),
                ("avgdayperdrugtest", models.FloatField(default=0)),
                ("positivethc", models.FloatField(default=0)),
                ("positivecocaine", models.FloatField(default=0)),
                ("positivemeth", models.FloatField(default=0)),
                ("positiveother", models.FloatField(default=0)),
                ("percentemp", models.FloatField(default=0)),
                ("jobsperyear", models.FloatField(default=0)),
                (
                    "empexempt",
                    models.CharField(
                        choices=[("FALSE", "False"), ("TRUE", "True")], max_length=15
                    ),
                ),
            ],
        ),
    ]
