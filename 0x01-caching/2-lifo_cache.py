#!/usr/bin/python3
""" LIFO cache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO  Class
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        last_keyItem = ""

    def put(self, key, item):
        """ add an item to cache using LIFO (Max items 4) """
        if key is None or item is None:
            return

        if key not in self.cache_data.keys():
            if (len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS):
                if self.last_keyItem != "":
                    print("DISCARD: " + self.last_keyItem)
                    self.cache_data.pop(self.last_keyItem)
                else:
                    self.last_keyItem = list(self.cache_data.keys())[-1]

        self.cache_data[key] = item
        self.last_keyItem = key

    def get(self, key):
        """ retrieve an item with given key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
