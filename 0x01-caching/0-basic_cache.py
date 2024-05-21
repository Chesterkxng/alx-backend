#!/usr/bin/python3
""" Basic cache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache Class
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ add an item to cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ retrieve an item with given key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
