from apps.common.models import TimeStampedUUIDModel
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class Profiles(TimeStampedUUIDModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
