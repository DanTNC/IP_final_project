from IP_funcs import *
from collections import deque
import matplotlib.pyplot as plt
import ImageIO as IIO


def run(arr, x1, x2, y1, y2):
	q = deque()
	fea = []
	L = arr.shape[0]
	W = arr.shape[1]
	ary = np.zeros([L,W], dtype = int)
	group = np.zeros([L,W], dtype = int)
	val = 0
	for i in range(L):	
		for j in range(W):
			if i >= x1 and i <= x2 and j >= y1 and j <= y2:
				ary[j,i] = arr[j,i]
	ary = thresholding(ary, 54, false_val = 0)
	ary = thresholding(ary, 148, 0)
	ary = thresholding(ary, 0, 255)
	ary = opening(ary)
	ary = closing(ary)
	for i in range(x1, x2+1):
		for j in range(y1, y2+1):
			num = 0
			if ary[j,i] == 255:
				val = val +1
				num = num + 1
				ary[j,i] = 0
				group[j,i] = val
				q.append((i,j))
				while len(q) > 0:
					(x,y) = q.popleft()
					for m in range(x-1, x+2):
						for n in range(y-1, y+2):
							if ary[n,m] == 255:
								num = num + 1
								ary[n,m] = 0
								group[n,m] = val
								q.append((m,n))
				fea.append(num)
	com = 0
	pos = 0
	for k in range(len(fea)):
		if fea[k] >= com:
			com = fea[k]
			pos = k
	for i in range(L):	
		for j in range(W):
			if group[j,i] == pos + 1:
				ary[j,i] = 255
	ary = gradient(ary) 
	return ary
	
if __name__=="__main__":
	iio = IIO.ImageIO()
	arr = iio.get_input_image("img/I0071695_1.jpg", "L")
	ans = run(arr,205,380,170,325)
	plt.imshow(ans)
	plt.show()
