# p08_two_image
size(328,154) #用你的background.jp圖的大小
imgBG = loadImage('background.jpg')
image(imgBG, 0, 0)
imgcat= loadImage('cat.png') #找半透明的png圖
image(imgcat, 0, 0, 100,100)
