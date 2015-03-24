""" Settings for mail_sender """

from .base import *
try:
    from .local import *
except ImportError as exc:
    exc.args = tuple(
        ['%s (did you rename settings/local-dist.py?)' % exc.args[0]])
    raise exc

from .private import *
