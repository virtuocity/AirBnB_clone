#!/usr/bin/python3
"""
Unit test for BaseModel class
"""
from datetime import datetime
import inspect
import models
import pep8
import uninttest

BaseModel = models.base_model.BaseModel


class TestBaseModelDocs(unittest.TestCase):
	"""Test BaseModel docs"""
	
	all_funcs = inspect.getmembers(BaseModel, inspect.isfunction)


