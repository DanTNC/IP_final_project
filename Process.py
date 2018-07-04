from IP_funcs import *
import matplotlib.pyplot as plt
import ImageIO as IIO

def run(arr, x1, x2, y1, y2):
	L = arr.shape[0]
	W = arr.shape[1]
	ary = np.zeros([L,W], dtype = int)
	for i in range(L):	
		for j in range(W):
			if i >= x1 and i <= x2 and j >= y1 and j <= y2:
				ary[j,i] = arr[j,i]
	ary = thresholding(ary, 55, false_val = 0)
	ary = thresholding(ary, 145, 0)
	ary = thresholding(ary, 0, 255)
	ary = opening(ary)
	ary = closing(ary)
	ary = gradient(ary)
	return ary

if __name__=="__main__":
	iio = IIO.ImageIO()
	arr = iio.get_input_image("img/I0071695_1.jpg", "L")
	ans = run(arr,205,380,170,325)
	plt.imshow(ans)
	plt.show()
