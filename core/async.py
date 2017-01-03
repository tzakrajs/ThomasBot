from core import main_loop

# SRC - https://mail.python.org/pipermail/python-list/2013-November/661061.html
class PeriodicTask(object):
    def __init__(self, func, interval):
        self.func = func
        self.interval = interval
        self._set()
    def _set(self):
        self._handler = main_loop.call_later(self.interval, self._run)
    def _run(self):
        self.func()
        self._set()
