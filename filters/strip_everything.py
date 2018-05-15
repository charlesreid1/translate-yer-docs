#!/usr/bin/env python
from panflute import *
import sys

def translate(english):
    """
    Super advanced machine learning.
    Guaranteed accurate tanslation.
    """
    return english

def translate_document(elem, doc):
    """
    Fake-translate a document
    """
    if type(elem)==Para:

        english = stringify(elem)
        translation = translate(english)
        new_elems = convert_text(translation, input_format='markdown')
        return new_elems

    elif type(elem)==Header:
        english = stringify(elem)
        translation = translate(english)
        h = Header(Str(translation))
        return h

def main(doc=None):
    return run_filter(translate_document, doc=doc)

if __name__=="__main__":
    main()

