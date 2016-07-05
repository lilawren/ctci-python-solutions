import copy

image = [[],[],[],[]]

for i in range(len(image)):
	for j in range(0,6):
		image[i].append(j+(i*6))

def zeroes(img):

	print(img)

	firstRowZero = False
	firstColZero = False

	#check first row and col
	for c in img[0]:
		if c == 0:
			firstRowZero = True
	for r in img:
		if r[0] == 0:
			firstColZero = True

	for row in range(1, len(img)):
		for val in range(1, len(img[row])):
			if img[row][val] == 0:
				#set whole row and col to 0
				img[0][val] = 0
				img[row][0] = 0

	for i in range(1,len(img)):
		if img[i][0] == 0:
			zeroRow(img, i)

	for j in range(1, len(img[0])):
		if img[0][j] == 0:
			zeroCol(img, j)

	if firstRowZero:
		zeroRow(img,0)

	if firstColZero:
		zeroCol(img, 0)

	return img

def zeroRow(img, row):
	for k in range(len(img[row])):
		img[row][k] = 0

def zeroCol(img, col):
	for j in img:
		j[col] = 0

print(zeroes(image))
