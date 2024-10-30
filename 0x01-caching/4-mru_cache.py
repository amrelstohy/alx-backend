#!/usr/bin/env python3
"""MRU caching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU caching class"""

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
            MRU_item = list(self.cache_data.keys())[self.MAX_ITEMS - 1]
            del self.cache_data[MRU_item]
            print(f"DISCARD: {MRU_item}")
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
            del self.cache_data[key]
            self.cache_data.update({key: item})
            return item
