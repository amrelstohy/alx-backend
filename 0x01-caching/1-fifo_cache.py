#!/usr/bin/env python3
"""FIFO caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching class"""

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
            first_item = list(self.cache_data.keys())[0]
            del self.cache_data[first_item]
            print(f"DISCARD: {first_item}")
            self.cache_data[key] = item
        else:
            self.cache_data[key] = item
