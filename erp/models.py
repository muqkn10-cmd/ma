from django.db import models


class Placeholder(models.Model):
    """A tiny model so the erp app has at least one model for migrations.

    This prevents Django from raising import/migrations errors in minimal
    deployments (CI/builds) where the full erp models may be missing.
    """
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Placeholder"
        verbose_name_plural = "Placeholders"
