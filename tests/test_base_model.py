#!/usr/bin/python3
"""
Test for base model
Run with python3 -m unittest -v tests/test_base_model.py
"""
import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime



class TestBaseModel(unittest.TestCase):
    """
    """

    def test_init(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        with self.assertRaises(TypeError):
            BaseModel(23)
        BaseModel.id