from django.test import TestCase
from index.models import Location, Category, Image

class LocationTestClass(TestCase):
    '''
    test instance,saving,deleting,updating
    '''
    def setUp(self):
        self.test_location = Location(location="Wakanda")

    def test_instance(self):
        self.assertTrue(isinstance(self.test_location, Location))

    def test_saving_location(self):
        self.test_location.save_locations()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

    def test_deleting_locations(self):
        self.test_location = Location(location="Wakanda")
        self.test_location.save_locations()
        self.test_location.delete_locations()
        locations = Location.objects.all()
        self.assertTrue(len(locations) < 1)

    def test_updating_image(self):
        self.test_location = Location(location="Wakanda")
        self.test_location.save_locations()
        updated = Location.update_location("Wakanda", "Bifrost")
        self.assertTrue(updated, "Bifrost")




