# -*- coding: utf-8 -*-
"""Task1.1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13Q1JnagY6W_nqie-uxnpBZxw3DEpt1Zd
"""

import csv
import inspect
from platform import system as system_name
from subprocess import run, PIPE
from concurrent.futures import ThreadPoolExecutor
import re


stdout_incorrect_warning = """
The message is different from the one specified in the task.
Should be: {}
And output: {}
"""


def check_attribute_or_method(obj, attribute=None, method=None):
    if attribute:
        assert getattribute(obj, attribute, None) != None, "Variable not found"
        assert not inspect.ismethod(
            getattribute(obj, attribute)
        ), f"{attribute} must be a variable, not a method"
    if method:
        assert getattribute(obj, method, None) != None, "Method not found"
        assert inspect.ismethod(
            getattribute(obj, method)
        ), f"{method} must be a method, not a variable"