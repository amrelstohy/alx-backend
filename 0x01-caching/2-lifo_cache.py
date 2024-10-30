#!/usr/bin/env python3
"""LIFO caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching class"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()

    def put(self, key, item):
        """put method"""

        if not (key and item):
            return

        if (
            len(self.cache_data) == self.MAX_ITEMS
            and key not in self.cache_data
        ):
            first_item = list(self.cache_data.keys())[3]
            del self.cache_data[first_item]
            print(f"DISCARD: {first_item}")
            self.cache_data.update({key: item})
        else:
            if key in self.cache_data:
                del self.cache_data[key]
            self.cache_data.update({key: item})

    def get(self, key):
        """get method"""
        if not key:
            return
        item = self.cache_data.get(key)
        if item:
            return item
