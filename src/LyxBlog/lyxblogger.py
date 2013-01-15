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

import re, sys, pdb
from display import Display
from account import Account
from account_manager import AccountManager
from transmitter import Transmitter
from elyxer_entry import ElyxerEntry

class LyXBlogger:

    VERSION = '0.43'
    def __init__(self, input_file, display = None):
        self.__display = display or Display()
        self.__state = 0
        self.__entry = None
        self.__manager = AccountManager()
        self.__input_file = input_file

    def start(self):
        self.__welcome()
        self.__entry = ElyxerEntry()
        self.__entry.load(self.__input_file)
        self.__ensure_title()
        self.__display_summary()
        account = self.__verify_which_account()
        self.__ensure_password(account)
        transmitter = self.__manager.pass_transmitter()
        self.__entry.set_transmitter(transmitter)
        self.__verify_create_new_or_overwrite()
        self.__entry.publish()
        self.__closing_remarks()

    def __verify_which_account(self):
        dd = self.__display
        mm = self.__manager
        recent_id = mm.get_recent_id()
        while(1):
            accounts = mm.get_accounts()
            response_with_case = dd.ask_which_account(accounts, recent_id)
            response = response_with_case.lower()
            if response == 'd':
                account_id = dd.ask_which_account(accounts, True)
                mm.delete_account_by_id(int(account_id))
            elif response == 'n':
                username = dd.ask_for_new_username()
                url = dd.ask_for_new_url()
                password = dd.ask_for_new_password()
                new_account = Account(url, username, password)
                mm.add_new_account(new_account)
            elif response == '':
                return mm.get_recent_account()
            elif re.compile('^\d+$').match(response):
                account_id = int(response)
                return mm.get_account_by_id(account_id)
            else:
                dd.print_unrecognized_response(response_with_case)


    def __ensure_title(self):
        if not self.__entry.get_title():
            title = self.__display.ask_for_title()
            self.__entry.set_title(title)
        
    def __ensure_password(self, account):
        if not account.get_password():
            temp = self.__display.ask_for_temp_password(account)
            account.set_temp_password(temp)

    def __verify_create_new_or_overwrite(self):
        pass

    def __welcome(self):
        self.__display.welcome(LyXBlogger.VERSION)

    def __closing_remarks(self):
        self.__display.print_done()

    def __display_summary(self):
        self.__display.print_entry_summary(self.__entry)



if __name__ == '__main__':
    try:
        input_file = sys.argv[1]    # Incoming file name
        lyxblogger = LyXBlogger(input_file)
        lyxblogger.start()
    except IndexError:
        handle_input_error()
    except SystemExit:
        pass    # Let this exception pass through so sys.exit() calls will work
    #except:
        #pass
        #handle_general_error()


