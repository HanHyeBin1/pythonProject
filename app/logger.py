import logging
import sys

#log
mylogger = logging.getLogger("mylogger")

formatter = logging.Formatter('[%(levelname)s] %(message)s')

handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

mylogger.addHandler(handler)
mylogger.setLevel(logging.DEBUG)

mylogger.debug("This is a debug message.")
mylogger.info("Some info message.")
mylogger.warning("A warning.")