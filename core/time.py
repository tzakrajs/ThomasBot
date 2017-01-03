import calendar
import time

def get_epoch():
  return calendar.timegm(time.gmtime())
