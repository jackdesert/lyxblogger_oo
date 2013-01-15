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
import getpass
from jabber import Jabber

class JabberTestCase(unittest.TestCase):

    def test_initialization(self):
        queue = ['hi', 'there', 'joe']
        jabber = Jabber(queue)
        loaded_queue = jabber._Jabber__queue
        self.assertTrue(isinstance(loaded_queue, list))
    def test_readline(self):
        queue = ['hi', 'there', 'joe']
        jabber = Jabber(queue)
        self.assertEqual(jabber.readline(), 'hi')
        self.assertEqual(jabber.readline(), 'there')
        self.assertEqual(jabber.readline(), 'joe')
        self.assertEqual(jabber.readline(), None)
    def test_interrupts_stdio(self):
        queue = ['hi', 'there', 'joe']
        jabber = Jabber(queue)
        self.assertEqual(raw_input(), 'hi')
        self.assertEqual(getpass.getpass(), 'there')

if __name__ == '__main__':
    unittest.main()

