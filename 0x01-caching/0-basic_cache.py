#!/usr/bin/env python3
"""Basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic dictionary"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()

    def put(self, key, item):
        """put method"""
        if key and item:
            self.cache_data.update({key: item})

    def get(self, key):
        """get method"""
        if not key:
            return
        item = self.cache_data.get(key)
        if item:
            return item
