import charts_handler
import inspect_interface
from freeorion_debug.option_tools import get_option_dict, HANDLERS

handlers = get_option_dict()[HANDLERS].split()

for handler in handlers:
    __import__('freeorion_debug.handlers.%s' % handler)

