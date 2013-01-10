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

import pdb, re

class Image:

    def __init__(self, local_html):
        self.__local_html = local_html
        self.__local_src = self.__parse_local_src()
        self.__remote_src = None


    def get_local_html(self):
        return self.__local_html
 
    def set_remote_src(self, src):
        self.__remote_src = src

    def get_remote_src(self):
        return self.__remote_src

    def __parse_local_src(self):
        # Note that we are looking for either a single or double quote in the regex. 
        # This is because eLyXer uses one type, LyXHTML uses the other
        # Note the group in the middle is non-greedy
        regex = re.compile('''src=["'](.+?)["']''')
        return regex.search(self.__local_html).group(1)

    def get_remote_html(self):
        return self.get_local_html().replace(self.__local_src, self.__remote_src)

 
