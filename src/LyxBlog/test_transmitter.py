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
from transmitter import Transmitter
from image import Image
from account import Account
from account_manager import AccountManager
from elyxer_entry import ElyxerEntry

class DisplayTestCase(unittest.TestCase):

    def setUp(self):
        self.filename = 'test_files/entry_test'
        self.bogus_account = Account('nonsenseasdfasdf.com', 'barry', 'manilow')
        self.account_with_bad_password = Account('blogtest.letseatalready.com', 'test', 'not_test')
        self.account_with_good_password = Account('blogtest.letseatalready.com', 'test', 'test')
        self.account_with_no_password = Account('blogtest.letseatalready.com', 'test', None)
    def test_publish_image(self):
        Image.set_abs_reference_dir_from_html_file(self.filename)
        account = AccountManager.get_default_account()
        tt = Transmitter()
        tt.set_account(account)
        image = Image("some <img src='Suzanne.jpg' /> string")
        before = image.get_remote_src()
        self.assertEqual(before, None)
        tt.publish_image(image)
        after = image.get_remote_src()
        self.assertNotEqual(after, None)
    def test_check_credentials_bogus(self):
        tt = Transmitter()
        tt.set_account(self.bogus_account)
        self.assertEquals(tt.check_credentials(), 'host not found') 
    def test_check_credentials_bad_password(self):
        tt = Transmitter()
        tt.set_account(self.account_with_bad_password)
        self.assertEquals(tt.check_credentials(), 'username/password error') 
    def test_check_credentials_golden_password(self):
        tt = Transmitter()
        tt.set_account(self.account_with_good_password)
        self.assertEquals(tt.check_credentials(), True) 
    def test_check_credentials_no_password(self):
        tt = Transmitter()
        tt.set_account(self.account_with_no_password)
        self.assertEquals(tt.check_credentials(), True) 
    def test_upload_entry(self):
        tt = Transmitter()
        tt.set_account(self.account_with_good_password)
        filename = 'test_files/entry_test'
        entry = ElyxerEntry()
        entry.set_transmitter(tt)
        entry.load(filename)
        entry.set_title('WoooYAH!')
        tt.publish_entry(entry)

if __name__ == '__main__':
    unittest.main()

