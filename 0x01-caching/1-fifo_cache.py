#!/usr/bin/python3
""" FIFO cache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    BasicCache Class
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ add an item to cache using FIFO (Max items 4) """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        first_keyItem = list(self.cache_data.keys())[0]
        if (len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS):
            print("DISCARD: " + first_keyItem)
            self.cache_data.pop(first_keyItem)

    def get(self, key):
        """ retrieve an item with given key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
