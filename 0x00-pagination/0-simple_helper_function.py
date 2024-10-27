#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Simple helper function"""
    return (page_size * (page - 1), page * page_size)
