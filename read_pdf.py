from operator import itemgetter
from itertools import groupby
from SortedCollection import SortedCollection
import fitz
import re

def read_pdf(file_name: str):
    doc = fitz.open( f"{regex(file_name)}.pdf" )
    pages = [ doc[i] for i in range( doc.pageCount ) ]
    text= """"""

    for page in pages:
        text_words = page.get_text_words()

        # The words should be ordered by y1 and x0
        sorted_words = SortedCollection(key = itemgetter( 3, 0 ) )

        for word in text_words:
            sorted_words.insert(word)

        # At this point you already have an ordered list. If you need to 
        # group the content by lines, use groupby with y1 as a key
        lines = groupby( sorted_words, key = itemgetter( 3 ) )
        for key, group in lines:
            for tupl in group:
                text += tupl[4] + " "
    return text


def regex(input: str):
    match = re.search(r'([\w]+\.)+[\w]+(?=[\s]|$)', input)
    return match.group()