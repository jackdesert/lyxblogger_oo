#! /usr/bin/env python
# -*- coding: utf-8 -*-
#####################       A U T H O R       ##########################
#                                                                      #
#   Copyright 2010 Jack Desert                                         #
#   <jackdesert556@gmail.com>                                          #
#   <http://www.LetsEATalready.com>                                    #
#                                                                      #
######################      L I C E N S E     ##########################
#                                                                      #
#   This file is part of LyXBlogger.                                   #
#                                                                      #
#   LyXBlogger is free software: you can redistribute it and/or modify #
#   it under the terms of the GNU General Public License as published  #
#   by the Free Software Foundation, either version 3 of the License,  #
#   or (at your option) any later version.                             #
#                                                                      #
#   LyXBlogger is distributed in the hope that it will be useful,      #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of     #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the      #
#   GNU General Public License for more details.                       #
#                                                                      #
#   You should have received a copy of the GNU General Public License  #
#   along with LyXBlogger.  If not, see <http://www.gnu.org/licenses>. #
#                                                                      #
########################################################################

# Code to test image.py

import unittest
import pdb
from entry import Entry 

class EntryTestCase(unittest.TestCase):

    def setUp(self):
        self.filename = 'test_files/entry_test'
        f = open(self.filename, 'w')
        self.contents = "nothing to see here"
        f.write(self.contents)
        f.close()
    def test_get_num_words(self):
        aa = Entry()
        self.assertEqual(aa.get_num_words(), 0)

    def test_get_num_images(self):
        aa = Entry()
        self.assertEqual(aa.get_num_images(), 0)

    def test_get_title(self):
        aa = Entry()
        self.assertEqual(aa.get_title(), '')

    def test_load(self):
        aa = Entry()
        aa.load(self.filename)
        self.assertEqual(aa.get_body(), self.contents)

if __name__ == '__main__':
    unittest.main()

