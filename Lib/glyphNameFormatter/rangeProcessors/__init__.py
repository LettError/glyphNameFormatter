# -*- coding: UTF-8 -*-
# default, final, catchall handler

from _processDiacritics import processDiacritics


def process(self):
    print "default processor"
    self.condense(self.uniName)
    return False


class GlyphNameProcessor(object):

    processDiacritics = processDiacritics