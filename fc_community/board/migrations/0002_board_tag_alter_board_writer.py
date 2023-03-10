# Generated by Django 4.1.5 on 2023-01-18 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tag", "0001_initial"),
        ("fcuser", "0003_alter_fcuser_options_fcuser_useremail"),
        ("board", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="board",
            name="tag",
            field=models.ManyToManyField(to="tag.tag", verbose_name="태그"),
        ),
        migrations.AlterField(
            model_name="board",
            name="writer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="fcuser.fcuser",
                verbose_name="작성자",
            ),
        ),
    ]
