#Below is an example of a test case that tests the search functionality of the application. Feel free to make any edits you see fit.

from django.test import TestCase
from .models import FdaData, EudamedData

class SearchFunctionalityTests(TestCase):
    
    def setUp(self):
        """
        Set up initial test data.
        """
        FdaData.objects.create(device_name="TestDevice1", manufacturer_name="ManufacturerA")
        EudamedData.objects.create(device_name="TestDevice1", manufacturer_name="ManufacturerA")
        FdaData.objects.create(device_name="TestDevice2", manufacturer_name="ManufacturerB")

    def test_device_in_both_tables(self):
        """
        Test that the device found in both tables returns correct data.
        """
        # Perform the search operation
        response = self.client.get('/search/', {'device_name': 'TestDevice1'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('ManufacturerA', response.content.decode())

    def test_device_in_fda_only(self):
        """
        Test that a device found only in the FDA table returns correct data.
        """
        response = self.client.get('/search/', {'device_name': 'TestDevice2'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('ManufacturerB', response.content.decode())
        self.assertIn('Not found in Eudamed', response.content.decode())

    def test_device_not_found(self):
        """
        Test that searching for a non-existing device returns a not found message.
        """
        response = self.client.get('/search/', {'device_name': 'NonExistentDevice'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Not found in both tables', response.content.decode())
