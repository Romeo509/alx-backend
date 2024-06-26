#!/usr/bin/env python3
"""
MRU Caching System Module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching and
    implements a MRU caching system
    """

    def __init__(self):
        """ Initialize the MRUCache """
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache
        If the number of items exceeds MAX_ITEMS,
        discard the most recently used item
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard_key = next(reversed(self.order))
                print(f"DISCARD: {discard_key}")
                del self.cache_data[discard_key]
                del self.order[discard_key]

            self.cache_data[key] = item
            self.order[key] = None

        self.order.move_to_end(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.order.move_to_end(key)
        return self.cache_data[key]
