from flask_caching import Cache
from utils.constants import UPDATE_SECONDS

cache = Cache(config={
    'CACHE_TYPE': 'FileSystemCache',
    'CACHE_DIR': 'cache-directory',
    'CACHE_DEFAULT_TIMEOUT': 3600 # 3600 seconds = 1 hour rate limit
})
