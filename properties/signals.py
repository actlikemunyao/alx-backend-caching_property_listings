
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Property
from .utils import CACHE_KEY

@receiver(post_save, sender=Property)
def invalidate_on_save(sender, instance, **kwargs):
    cache.delete(CACHE_KEY)

@receiver(post_delete, sender=Property)
def invalidate_on_delete(sender, instance, **kwargs):
    cache.delete(CACHE_KEY)
