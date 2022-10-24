# -*- coding: utf-8 -*-
"""detect_Html_tags_attrb.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zN-EHECVjngrp3x2Q5v131QbxfOKYTt_
"""

from html.parser import HTMLParser

class CustomHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print(tag)
        self.handle_attrs(attrs)
    def handle_startendtag(self,tag,attrs):
        print(tag)
        self.handle_attrs(attrs)
    def handle_attrs(self,attrs):
        for attrs_pair in attrs:
            print('->',attrs_pair[0].strip(),'>',attrs_pair[1].strip())        

n = int(input())
html_string = ''
for i in range(n):
    html_string += input()
    
customHTMLParser = CustomHTMLParser()
customHTMLParser.feed(html_string)
customHTMLParser.close()