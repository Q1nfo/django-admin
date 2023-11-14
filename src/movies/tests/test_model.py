from config.test_settings import Settings


class GenreModelTest(Settings):
    def test_value(self):
        self.assertEqual(self.uuid_genre, self.genre.id)
        self.assertEqual('Action', self.genre.name)
        self.assertEqual('Some descriptions about action', self.genre.description)

    def test_equipment_meta(self):
        self.assertEqual('ID', self.genre._meta.get_field('id').verbose_name)
        self.assertEqual(255, self.genre._meta.get_field('name').max_length)
        self.assertEqual(True, self.genre._meta.get_field('description').null)
        self.assertEqual(True, self.genre._meta.get_field('description').blank)


class PersonModelTest(Settings):
    def test_value(self):
        self.assertEqual(self.uuid_person_writer, self.person_writer.id)
        self.assertEqual('Boris', self.person_writer.full_name)

    def test_equipment_meta(self):
        self.assertEqual('ID', self.person_writer._meta.get_field('id').verbose_name)
        self.assertEqual(255, self.person_writer._meta.get_field('full_name').max_length)


class FilmWorkModelTest(Settings):
    def test_value(self):
        self.assertEqual(self.uuid_film_work, self.film_work.id)
        self.assertEqual('Star Wars', self.film_work.title)
        self.assertEqual('Film adventure and actions about stars who are begin at wars', self.film_work.description)
        self.assertEqual('18+', self.film_work.certificate)
        self.assertEqual('film/action/star_wars', self.film_work.file_path)
        self.assertEqual(8.1, self.film_work.rating)
        self.assertEqual('movie', self.film_work.type)

    def test_equipment_meta(self):
        self.assertEqual('ID', self.film_work._meta.get_field('id').verbose_name)
        self.assertEqual(True, self.film_work._meta.get_field('description').blank)
        self.assertEqual(False, self.film_work._meta.get_field('description').null)

    def test_link_with_genre(self):
        self.assertEqual(self.genre, self.film_work.genres.all()[0])

    def test_link_with_persons(self):
        self.assertEqual(self.person_writer, self.film_work.persons.all()[0])
        self.assertEqual(self.person_actor, self.film_work.persons.all()[1])
        self.assertEqual(self.person_director, self.film_work.persons.all()[2])

