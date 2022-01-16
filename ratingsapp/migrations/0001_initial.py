# Generated by Django 3.2.4 on 2021-12-23 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(choices=[(1, 'LIKE'), (-1, 'DISLIKE')], verbose_name='Рейтинг')),
                ('object_id', models.CharField(max_length=40)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Счетчик рейтинга',
                'verbose_name_plural': 'Счетчики рейтинга',
            },
        ),
    ]
