#!/usr/bin/env python3
"""
Helper Function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes
    """
    return ((page - 1) * page_size, page * page_size)
