! /usr/bin/python3
from PIL import Image

def popup():
	filename = "yum.jpg"
	image = Image.open(filename)
	out = image.resize((1000,600))
	for _ in range(0, 100):
		image.show()
	
def main():
	popup()
	
main()
