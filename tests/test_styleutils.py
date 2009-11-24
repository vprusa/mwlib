#! /usr/bin/env py.test
# -*- coding: utf-8 -*-
# Copyright (c) 2007-2009 PediaPress GmbH
# See README.txt for additional licensing information.


import sys
from mwlib.dummydb import DummyDB
from mwlib.uparser import parseString
from mwlib import parser
from mwlib import advtree
from mwlib.writer import styleutils

def getTreeFromMarkup(raw):
    tree = parseString(title="Test", raw=raw, wikidb=DummyDB())
    advtree.buildAdvancedTree(tree)
    return tree


def show(tree):
    parser.show(sys.stdout, tree)

def test_getTextAlign():
    raw =  '''
{|
|-
! center
! style="text-align:right;"|right
|- style="text-align:left;"
! left
! style="text-align:right;"|right
|}
    '''
    tree = getTreeFromMarkup(raw)
    for cell in tree.getChildNodesByClass(advtree.Cell):
        txt = cell.getAllDisplayText().strip()
        align = styleutils.getTextAlign(cell)
        assert txt == align, 'alignment not correctly parsed'
