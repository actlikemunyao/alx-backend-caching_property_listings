
from django.core.cache import cache
from django_redis import get_redis_connection
from .models import Property

CACHE_KEY = 'all_properties'

def get_all_properties():
    data = cache.get(CACHE_KEY)
    if data is None:
        qs = Property.objects.all().values('id','title','description','price','location','created_at')
        data = list(qs)
        cache.set(CACHE_KEY, data, 3600)
    return data

def get_redis_cache_metrics():
    r = get_redis_connection('default')
    info = r.info()
    hits = info.get('keyspace_hits', 0)
    misses = info.get('keyspace_misses', 0)
    total = hits + misses
    hit_ratio = (hits / total) if total else 0.0
    return {'keyspace_hits': hits, 'keyspace_misses': misses, 'hit_ratio': hit_ratio}
