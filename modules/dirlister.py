#-*- coding:utf-8 -*-

import os

def run(**arg):

	print "[*] In dirlister modules."
	files = os.listdir(".")

	return str(files)