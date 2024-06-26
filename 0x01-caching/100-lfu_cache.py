#!/usr/bin/env python3
"""
LFU Caching System Module
"""

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching
    and implements a LFU caching system
    """

    def __init__(self):
        """ Initialize the LFUCache """
        super().__init__()
        self.freq = defaultdict(int)
        self.order = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache
        If the number of items exceeds MAX_ITEMS,
        discard the least frequently used item
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
            self.order.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used items
                min_freq = min(self.freq.values())
                least_frequent_keys = [
                    k for k, v in self.freq.items() if v == min_freq
                ]

                # Among the least frequently used, find the least recently used
                for k in self.order:
                    if k in least_frequent_keys:
                        discard_key = k
                        break

                print(f"DISCARD: {discard_key}")
                del self.cache_data[discard_key]
                del self.freq[discard_key]
                del self.order[discard_key]

            self.cache_data[key] = item
            self.freq[key] = 1
            self.order[key] = None

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.freq[key] += 1
        self.order.move_to_end(key)
        return self.cache_data[key]
