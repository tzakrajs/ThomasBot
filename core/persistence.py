import glob
import json
import os

from core.time import get_epoch
from core.async import PeriodicTask

memory = {}

def main():
    global memory
    memory = load_memory_from_disk()

def get_memory():
    return memory

def save_memory(type, value):
    if not memory.get(type):
        memory[type] = []
    memory[type].append(value)

def persist_memory_to_disk():
    with open('thomasbot_memory_{0}.json'.format(get_epoch()), 'w') as outfile:
        json.dump(memory, outfile)

def load_memory_from_disk():
    latest = max(glob.iglob('thomasbot_memory*.json'), key=os.path.getctime)
    with open(latest, 'r') as infile:
        return json.load(infile)

main()

task = PeriodicTask(persist_memory_to_disk, 60)
