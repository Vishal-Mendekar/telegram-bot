from collections import defaultdict, deque

user_memory = defaultdict(lambda: deque(maxlen=3))

def add_message(user_id, query, response):
    user_memory[user_id].append((query, response))

def get_history(user_id):
    return list(user_memory[user_id])