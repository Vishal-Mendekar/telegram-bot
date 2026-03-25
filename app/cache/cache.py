query_cache = {}

def get_cached(query):
    if query in query_cache:
        print("⚡ CACHE HIT")
        return query_cache[query]
    print("CACHE MISS")
    return None

def set_cache(query, result):
    print("Storing in cache")
    query_cache[query] = result