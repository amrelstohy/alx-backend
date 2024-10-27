#!/usr/bin/env python3
"""Simple pagination"""
import csv
import math
from typing import List, Tuple


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

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """Simple helper function"""
        return (page_size * (page - 1), page * page_size)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Simple pagination"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page_size > 0 and page > 0
        range = self.index_range(page, page_size)
        if range[1] > len(self.dataset()):
            return []
        return self.dataset()[range[0]: range[1]]
