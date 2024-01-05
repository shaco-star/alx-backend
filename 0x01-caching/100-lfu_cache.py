#!/usr/bin/python3
""" BaseCaching module
"""

from collections import Counter
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """_summary_

    Args:
        BaseCaching (_type_): _description_
    """
    def __init__(self):
        super().__init__()
        self.order = []
        self.counter = Counter()

    def put(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_freq = min(
                    self.counter.items(),
                    key=lambda x: (x[1], self.order.index(x[0]))
                )
                discarded = least_freq[0]
                del self.cache_data[discarded]
                del self.counter[discarded]
                self.order.remove(discarded)
                print(f"DISCARD: {discarded}")
            self.cache_data[key] = item
            self.counter[key] += 1
        self.order.append(key)

    def get(self, key):
        """_summary_

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        self.counter[key] += 1
        return self.cache_data[key]
