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
import sys
from account import Account
from account_manager import AccountManager
from account_manager import SystemNotFoundError

class AccountManagerTestCase(unittest.TestCase):

    def test_initialization(self):
        a = AccountManager()
        path = a._AccountManager__configpath
        self.assertTrue(path.endswith(".lyxblogger/config.cfg"))
    def test_system_not_found_error(self):
        saved_platform = sys.platform
        sys.platform = 'spiderman'
        self.assertRaises(SystemNotFoundError, AccountManager)
        sys.platform = saved_platform
    def test_add_new_account(self):
        aa = AccountManager()
        aa.reset_config()
        url = 'http://myblog.com'
        username = 'charles'
        password = 'not telling'
        new_account = Account(url, username, password)
        aa.add_new_account(new_account)
        accounts = aa._AccountManager__accounts
        self.assertEquals(accounts[0], Account(url, username, password))
        self.assertEqual(len(accounts), 1)
    def test_retrieving_account_with_None_password(self):
        aa = AccountManager()
        aa.reset_config()
        url = 'aa.com'
        username = 'my_account'
        password = None
        new_account = Account(url, username, password)
        aa.add_new_account(new_account)
        aa_retrieved = aa.get_account_by_id(1)
        self.assertEqual(aa_retrieved.get_url(), 'aa.com')
        self.assertEqual(aa_retrieved.get_password(), None)
        bb = AccountManager()   # new instance, pulled from config file
        bb_retrieved = bb.get_account_by_id(1)
        self.assertEqual(bb_retrieved.get_url(), 'aa.com')
        self.assertEqual(bb_retrieved.get_password(), None)



    def test_add_new_account_to_config(self):
        # '__add_new_account_to_config' must throw an exception if it is fed an account
        # that does not have a section_id
        url = 'bb.com'
        username = 'yesman'
        password = None
        new_account = Account(url, username, password)
        aa = AccountManager()
        self.assertRaises(TypeError, lambda: aa._AccountManager__add_account_to_config(new_account))
    def test_save_accounts_to_file(self):
        aa = AccountManager()
        aa.reset_config()
        self.assertEqual(len(aa.get_accounts()), 1)
        url = 'http://cheeky.com'
        username = 'mgh'
        password = 'no fair yelling'
        new_account = Account(url, username, password)
        aa.add_new_account(new_account)
        self.assertEqual(len(aa.get_accounts()), 2)
        bb = AccountManager()
        aa_account = aa.get_accounts()[0]
        bb_account = bb.get_accounts()[0]
        self.assertEquals(aa_account, bb_account)
    def test_default_account(self):
        aa = AccountManager()
        aa.reset_config()
        expected = AccountManager.get_default_account() 
        self.assertEqual(aa.get_recent_account(), expected)
    def test_get_account_by_id(self): 
        aa = AccountManager()
        aa.reset_config()
        url = 'hi.com'
        username = 'babyblue'
        password = None
        new_account = Account(url, username, password)
        aa.add_new_account(new_account)
        self.assertEqual(AccountManager.get_default_account(), aa.get_account_by_id(0))
        self.assertEqual(new_account, aa.get_account_by_id(1))
    def test_recent_account(self): 
        aa = AccountManager()
        aa.reset_config()
        url = 'hi.com'
        username = 'babyblue'
        password = None
        new_account = Account(url, username, password)
        aa.add_new_account(new_account)
        self.assertEqual(new_account, aa.get_account_by_id(1))
        self.assertEqual(new_account, aa.get_recent_account())
        self.assertEqual(AccountManager.get_default_account(), aa.get_account_by_id(0))
        self.assertEqual(AccountManager.get_default_account(), aa.get_recent_account())
        

if __name__ == '__main__':
    unittest.main()

