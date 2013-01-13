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
from display import Display
from account import Account
from jabber import Jabber
from image import Image
from elyxer_entry import ElyxerEntry

class DisplayTestCase(unittest.TestCase):

    def setUp(self):
        self.display = Display()
    def test_print_entry_summary(self):
        entry = ElyxerEntry()
        entry._Entry__images = [Image("<img src='photo.jpg' />")]
        entry._Entry__title = 'my title'
        entry._Entry__body = 'fine, fine day'
        returned = self.display.print_entry_summary(entry)
        expected = "You are about to publish:\n\n    my title\n      3 words\n      1 image\n"
        print '**************************************************************'
        print returned
        print expected
        self.assertEqual(returned, expected)
    def test_ask_for_new_password_with_jabber(self):
        jabber = Jabber(['test'])
        new_display = Display(jabber)
        expected = new_display.ask_for_new_password()
        self.assertEqual(expected, "test")
    def test_ask_for_temp_password_with_jabber(self):
        jabber = Jabber(['a temporary password'])
        new_display = Display(jabber)
        account = Account('hi', 'there', None)
        expected = new_display.ask_for_temp_password(account)
        self.assertEqual(expected, "a temporary password")
    def test_ask_for_new_username_with_jabber(self):
        jabber = Jabber(['microgasm'])
        new_display = Display(jabber)
        expected = new_display.ask_for_new_username()
        self.assertEqual(expected, 'microgasm')
    def test_ask_which_account_with_jabber(self):
        jabber = Jabber(['1300'])
        new_display = Display(jabber)
        account = Account('url', 'username', 'password')
        expected = new_display.ask_which_account([account], 17)
        self.assertEqual(expected, '1300')
    def test_ask_for_title_with_jabber(self):
        jabber = Jabber(['Love Conquers All'])
        new_display = Display(jabber)
        expected = new_display.ask_for_title()
        self.assertEqual(expected, 'Love Conquers All')
    def test_ask_for_new_url_with_jabber(self):
        jabber = Jabber(['whee.com'])
        new_display = Display(jabber)
        expected = new_display.ask_for_new_url()
        self.assertEqual(expected, 'whee.com')
    def test_print_accounts(self):
        account = Account('url', 'username', 'password')
        account.set_section_id(1)
        expected = "ACCOUNTS\nEnter the number next to the desired account.\n(**latest) N = New, D = Delete\n1. username@url  **"
        result = self.display._Display__print_accounts([account], 1, False)
        self.assertEqual(result, expected)
    def test_welcome(self):
        self.assertEqual(self.display.welcome('33'), 'LyXBlogger 33')
        


if __name__ == '__main__':
    unittest.main()

