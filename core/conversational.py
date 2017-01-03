import functools
import signal

from core import main_loop
from core.persistence import memory, save_memory

def accept_input():
    user_input = input("tb> ")
    save_memory("user_input", user_input)
    process_input(user_input)

def process_input(user_input):
    # very naive processing for now
    if user_input == "memory":
        print(memory)
    if user_input == "sleep":
        sleep()

def sleep():
    print("Zzzzzz")
    main_loop.stop()

# CTRL-C 
main_loop.add_signal_handler(getattr(signal, 'SIGINT'), accept_input)

