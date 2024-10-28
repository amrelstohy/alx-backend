#!/usr/bin/env python3
"""Hypermedia pagination"""
import csv
import math
from typing import List, Tuple, Dict, Any


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Hypermedia pagination"""
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        if page >= total_pages:
            next_page = None
        else:
            next_page = page + 1

        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1

        return {
                'page_size': len(data),
                'page': page, 'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }
