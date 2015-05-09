import sys
import charts_handler
from traceback import print_exc

from freeorion_debug.option_tools import get_option_dict, HANDLERS

handlers = get_option_dict()[HANDLERS].split()

for handler in handlers:
    try:
        __import__('freeorion_debug.handlers.%s' % handler)
    except Exception as e:
        print >> sys.stderr, "Fail to import handler %s wit error %s" % (handler, e)
        print_exc()
        exit(1)
