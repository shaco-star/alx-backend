#!/usr/bin/env python3

"""Pagination function"""


def index_range(page, page_size):
    """_summary_

    Args:
        page (int): number of start page
        page_size (int): size of items in each page

    Returns:
        Tuple: size two containing a start index and an end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
