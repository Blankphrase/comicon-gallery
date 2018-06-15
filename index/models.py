from django.db import models
import datetime as dt


class Location(models.Model):
    '''
    Image location model
    '''
    PLACES=(
        ("Metropolis","Metropolis"),
        ("Gotham","Gotham"),
        ("Central City","Central City"),
        ("Avengers mansion","Avengers mansion"),
        ("Bifrost","Bifrost"),
        ("Wakanda","Wakanda")
        )
    location = models.CharField(max_length=120, choices = PLACES)

    def save_locations(self):
        self.save()

    def delete_locations(self):
        self.delete()

    @classmethod
    def update_location(cls,place, update):
        updated = cls.objects.filter(location=place).update(location=update)
        return updated

    def __str__(self):
        return self.location




