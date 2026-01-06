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
