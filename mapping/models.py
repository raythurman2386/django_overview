import logging

from django.db import models

logger = logging.getLogger(__name__)


class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        logger.debug(f"Saving location: {self.name}")
        try:
            super().save(*args, **kwargs)
            logger.info(f"Successfully saved location: {self.name}")
        except Exception as e:
            logger.error(f"Error saving location {self.name}: {str(e)}", exc_info=True)
            raise

    def delete(self, *args, **kwargs):
        logger.info(f"Deleting location: {self.name}")
        try:
            super().delete(*args, **kwargs)
            logger.info(f"Successfully deleted location: {self.name}")
        except Exception as e:
            logger.error(
                f"Error deleting location {self.name}: {str(e)}", exc_info=True
            )
            raise
