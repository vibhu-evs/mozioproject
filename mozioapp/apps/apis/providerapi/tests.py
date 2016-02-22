from rest_framework import status
from rest_framework.test import APITestCase
from .models import Providers, ServiceArea


class ProviderTest(APITestCase):

    def setUp(self):
        self.payload = {
            'name': 'test', 'email': 'test1@test.com',
            'phone_no': "+919990677865", 'language': 'en', 'currency': 'USD'}
        self.provider = Providers.objects.create(
            name="test",
            email="test@test.com",
            phone_no=000000,
            language="en",
            currency="USD")
        self.pk = self.provider.id
        self.endpoint = "/api/provider"

    def test_can_create_provider(self):
        endpoint = self.endpoint
        endpoint = "%s/" % (self.endpoint,)
        response = self.client.post(endpoint, self.payload)
        self.assertEqual(response.status_code, 201)

    def test_can_update_provider(self):
        endpoint = "%s/%s/" % (self.endpoint, self.pk)
        payload = self.payload
        payload["name"] = "test123"
        response = self.client.put(endpoint, payload)
        self.assertEqual(response.status_code, 200)

    def test_can_retrieve_provider(self):
        endpoint = "%s/%s/" % (self.endpoint, self.pk)
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 200)

    def test_can_add_servicearea(self):
        endpoint = "%s/%s/servicearea/" % (self.endpoint, self.pk)
        payload = {
            "polygon": [[
                [12.84528, 77.696], [12.82084, 77.67368],
                [12.85427, 77.66235], [12.84528, 77.696]]],
            "name": "electronic city, Bangalore",
            "price": 100,
        }
        response = self.client.post(endpoint, payload, format='json')
        self.assertEqual(response.status_code, 201)

    def test_can_view_servicearea(self):
        endpoint = "%s/%s/servicearea/" % (self.endpoint, self.pk)
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 200)

    def test_can_delete_provider(self):
        endpoint = "%s/%s/" % (self.endpoint, self.pk)
        response = self.client.delete(endpoint)
        self.assertEqual(response.status_code, 204)



class ServiceAreaTest(APITestCase):

    def setUp(self):
        self.payload = {
            "polygon": [[
                [12.84528, 77.696], [12.82084, 77.67368],
                [12.85427, 77.66235], [12.84528, 77.696]]],
            "name": "electronic city, Bangalore",
            "price": 100,
        }
        self.provider = Providers.objects.create(
            name="test",
            email="test@test.com",
            phone_no="+918885687654",
            language="en",
            currency="USD")
        self.servicearea = ServiceArea.objects.create(
            polygon=[[
                [12.84528, 77.696], [12.82084, 77.67368],
                [12.85427, 77.66235], [12.84528, 77.696]]],
            name="test",
            price="1000",
            provider_id=str(self.provider.id))
        self.pk = self.servicearea.id
        self.endpoint = "/api/service/area"

    def test_can_update_servicearea(self):
        endpoint = "%s/%s/" % (self.endpoint, self.pk)
        payload = self.payload
        payload["name"] = "test123",
        payload["provider_id"] = str(self.provider.id)
        response = self.client.put(endpoint, payload, format='json')
        self.assertEqual(response.status_code, 200)

    def test_can_retrieve_servicearea(self):
        endpoint = "%s/%s/" % (self.endpoint, self.pk)
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 200)

    def test_can_delete_servicearea(self):
        endpoint = "%s/%s/" % (self.endpoint, self.pk)
        response = self.client.delete(endpoint)
        self.assertEqual(response.status_code, 204)
