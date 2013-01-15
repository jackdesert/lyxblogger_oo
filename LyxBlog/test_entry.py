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
from elyxer_entry import ElyxerEntry 
from lyxhtml_entry import LyxhtmlEntry 
from transmitter import Transmitter
from entry import TransmitterAlreadyExistsError
from entry import TransmitterNotDefinedError
from entry import TitleAlreadySetError
from account import Account

class EntryTestCase(unittest.TestCase):

    def setUp(self):
        self.filename = '../test_samples/original.elyxer_html'
    def test_get_num_words(self):
        aa = ElyxerEntry()
        aa._Entry__body = '<b> </b> three more lines'
        self.assertEqual(aa.get_num_words(), 3)

    def test_get_num_images(self):
        aa = ElyxerEntry()
        self.assertEqual(aa.get_num_images(), 0)
        aa.load(self.filename)
        self.assertEqual(aa.get_num_images(), 1)

    def test_get_title(self):
        aa = ElyxerEntry()
        self.assertEqual(aa.get_title(), None)
        aa.load(self.filename)
        self.assertEqual(aa.get_title(), 'Tutorial de LyX')
        self.assertRaises(TitleAlreadySetError, lambda: aa.set_title('Second Title'))


    def test_load(self):
        aa = ElyxerEntry()
        aa.load(self.filename)
        self.assertTrue('Tutorial de LyX' in aa.get_body())
    def test_get_wordcount(self):
        aa = ElyxerEntry()
        aa.load(self.filename)
        returned = aa.get_num_words()
        self.assertTrue(isinstance(returned, int))
    def test_replace_special_characters(self):
        aa = ElyxerEntry()
        body = "&lt;code&gt;   SOME CODE   &lt;/code&gt;"
        body +="Footnotes:  [→    →] "
        aa._Entry__body = body
        aa._Entry__replace_special_characters()
        self.assertTrue('<code>' in aa.get_body())
        self.assertTrue('</code>' in aa.get_body())
        self.assertTrue('→' not in aa.get_body())
    def test_set_transmitter_exactly_once(self):
        tt = Transmitter()
        url = 'whee.com'
        username = 'boyhowdy'
        account = Account(url, username, None)
        tt.set_account(account)
        aa = ElyxerEntry()
        aa.set_transmitter(tt)
        self.assertRaises(TransmitterAlreadyExistsError, lambda: aa.set_transmitter(tt))
    def test_publish(self):
        aa = ElyxerEntry()
        self.assertRaises(TransmitterNotDefinedError, lambda: aa.publish())


if __name__ == '__main__':
    unittest.main()

