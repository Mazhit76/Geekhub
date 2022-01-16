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
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=512, null=True, verbose_name='Жалоба')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('A', 'Approved'), ('M', 'Moderating'), ('D', 'Discarded')], default='M', max_length=1, verbose_name='Статус')),
                ('reason_for_rejection', models.CharField(blank=True, max_length=512, null=True, verbose_name='Причина отклонения')),
                ('object_id', models.CharField(max_length=40, null=True)),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Жалоба',
                'verbose_name_plural': 'Жалобы',
            },
        ),
    ]
