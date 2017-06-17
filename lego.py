import urllib.request
import sys

# url = 'https://shop.lego.com/en-CZ/LEGO-NASA-Apollo-Saturn-V-21309'

def check_aviability(url):
	response = urllib.request.urlopen(url)
	data = response.read().decode('utf-8')

	if data.find("available--now"):
		return True
	else:
		return False 


if __name__ == "__main__":
	check_aviability(sys.argv[1])