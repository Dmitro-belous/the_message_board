# Generated by Django 4.2 on 2023-07-06 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryType', models.CharField(choices=[('TA', 'Танк'), ('HE', 'Хилер'), ('DD', 'Дамагер'), ('ME', 'Торговец'), ('GM', 'Гилдмастер'), ('QG', 'Квестгивер'), ('SM', 'Кузнец'), ('TN', 'Кожевник'), ('PM', 'Зельевар'), ('SM', 'Мастер заклинаний')], default='TA', max_length=2)),
                ('time_add', models.DateTimeField(auto_now_add=True)),
                ('head', models.CharField(max_length=256)),
                ('body', models.TextField()),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('time_add', models.DateTimeField(auto_now_add=True)),
                ('response_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.announcement')),
                ('response_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]