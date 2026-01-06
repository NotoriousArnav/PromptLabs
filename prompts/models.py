from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.
class Prompt(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid4,
            editable=False
        )

    author = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            related_name="prompts",
            default=1
        )

    prompt = models.TextField() # Field that will contain the Prompt
    tags = models.CharField(max_length=200) # Comma Seperated tags
    expected_output = models.ImageField(upload_to='media/prompts/expected_output/', blank=True, null=True)

class Vote(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid4,
            editable=False
        )

    prompt = models.ForeignKey(
            Prompt,
            on_delete=models.CASCADE,
            related_name="votes",
        )

    voter = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            related_name="votes",
            default=1
        )

    VOTE_CHOICES = [
            (1, "Upvote"),
            (-1, "Downvote")
        ]
    value = models.IntegerField(choices=VOTE_CHOICES)

    def __add__(self, obj):
        if not isinstance(obj, Vote):
            raise Exception("Vote can be only added to Vote")
        return self.value + obj.value

    def __repr__(self):
        return str(self.value)
