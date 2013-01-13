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

import unittest, sys
import pexpect
from lyxblogger import LyXBlogger

class LyxbloggerTestCase(unittest.TestCase):

    def setUp(self):
        self.filename = '../../test_samples/original.elyxer_html' 
    def test_initialize(self):
        aa = LyXBlogger(self.filename)
    def test_basic_runthrough(self):
        child = pexpect.spawn('python lyxblogger.py {0}'.format(self.filename))
        child.logfile = sys.stdout
        child.expect('Delete')
        child.sendline('0')
        child.expect('Salvation')

if __name__ == '__main__':
    unittest.main()

