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

import pdb
import xmlrpclib, socket, wordpresslib

class Transmitter:

    NONSENSE = 'gobbledygook'

    def __init__(self):
        self.__account = None
        self.__connection = None

    def publish_image(self, image):
        remote_src = self.__connection.newMediaObject(image.get_local_absolute_src())
        image.set_remote_src(remote_src)

    def set_account(self, account):
        self.__account = account
        self.__set_connection()

    def __set_connection(self):
        self.__connection = wordpresslib.WordPressClient(
            self.__account.get_full_url(), 
            self.__account.get_username(), 
            self.__account.get_password())

    def refresh_connection_with_account_details(self):
        self.__set_connection()

        
    def select_post_id(self):
        post_id = 0
        self.__connection.selectBlog(post_id)

    def publish_entry(self, entry):
        categories = [1]
        self.select_post_id()
        post = wordpresslib.WordPressPost()
        post.title = entry.get_title()
        post.categories = categories
        post.description = entry.get_body()
        if not post.title: raise IncompleteEntryError('title')
        if not post.categories: raise IncompleteEntryError('categories')
        if not post.description: raise IncompleteEntryError('description')
        try:
            self.__connection.newPost(post, True)
            return True
        except (socket.gaierror, wordpresslib.WordPressException):
            msg = traceback.format_exc()
            if ('[Errno -2] Name or service not known' in msg):
                return 'connection error'
            elif ('Bad login/pass combination' in msg):
                return 'username/password error'




    def check_credentials(self):
        rpc_server = xmlrpclib.ServerProxy(self.__account.get_full_url())
        password = self.__account.get_password()
        if not password: password = Transmitter.NONSENSE
        try:
            print 'about to check credentials, password={}'.format(password)
            rpc_server.blogger.getUserInfo('', self.__account.get_username(), password)
            print 'back after checking'
            return True
        except socket.gaierror:    # gaierror caught if no connection to host
            print 'back after checking'
            return 'host not found'
        except xmlrpclib.Fault:    # xmlFault caught if host found but user/pass mismatch
            print 'back after checking'
            if self.__account.get_password() == None:
                # Don't bother checking password if none given
                return True
            else:
                return 'username/password error'
        except xmlrpclib.ProtocolError:
            # Usually this just means try again--not your fault
            print 'back after checking'
            return 'protocol error'


            
class IncompleteEntryError(Exception):
    def __init__(self, missing_piece):
        self.msg = 'Entry must have a {0} before transmitter can publish'.format(missing_piece) 
