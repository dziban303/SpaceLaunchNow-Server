import datetime
import json

from rest_framework import status

from api.models import Astronauts
from api.tests.test__base import SLNAPITests


class AstronautTest(SLNAPITests):

    def test_v330_astronauts(self):
        """
        Ensure astronaut endpoints work as expected.
        """
        path = '/api/3.3.0/astronauts/'
        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data['count'], 1)
        starman = Astronauts.objects.get(name=data['results'][0]['name'])
        self.assertEqual(data['results'][0]['name'], starman.name)
        self.assertEqual(data['results'][0]['born'],
                         "2018-02-06")
        self.assertEqual(data['results'][0]['status']['name'],
                         starman.status.name)
        self.assertEqual(data['results'][0]['nationality'],
                         starman.nationality)
        self.assertEqual(data['results'][0]['agency']['name'],
                         starman.agency.name)
        self.assertEqual(data['results'][0]['twitter'],
                         starman.twitter)
        self.assertEqual(data['results'][0]['bio'],
                         starman.bio)