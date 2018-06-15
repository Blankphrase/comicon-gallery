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

class CategoryTestClass(TestCase):
    '''
    test instance,saving,deleting,updating
    '''
    def setUp(self):
        self.test = Category(name="DC")

    def test_instance(self):
        self.assertTrue(isinstance(self.test, Category))

    def test_saving_category(self):
        self.test.save_category()
        images = Category.objects.all()
        self.assertTrue(len(images) > 0)

    def test_deleting_category(self):
        self.test.save_category()
        self.test.delete_category()
        locationss = Category.objects.all()
        self.assertTrue(len(locationss) < 1)

    def test_updating_category(self):
        self.test.save_category()
        updated = Category.update_category("DC", 'Marvel')
        self.assertTrue(updated, 'Marvel')







