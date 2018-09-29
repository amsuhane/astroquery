"""
NEOS Query Tool
===============

:Authors:
1) Juan Luis Cano Rodríguez (juanlu001@gmail.com)
2) Antonio Hidalgo (antoniohidalgo.inves@gmail.com)
3) Shreyas Bapat (bapat.shreyas@gmail.com)

This module contains various methods for querying the
NEOWS and DASTCOM5 services.

All of them are coded as part of SOCIS 2017 for poliastro by Antonio Hidalgo.
"""
from astropy import config as _config

class Conf(_config.ConfigNamespace):
    pass

from .core import *

__all__ = []
