# Given image repesented by NxN matrix with each pixel 4 bytes. Write a method to rotate image by 90 degrees

image = [[],[],[],[]]

for i in range(len(image)):
	for j in range(0,6):
		image[i].append(j+(i*6))

print(image)

def rotate(img):
	rotated = []

	for i in range(len(img[0])): # rows is size of row
		newrow = []
		for row in img:
			newrow.append(row[i])
		rotated.append(newrow)

	return rotated


print(rotate(image))