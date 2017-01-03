#!/usr/bin/env python3
# ThomasBot
# Author: Thomas Zakrajsek
# Copyright 2017
from core import main_loop
import core.conversational
import core.persistence

# Start the main loop
try:
    main_loop.run_forever()
finally:
    main_loop.close()
