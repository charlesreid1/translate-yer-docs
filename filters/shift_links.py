#!/usr/bin/env python
from panflute import *
import sys

def translate(english):
    """
    Super advanced machine learning.
    Guaranteed accurate tanslation.
    """
    return english


def strip_links(elem,doc):
    """
    Each link will be stripped in the translation process.
    Save them for the end.
    """
    if isinstance(elem,Link):
        doc.linklist.append(Para(elem))


##############################
#  Pandoc functions


def prepare(doc):
    doc.linklist = []


def translate_document(elem, doc):
    """
    Fake-translate a document
    """
    if type(elem)==Para:

        # Walk it and look for links first
        doc.linklist = []
        elem.walk(strip_links)

        english = stringify(elem)
        translation = translate(english)
        new_elems = convert_text(translation, input_format='markdown')

        return new_elems + doc.linklist

    elif type(elem)==Header:
        english = stringify(elem)
        translation = translate(english)
        h = Header(Str(translation))
        return h


def finalize(doc):
    pass



#########################
# Apply pandoc functions


def main(doc=None):
    return run_filter(translate_document, prepare, finalize, doc=doc)

if __name__=="__main__":
    main()


