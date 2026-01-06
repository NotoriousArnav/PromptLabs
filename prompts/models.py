from django.db import models
from uuid import uuid4

# Create your models here.
class Prompt(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid4,
            editable=False
        )

    prompt = models.TextField() # Field that will contain the Prompt
    tags = models.CharField(max_length=200) # Comma Seperated tags
    expected_output = models.ImageField(upload_to='media/prompts/expected_output/', blank=True, null=True)
