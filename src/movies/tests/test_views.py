from django.urls import reverse
from django.test import Client

from config.test_settings import Settings


class TestViews(Settings):
    def setUp(self):
        self.client = Client()

    def test_get_all_movies(self):
        url = reverse('movies-list')
        result = self.client.get(url)

        results = [{'id': str(self.film_work.id), 'title': 'Star Wars',
                    'description': 'Film adventure and actions about stars who are begin at wars',
                    'creation_date': '2023-11-14', 'rating': 8.1, 'type': 'movie', 'actors': ['Maxim'],
                    'directors': ['Leonid'], 'writers': ['Boris'], 'genre': ['Action']}]

        self.assertEqual(200, result.status_code)
        self.assertEqual(1, result.json().get('count'))
        self.assertEqual(1, result.json().get('total_pages'))
        self.assertEqual(results, result.json().get('results'))

    def test_get_detail(self):
        url = f'/api/v1/movies/{str(self.film_work.id)}/'

        result = self.client.get(url)

        self.assertEqual(200, result.status_code)
        self.assertEqual(str(self.film_work.id), result.json().get('id'))
        self.assertEqual(self.film_work.title, result.json().get('title'))
        self.assertEqual(self.film_work.description, result.json().get('description'))
        self.assertEqual(self.film_work.type, result.json().get('type'))
        self.assertEqual(self.film_work.rating, result.json().get('rating'))


