#!/usr/bin/python3
"""
This module contains a single class Review inheriting from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    this contains a representation of the class
    """
    place_id = ""
    user_id = ""
    text = ""
