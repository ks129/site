from django.core.validators import RegexValidator
from django.db import models


class DocumentationLink(models.Model):
    """A documentation link used by the `!docs` command of the bot."""

    package = models.CharField(primary_key=True, max_length=50)
    base_url = models.URLField()
    inventory_url = models.URLField()


class OffTopicChannelName(models.Model):
    name = models.CharField(
        primary_key=True,
        max_length=96,
        validators=(RegexValidator(regex=r'^[a-z0-9-]+$'),)
    )


class SnakeName(models.Model):
    """A snake name used by the bot's snake cog."""

    name = models.CharField(primary_key=True, max_length=100)
    scientific = models.CharField(max_length=150)