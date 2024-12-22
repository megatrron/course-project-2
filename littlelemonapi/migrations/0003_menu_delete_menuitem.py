# Generated by Django 5.1.4 on 2024-12-22 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('littlelemonapi', '0002_menuitem_delete_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('menu_item_description', models.TextField(default='', max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
    ]
