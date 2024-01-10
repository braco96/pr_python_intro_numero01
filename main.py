# -*- coding: utf-8 -*-
import re
def describe_value(v):
    """Devuelve (tipo, verdad, representacion)."""
    t = type(v).__name__
    truth = bool(v)
    return t, truth, str(v)

