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
import re, pdb
from entry import Entry

class LyxhtmlEntry(Entry):

    def __init__(self):
        return

    def _create_image_regex(self):
        # INTERNAL img tags look something like this:
        # <img src='0_home_jd_Escritorio_rv-8_tiny.jpg' alt='image: 0_home_jd_Escritorio_rv-8_tiny.jpg' />
        # Notice LYXHTML uses single quotes within the tag.
        regex = re.compile('''
            <img\ src='     # The beginning of an <img> tag -- note the escaped space
            .+?             # Non-greedy match of the rest of the stuff in the middle
            />              # The closing of the <img> tag
            ''', re.VERBOSE)
        return regex

