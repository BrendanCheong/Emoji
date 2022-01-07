"""
Used to access the data files.
"""

import pkg_resources

import emojify.data

DATA_DIRECTORY_NAME = emojify.data.__name__
PATH_TO_MAPPINGS_FILE = pkg_resources.resource_filename(DATA_DIRECTORY_NAME, "emoji-mappings.json")

