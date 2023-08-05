# from django.db import models
from django.contrib.gis.db import models
import uuid

# Create your models here.


class Place(models.Model):
    place_id = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.PointField()

    def __str__(self):
        return self.name

    def get_details(self):
        return {
            "place_id": self.place_id,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at,
            "location": {"latitude": self.location.y, "longitude": self.location.x},
        }
