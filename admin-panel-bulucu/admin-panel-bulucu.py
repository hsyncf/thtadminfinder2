#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("link.txt","r");
	link = raw_input("Site linki giriniz \n(örnek: www.örnek.com ): ")
	print "\n\nUygun linkler : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "Bulundu => ",req_link

def Credit():
	Space(9); print "#####################################"
	Space(9); print "#   +++   Admin Panel Bulucu   +++  #"
	Space(9); print "#    Kodlayıcı: Illûmïnåté Ðëmøñ    #"
	Space(9); print "#   Çeviren ve geliştiren Nighty    #"
	Space(9); print "#      Turk Hack Team version       #"
	Space(9); print "#####################################"

Credit()
findAdmin()
