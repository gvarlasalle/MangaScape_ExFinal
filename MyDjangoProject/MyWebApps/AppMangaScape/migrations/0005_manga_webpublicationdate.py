# Generated by Django 5.0.6 on 2024-07-02 08:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AppMangaScape", "0004_remove_manga_artistid_remove_manga_authorid_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="manga",
            name="WebPublicationDate",
            field=models.DateField(blank=True, null=True),
        ),
    ]
