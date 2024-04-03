# Generated by Django 5.0.3 on 2024-04-03 11:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nutrition_facts", "0003_delete_nutritionfacts"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ingredient",
            name="carbohydrates_total_g",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="ingredient",
            name="fiber_g",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="ingredient",
            name="potassium_mg",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="ingredient",
            name="sodium_mg",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
