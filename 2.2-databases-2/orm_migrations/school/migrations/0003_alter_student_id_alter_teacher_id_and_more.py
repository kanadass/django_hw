# Generated by Django 5.0.2 on 2024-02-12 12:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0002_remove_student_teacher_alter_student_group_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="teacherstudent",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
