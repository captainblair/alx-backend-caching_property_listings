from django.core.cache import cache
from django_redis import get_redis_connection
import logging
from .models import Property

def get_all_properties():
    properties = cache.get('all_properties')
    if properties is None:
        properties = Property.objects.all()
        cache.set('all_properties', properties, 3600)
    return properties

def get_redis_cache_metrics():
    redis_conn = get_redis_connection("default")
    info = redis_conn.info()
    
    keyspace_hits = info.get('keyspace_hits', 0)
    keyspace_misses = info.get('keyspace_misses', 0)
    
    total_requests = keyspace_hits + keyspace_misses
    hit_ratio = keyspace_hits / total_requests if total_requests > 0 else 0
    
    metrics = {
        'keyspace_hits': keyspace_hits,
        'keyspace_misses': keyspace_misses,
        'hit_ratio': hit_ratio
    }
    
    logging.info(f"Redis Cache Metrics: {metrics}")
    return metrics