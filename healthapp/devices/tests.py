#Below is an example of a test case that tests the search functionality of the application. You can modify any of the existing test code or add new test cases as needed.

from django.test import TestCase
from .models import fda_data, eudamed_data
from django.urls import reverse
class SearchFunctionalityTests(TestCase):
    
    def setUp(self):
        """
        Set up initial test data.
        """
        fda_data.objects.create(device_name="TestDevice1", manufacturer_name="ManufacturerA", k_number="1")
        eudamed_data.objects.create(device_name="TestDevice1", manufacturer_name="ManufacturerA", basic_udi="1")
        fda_data.objects.create(device_name="TestDevice2", manufacturer_name="ManufacturerB", k_number="2")
        self.url = reverse("search_device")
        self.apiurl = reverse("api_search_device")

    def test_device_in_both_tables(self):
        """
        Test that the device found in both tables returns correct data.
        """
        # Perform the search operation
        
        response = self.client.get(self.url, {'device_name': 'TestDevice1'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('ManufacturerA', response.content.decode())

    def test_device_in_fda_only(self):
        """
        Test that a device found only in the FDA table returns correct data.
        """
        response = self.client.get(self.url, {'device_name': 'TestDevice2'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('ManufacturerB', response.content.decode())
        self.assertIn('No results found in Eudamed data.', response.content.decode())

    def test_device_not_found(self):
        """
        Test that searching for a non-existing device returns a not found message.
        """
        response = self.client.get(self.url, {'device_name': 'NonExistentDevice'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('No results', response.content.decode())

    def test_case_insensitive_search(self):
        """
        Test that the search is case insensitive.
        """
        response = self.client.get(self.url, {'device_name': 'testdevice1'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('ManufacturerA', response.content.decode())

    def test_case_non_device_search(self):
        """
        Test that the search is case of non device.
        """
        response = self.client.get(self.url, {'device_name': 'testdevic'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('No results', response.content.decode())
