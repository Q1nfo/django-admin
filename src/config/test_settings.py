import uuid
from unittest import TestCase

from django.utils import timezone

from movies.models import Genre, Person, FilmWork, GenreFilmWork, PersonFilmWork, PersonRole


class Settings(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.uuid_genre = uuid.uuid4()
        cls.genre = Genre.objects.create(
            id=cls.uuid_genre,
            name='Action',
            description='Some descriptions about action'
        )

        cls.uuid_person_writer = uuid.uuid4()
        cls.person_writer = Person.objects.create(
            id=cls.uuid_person_writer,
            full_name='Boris',
            birth_date=timezone.now()
        )

        cls.uuid_person_actor = uuid.uuid4()
        cls.person_actor = Person.objects.create(
            id=cls.uuid_person_actor,
            full_name='Maxim',
            birth_date=timezone.now(),
        )

        cls.uuid_person_director = uuid.uuid4()
        cls.person_director = Person.objects.create(
            id=cls.uuid_person_director,
            full_name='Leonid',
            birth_date=timezone.now()
        )

        cls.uuid_film_work = uuid.uuid4()
        cls.film_work = FilmWork.objects.create(
            id=cls.uuid_film_work,
            title='Star Wars',
            description='Film adventure and actions about stars who are begin at wars',
            creation_date=timezone.now(),
            certificate='18+',
            file_path='film/action/star_wars',
            rating=8.1,
            type='movie'
        )

        cls.uuid_genre_film_work = uuid.uuid4()
        cls.genre_film_work = GenreFilmWork.objects.create(
            id=cls.uuid_film_work,
            genre=cls.genre,
            film_work=cls.film_work
        )

        cls.uuid_person_director_film_work = uuid.uuid4()
        cls.person_director_film_work = PersonFilmWork.objects.create(
            id=cls.uuid_person_director_film_work,
            film_work=cls.film_work,
            person=cls.person_director,
            role=PersonRole.DIRECTOR
        )

        cls.uuid_person_actor_film_work = uuid.uuid4()
        cls.person_director_film_work = PersonFilmWork.objects.create(
            id=cls.uuid_person_actor_film_work,
            film_work=cls.film_work,
            person=cls.person_actor,
            role=PersonRole.ACTOR
        )

        cls.uuid_person_writer_film_work = uuid.uuid4()
        cls.person_director_film_work = PersonFilmWork.objects.create(
            id=cls.uuid_person_writer_film_work,
            film_work=cls.film_work,
            person=cls.person_writer,
            role=PersonRole.WRITER
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        GenreFilmWork.objects.filter(
            film_work=cls.film_work
        ).delete()
        PersonFilmWork.objects.filter(
            film_work=cls.film_work
        ).delete()
        Person.objects.filter(
            id=cls.person_director.id
        ).delete()
        Person.objects.filter(
            id=cls.person_writer.id
        ).delete()
        Person.objects.filter(
            id=cls.person_actor.id
        ).delete()
        Genre.objects.filter(
            id=cls.genre.id
        ).delete()
        FilmWork.objects.filter(
            id=cls.film_work.id
        ).delete()




