# Generated by Django 3.1 on 2023-11-14 11:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmWork',
            fields=[
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True, null=True, verbose_name='дата создания')),
                ('id', models.UUIDField(default=uuid.UUID('97c28e7f-cc87-450f-9293-69c2cf48a72f'), editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='название')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('creation_date', models.DateField(blank=True, verbose_name='дата создания фильма')),
                ('certificate', models.TextField(blank=True, verbose_name='сертификат')),
                ('file_path', models.FileField(blank=True, upload_to='film_works/', verbose_name='файл')),
                ('rating', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='рейтинг')),
                ('type', models.CharField(choices=[('movie', 'фильм'), ('tv_show', 'шоу')], max_length=20, verbose_name='тип')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='дата обновления')),
            ],
            options={
                'verbose_name': 'кинопроизведение',
                'verbose_name_plural': 'кинопроизведения',
                'db_table': 'film_work',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True, null=True, verbose_name='дата создания')),
                ('id', models.UUIDField(default=uuid.UUID('b93ab59c-3217-4e2f-900c-5bd9b4866e27'), editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='дата обновления')),
            ],
            options={
                'verbose_name': 'жанр',
                'verbose_name_plural': 'жанры',
                'db_table': 'genre',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True, null=True, verbose_name='дата создания')),
                ('id', models.UUIDField(default=uuid.UUID('8b07c71d-9748-482f-bad9-6a98acc18150'), editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='полное имя')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='день рождения')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='дата обновления')),
            ],
            options={
                'verbose_name': 'личность',
                'verbose_name_plural': 'личности',
                'db_table': 'person',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonFilmWork',
            fields=[
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='дата создания')),
                ('id', models.UUIDField(default=uuid.UUID('e2197358-c72d-4edb-8b5d-680d0afcd068'), editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('actor', 'актер'), ('director', 'режиссер'), ('writer', 'сценарист')], max_length=20, verbose_name='роль')),
                ('film_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.person')),
            ],
            options={
                'verbose_name': 'Участие личности в кинопроизведении',
                'verbose_name_plural': 'Личности в кинопроизведениях',
                'db_table': 'person_film_work',
                'unique_together': {('film_work', 'person', 'role')},
            },
        ),
        migrations.CreateModel(
            name='GenreFilmWork',
            fields=[
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='дата создания')),
                ('id', models.UUIDField(default=uuid.UUID('efdca28d-8dd7-404c-af07-9a17963a3015'), editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre')),
            ],
            options={
                'verbose_name': 'Жанр кинопроизведения',
                'verbose_name_plural': 'Жанры кинопроизведений',
                'db_table': 'genre_film_work',
                'unique_together': {('film_work_id', 'genre')},
            },
        ),
        migrations.AddField(
            model_name='filmwork',
            name='genres',
            field=models.ManyToManyField(through='movies.GenreFilmWork', to='movies.Genre'),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='persons',
            field=models.ManyToManyField(through='movies.PersonFilmWork', to='movies.Person'),
        ),
    ]
