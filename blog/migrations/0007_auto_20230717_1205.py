# Generated by Django 3.2.20 on 2023-07-17 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20230715_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='Comment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.comment'),
            preserve_default=False,
        ),
    ]
