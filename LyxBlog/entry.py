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
import abc
from abc import ABCMeta, abstractmethod
from image import Image
from transmitter import Transmitter

class Entry:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.__transmitter = None
        self.__title = None
        self.__body = ''
        self.__images = []
        self.__image_regex = self._create_image_regex()
       
    def __eq__(self, other):
        return self.__wordcount == other._Entry__wordcount

    def get_body(self):
        return self.__body

    def get_title(self):
        return self.__title

    def set_title(self, title):
        if self.__title: raise TitleAlreadySetError()
        self.__title = title

    def get_num_words(self):
        text_no_tags = re.sub('<.*?>', '', self.__body)
        word_list = text_no_tags.split()
        return len(word_list)

    def get_num_images(self):
        return len(self.__images)
    
    def load(self, filename):
        self.__body = self.__read_contents(filename)
        Image.set_abs_reference_dir_from_html_file(filename)
        self.__massage_body()
        self.__extract_images_from_body()

    def publish(self):
        if not self.__transmitter: raise TransmitterNotDefinedError()
        self.__publish_images()
        self.__substitute_remote_image_urls_into_body()
        self.__transmitter.publish_entry(self)

    def set_transmitter(self, transmitter):
        if self.__transmitter: raise TransmitterAlreadyExistsError()
        transmitter.refresh_connection_with_account_details()
        self.__transmitter = transmitter

    def __massage_body(self):
        self.__extract_title_from_header()
        self.__trim_body_excess()
        self.__remove_title_from_body()
        self.__replace_special_characters()

    def __trim_body_excess(self):
        search_obj = re.search('<body>(.+)</body>', self.__body)
        if search_obj:
            self.__body = search_obj.group(1)

    def __extract_title_from_header(self):
        search_obj = re.search('<title>(.+?)</title>', self.__body)
        if search_obj:
            self.set_title(search_obj.group(1))

    def __remove_title_from_body(self):
        # REMOVING TITLE FROM BODY
        # Typical body title using ENGINE_INTERNAL:
        #   <h1 class="title"><a id='magicparlabel-309' />
        #   Example Article Title</h1>
        #   <h1 class="title">
        # Typical body title using ELYXER_ENGINE using optional sizing:
        #   <h1 class="title">
        #   <span class="footnotesize">Hi Brian</span>
        #
        #   </h1>
        # Note we are using a non-greedy .*?
        search_obj = re.search('''<h1 class="title".*?</h1>''', self.__body)
        if(search_obj):
            self.__replace_in_body(search_obj.group(), '')

    def __replace_special_characters(self):
        # Reinvoke <code> and </code> tags from their escape sequence counterparts
        self.__replace_in_body('&lt;code&gt;', '<code>')
        self.__replace_in_body('&lt;/code&gt;', '</code>')

        # Remove Arrows from footnotes and margin notes
        self.__replace_in_body('[→', '[')
        self.__replace_in_body('→]', ']')

    def __substitute_remote_image_urls_into_body(self):
        for image in self.__images:
            self.__replace_in_body(image.get_local_html(), image.get_remote_html())
        
    def __read_contents(self, filename):
        f = open(filename, 'r')
        contents = f.read()
        f.close
        return contents

    def __extract_images_from_body(self):
        local_image_links = self.__image_regex.findall(self.__body)
        for local_link in local_image_links:
            image = Image(local_link)
            self.__add_image(image)

    def __publish_images(self):
        for image in self.__images:
            self.__transmitter.publish_image(image)
    
    def __replace_in_body(self, old, new):
        self.__body = self.__body.replace(old, new)

    def __add_image(self, image):
        self.__images.append(image)
            
        
    # A B S T R A C T    M E T H O D S 
    # Note that I'm using a single leading underscore for abstract methods 
    # since subclasses cannot see methods with double leading underscores
    @abstractmethod
    def _create_image_regex(self):
        pass 


class TransmitterAlreadyExistsError(Exception):
    def __init__(self):
        self.msg = 'Transmitter can only be set once'
class  TransmitterNotDefinedError(Exception):
    def __init__(self):
        self.msg = 'Must call Entry#set_transmitter before publishing'
class TitleAlreadySetError(Exception):
    def __init__(self):
        self.msg = 'Title has already been set'
