from django.db import models
import uuid

class Club(models.Model):
    club_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.JSONField(default=list)  # List of member user IDs
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    event_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, related_name="events"
    )  # Connects events to a club
    date = models.DateTimeField()
    description = models.TextField()
    location = models.CharField(max_length=100)
    participants = models.JSONField(default=list)  # List of participant user IDs

    def __str__(self):
        return self.name
