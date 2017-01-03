memory = {}

def save_memory(type, value):
    if not memory.get(type):
        memory[type] = []
    memory[type].append(value)
