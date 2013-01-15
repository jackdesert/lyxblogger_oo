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

import sys
import unittest
import pdb
from image import Image
from image import ReferenceDirError

class ImageTestCase(unittest.TestCase):
    
    def setUp(self):
        self.image_tag = "<img src='hi' />"
    def test_initialize(self):
        aa = Image(self.image_tag)
        self.assertEqual(aa.get_local_html(), self.image_tag)
    def test_set_remote_src(self):
        remote = 'http://something'
        aa = Image(self.image_tag)
        aa.set_remote_src(remote)
        self.assertEqual(aa.get_remote_src(), remote)
    def test_generate_remote_html(self):
        aa = Image(self.image_tag)
        aa.set_remote_src('there')
        expected = "<img src='there' />"
        self.assertEqual(expected, aa.get_remote_html())
    def test_get_local_abs_path(self):
        aa = Image(self.image_tag)
        self.assertRaises(ReferenceDirError, lambda: aa.get_local_absolute_src())
        Image.set_abs_reference_dir_from_html_file('some_file.html')
        self.assertTrue('hi' in aa.get_local_absolute_src())


if __name__ == '__main__':
    unittest.main()

