import urllib.request
import sys

# url = 'https://shop.lego.com/en-CZ/LEGO-NASA-Apollo-Saturn-V-21309'

def check_availability(url):
	response = urllib.request.urlopen(url)
	data = response.read().decode('utf-8')
	if data.find("available--now") != -1:
		return True
	else:
		return False 

if __name__ == "__main__":
	if check_availability(sys.argv[1]):
		sys.exit(0)
	else:
		sys.exit(1)