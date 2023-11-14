import uuid

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    birth_date = models.DateTimeField()


class Genre(models.Model):
    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(_('название'), max_length=255)
    description = models.TextField(_('описание'), null=True, blank=True)

    created_at = models.DateTimeField('дата создания', auto_created=True, auto_now_add=True,
                                      null=True, blank=True)
    updated_at = models.DateTimeField('дата обновления', auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = _('жанр')
        verbose_name_plural = _('жанры')
        # db_table = 'content"."genre'
        db_table = 'genre'

    def __str__(self):
        return self.name


class Person(models.Model):
    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4(), editable=False)
    full_name = models.CharField(_('полное имя'), max_length=255)
    birth_date = models.DateField(_('день рождения'), null=True, blank=True)

    created_at = models.DateTimeField('дата создания', auto_created=True, auto_now_add=True,
                                      null=True, blank=True)
    updated_at = models.DateTimeField('дата обновления', auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = 'личность'
        verbose_name_plural = 'личности'
        # db_table = 'content"."person'
        db_table = 'person'

    def __str__(self):
        return self.full_name


class FilmWorkType(models.TextChoices):
    MOVIE = 'movie', _('фильм')
    TV_SHOW = 'tv_show', _('шоу')


class FilmWork(models.Model):
    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4(), editable=False)
    title = models.TextField(_('название'))
    description = models.TextField(_('описание'), blank=True, null=False)
    creation_date = models.DateField(_('дата создания фильма'), blank=True)
    certificate = models.TextField(_('сертификат'), blank=True, null=False)
    file_path = models.FileField(_('файл'), upload_to='film_works/', blank=True)
    rating = models.FloatField(_('рейтинг'), validators=[MinValueValidator(0)], blank=True, null=False)
    type = models.CharField(_('тип'), max_length=20, choices=FilmWorkType.choices)
    genres = models.ManyToManyField(Genre, through='movies.GenreFilmWork')
    persons = models.ManyToManyField(Person, through='movies.PersonFilmWork')

    created_at = models.DateTimeField('дата создания', auto_created=True, auto_now_add=True,
                                      null=True, blank=True)
    updated_at = models.DateTimeField('дата обновления', auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = _('кинопроизведение')
        verbose_name_plural = _('кинопроизведения')
        # db_table = 'content"."film_work'
        db_table = 'film_work'

    def __str__(self):
        return self.title


class GenreFilmWork(models.Model):
    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4(), editable=False)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    film_work = models.ForeignKey(FilmWork, on_delete=models.CASCADE)
    created_at = models.DateTimeField('дата создания', auto_created=True, auto_now_add=True)

    class Meta:
        verbose_name = 'Жанр кинопроизведения'
        verbose_name_plural = 'Жанры кинопроизведений'
        # db_table = 'content"."genre_film_work'
        db_table = 'genre_film_work'
        unique_together = ('film_work_id', 'genre')

    def __str__(self):
        return str(self.id)


class PersonRole(models.TextChoices):
    ACTOR = 'actor', _('актер')
    DIRECTOR = 'director', _('режиссер')
    WRITER = 'writer', _('сценарист')


class PersonFilmWork(models.Model):
    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4(), editable=False)
    film_work = models.ForeignKey(FilmWork, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.CharField(_('роль'), max_length=20, choices=PersonRole.choices)
    created_at = models.DateTimeField('дата создания', auto_created=True, auto_now_add=True)

    class Meta:
        verbose_name = 'Участие личности в кинопроизведении'
        verbose_name_plural = 'Личности в кинопроизведениях'
        # db_table = 'content"."person_film_work'
        db_table = 'person_film_work'
        unique_together = ('film_work', 'person', 'role')

    def __str__(self):
        return str(self.id)
