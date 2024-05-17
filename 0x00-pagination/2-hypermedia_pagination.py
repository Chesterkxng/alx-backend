#!/usr/bin/env python3
"""
SIMPLE PAGINATION
"""

import csv
import math
from typing import List, Tuple, Dict, Union


def index_range(page: int, page_size: int) -> Tuple:
    """
    return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes
    """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        paginate the dataset correctly and return the appropriate page
        of the dataset (i.e. the correct list of rows).
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        idx_range: Tuple = index_range(page, page_size)

        return self.dataset()[idx_range[0]:idx_range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns a dictionary containing the following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        data: List = self.get_page(page, page_size)
        total_pages: int = math.ceil(len(self.dataset()) / page_size)

        """ check if the prev page exists """
        prev_page: Union[int, None] = None
        if (page > 1):
            prev_page = page - 1

        """ check if the next page exists """
        next_page: Union[int, None] = None
        if (len(self.get_page(page + 1, page_size))):
            next_page = page + 1

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
            }
