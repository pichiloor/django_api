import unittest
from django.test.client import RequestFactory

from django_api.views import booking_detail, booking_list, event_detail, event_list, room_detail, room_list


class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_rooms(self):
        # Create an instance of a GET request.
        request = self.factory.get('/rooms/')

        # Test room_list() as if it were deployed at /rooms
        response = room_list(request)
        self.assertEqual(response.status_code, 200)

    def test_rooms_detail(self):
        # Create an instance of a GET request.
        request = self.factory.get('/rooms/1')

        # Test room_detail() as if it were deployed at /rooms/details
        response = room_detail(request, 1)
        self.assertEqual(response.status_code, 200)

    def test_rooms_create(self):
        # Create an instance of a POST request.
        request = self.factory.post(
            '/rooms/', {'name': 'Room30', 'description': 'This is the New Room 30 '})

        # Test room_detail() as if it were deployed at /rooms/
        response = room_list(request)
        self.assertEqual(response.status_code, 201)

    def test_rooms_update(self):
        # Create an instance of a PUT request.
        request = self.factory.put(
            '/rooms/2', {'name': 'Room2', 'description': 'This is the Room 2 Updated'}, content_type='application/json')

        # Test room_detail() as if it were deployed at /rooms/details
        response = room_detail(request, 2)
        self.assertEqual(response.status_code, 200)

    def test_events(self):
        # Create an instance of a GET request.
        request = self.factory.get('/events/')

        # Test event_list() as if it were deployed at /events/details
        response = event_list(request)
        self.assertEqual(response.status_code, 200)

    def test_events_detail(self):
        # Create an instance of a GET request.
        request = self.factory.get('/events/3')

        # Test my_view() as if it were deployed at /events/details
        response = event_detail(request, 3)
        self.assertEqual(response.status_code, 200)

    def test_booking(self):
        # Create an instance of a GET request.
        request = self.factory.get('/booking/')

        # Test my_view() as if it were deployed at /customer/details
        response = booking_list(request)
        self.assertEqual(response.status_code, 200)

    def test_booking_detail(self):
        # Create an instance of a GET request.
        request = self.factory.get('/booking/2')

        # Test my_view() as if it were deployed at /customer/details
        response = booking_detail(request, 2)
        self.assertEqual(response.status_code, 200)
