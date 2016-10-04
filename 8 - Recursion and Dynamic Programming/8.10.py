# implement the paint fill function

class pixel:
    r = 0
    g = 0
    b = 0

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        return str(self.r) + " " + str(self.g) + " " + str(self.b)

def fill(img, x, y, color):
    if len(img) == 0 or len(img[0]) == 0:
        return

    memo = []
    for i in range(len(img)):
        memo.append([False for i in range(len(img[0]))])

    print(memo)
    to_change = img[x][y]
    fill_helper(img, x, y, color, memo, to_change)

def fill_helper(img, x, y, color, memo, to_change):

    #print(str(x) + " " + str(y))
    if x < 0 or y < 0 or x >= len(img) or y >= len(img[0]): #out of bounds
        return

    if img[x][y].r == to_change.r and img[x][y].g == to_change.g and img[x][y].b == to_change.b: #same pixel color
        if memo[x][y]:#already changed
            return
        else: #not changed
            img[x][y] = color
            memo[x][y] = True
        #change similar surrounding pixels
        fill_helper(img, x - 1, y, color, memo, to_change)
        fill_helper(img, x + 1, y, color, memo, to_change)
        fill_helper(img, x - 1, y + 1, color, memo, to_change)
        fill_helper(img, x + 1, y + 1, color, memo, to_change)
        fill_helper(img, x - 1, y - 1, color, memo, to_change)
        fill_helper(img, x + 1, y - 1, color, memo, to_change)
        fill_helper(img, x, y + 1, color, memo, to_change)
        fill_helper(img, x, y - 1, color, memo, to_change)

    return


img = []
for i in range(5):
    img.append([pixel(0,0,0) for j in range(5)])

img[0][0].r = 2
img[1][1].r = 2
img[1][2].r = 2

img[4][4].r = 2


for i in img:
    print(i)

fill(img, 0, 0, pixel(9,9,9))

for i in img:
    print(i)

