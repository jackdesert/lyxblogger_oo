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

    def __init__(self):
        self.__account = None
        self.__connection = None

    def publish_image(self, image):
        src = 'http://somesite.com/somepath.jpg'
        image.set_remote_src(src)

    def load_account(self, account):
        self.__account = account
        self.__connection = wordpresslib.WordPressClient(account.get_full_url(), account.get_username(), account.get_password())

        
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
        if password == None: password = ''
        try:
            rpc_server.blogger.getUserInfo('', self.__account.get_username(), password)
            return True
        except socket.gaierror:    # gaierror caught if no connection to host
            return 'host not found'
        except xmlrpclib.Fault:    # xmlFault caught if host found but user/pass mismatch
            if self.__account.get_password() == None:
                # Don't bother checking password if none given
                return True
            else:
                return 'username/password error'
        except xmlrpclib.ProtocolError:
            # Usually this just means try again--not your fault
            return 'protocol error'


            
            
