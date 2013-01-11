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
class Entry:
    __metaclass__ = ABCMeta

    def __init__(self, transmitter):
        self.__transmitter = transmitter
        self.__wordcount = 0
        self.__title = '*ucking amazing title'
        self.__body = ''
        self.__images = []
        self.__image_regex = self._create_image_regex()
       
    def __eq__(self, other):
        return self.__wordcount == other._Entry__wordcount

    def get_body(self):
        return self.__body

    def get_num_words(self):
        return self.__wordcount

    def get_title(self):
        return self.__title

    def get_num_images(self):
        return len(self.__images)
    
    def load(self, filename):
        self.__body = self.__read_contents(filename)
        self.__extract_images_from_body()

    def publish(self):
        self.__publish_images()
        self.__substitute_remote_image_urls_into_body()
        self.__transmitter.publish_entry(self)

    def __substitute_remote_image_urls_into_body(self):
        for image in self.__images:
            self.__body = self.__body.replace(image.get_local_html(), image.get_remote_html())
        
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
    


    def __add_image(self, image):
        self.__images.append(image)
            
        
    # Note that I'm using a single leading underscore for abstract methods 
    # since subclasses cannot see methods with double leading underscores
    @abstractmethod
    def _create_image_regex(self):
        pass 
