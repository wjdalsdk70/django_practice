# Generated by Django 4.1.5 on 2023-01-11 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fcuser", "0002_alter_fcuser_username"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="fcuser",
            options={"verbose_name": "패스트캠퍼스 사용자", "verbose_name_plural": "패스트캠퍼스 사용자"},
        ),
        migrations.AddField(
            model_name="fcuser",
            name="useremail",
            field=models.EmailField(
                default="test@gmail.com", max_length=128, verbose_name="사용자이메일"
            ),
            preserve_default=False,
        ),
    ]
