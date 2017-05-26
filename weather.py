#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
import time
import lxml
import sys

def weather(lat1, lon1):
	print("[+] Fetching the Weather Report\n")
	r = requests.get('http://w1.weather.gov/xml/current_obs/index.xml')
	soup = BeautifulSoup(r.text, "lxml")
	over = soup.findAll('station')
	for j in over:
		if j.find('latitude').string == lat1 and j.find('longitude').string == lon1:
			a=j.find('xml_url').string		
	r1= requests.get(a)
	soup1 = BeautifulSoup(r1.text, "html.parser")
	print("[+]The Location is: "+soup1.find("location").string)
	print("[+]Last Fetched at: "+soup1.find("observation_time").string)
	print("[+]The Temperature is: "+soup1.find("temperature_string").string)
	print("[+]The Wind is: "+soup1.find("wind_string").string)
	print("[+]The Dew is: "+soup1.find("dewpoint_string").string)

def main():
	choice()
	
def choice():
	lat=raw_input("Enter the Latitude (Exact) : ")
	lon=raw_input("Enter the Longitude (Exact) : ")
	print "The Latitude is "+lat+" and the Longitude is "+lon
	print ""
	print("[+] Do you want to Fetch Data now (y/n)")
	x = raw_input()
	if x=="y":
		weather(lat, lon)
	else:
		print "[-] Ok Bye"

if __name__=="__main__":
	main()
