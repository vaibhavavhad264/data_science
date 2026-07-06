# import logging as lg
#
#
# lg.basicConfig(level=lg.INFO)
# lg.info("This is info")
#
# lg.warning("This is warning")
# lg.error("This is error")

import logging as lg

"""
lg.basicConfig(level = lg.DEBUG)
lg.debug('This is a debug message')
lg.info("This is information message")
lg.warning("This is warning message")
lg.error("This is error message")
lg.critical("This is critical message")


O/p
DEBUG:root:This is a debug message
INFO:root:This is information message
WARNING:root:This is warning message
ERROR:root:This is error message
CRITICAL:root:This is critical message
"""

"""
lg.basicConfig(level = lg.INFO)
lg.debug('This is a debug message')
lg.info("This is information message")
lg.warning("This is warning message")
lg.error("This is error message")
lg.critical("This is critical message")

O/P

INFO:root:This is information message
WARNING:root:This is warning message
ERROR:root:This is error message
CRITICAL:root:This is critical message

"""

"""
lg.basicConfig(level = lg.WARNING)
lg.debug('This is a debug message')
lg.info("This is information message")
lg.warning("This is warning message")
lg.error("This is error message")
lg.critical("This is critical message")

O/P

WARNING:root:This is warning message
ERROR:root:This is error message
CRITICAL:root:This is critical message

"""

"""

lg.basicConfig(level = lg.ERROR)
lg.debug('This is a debug message')
lg.info("This is information message")
lg.warning("This is warning message")
lg.error("This is error message")
lg.critical("This is critical message")

O/PermissionError

ERROR:root:This is error message
CRITICAL:root:This is critical message

"""


"""
lg.basicConfig(level = lg.CRITICAL)
lg.debug('This is a debug message')
lg.info("This is information message")
lg.warning("This is warning message")
lg.error("This is error message")
lg.critical("This is critical message")

O/P

CRITICAL:root:This is critical message

"""


