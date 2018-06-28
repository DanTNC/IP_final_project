import numpy as np
from scipy.signal import convolve2d as conv # conv(arr, Ki, mode="same", boundary="symm")
import matplotlib.pyplot as plt

GUASSIAN_KERNEL = np.array([[2,  4,  5,  4, 2],
							[4,  9, 12,  9, 4],
							[5, 12, 15, 12, 5],
							[4,  9, 12,  9, 4],
							[2,  4,  5,  4, 2]])

DIR_NEIGHBOR = [(1, -1), (0, -1), (-1, -1), (-1, 0)]

NEIGHBORS = DIR_NEIGHBOR + [(-1, 1), (0, 1), (1, 1), (1, 0)]

WEAK, CANDIDATE, STRONG = 0, 1, 2

TH_HIGH, TH_LOW = 250, 220

class CannyEdge(object):
	@staticmethod
	def run(arr):
		assert len(arr.shape) == 2
		h, w = arr.shape
		# res = CannyEdge.smooth(arr)
		res = arr
		gy, gx = np.gradient(res.astype(float))
		mag = (gx**2 + gy**2)**(0.5)
		# plt.imshow(mag)
		# plt.show()
		ang = np.arctan2(gy, gx)/np.pi*180
		ang_grp = np.floor((ang - 22.5)/45).astype(int)%4
		res = CannyEdge.surpress(mag, ang_grp, h, w)
		return CannyEdge.double_threshold(arr, h, w)

	@staticmethod
	def smooth(arr):
		return conv(arr, GUASSIAN_KERNEL, mode="same", boundary="fill")

	@staticmethod
	def surpress(mag, dire, h, w):
		res = np.zeros_like(mag)
		for y in xrange(h):
			for x in xrange(w):
				dd = DIR_NEIGHBOR[dire[y, x]]
				yy1, xx1, yy2, xx2 = y + dd[1], x + dd[0], y - dd[1], x - dd[0]
				test1, test2 = True, True
				if 0 <= yy1 < h and 0 <= xx1 < w:
					test1 = mag[y, x] >= mag[yy1, xx1]
				if 0 <= yy2 < h and 0 <= xx2 < w:
					test2 = mag[y, x] >= mag[yy2, xx2]
				res[y, x] = mag[y, x] if test1 and test2 else 0.0
		return res

	@staticmethod
	def double_threshold(arr, h, w):
		res = np.full_like(arr, WEAK, dtype=int)
		# res[arr > TH_LOW] = CANDIDATE
		res[arr > TH_HIGH] = STRONG
		ress = np.array(res)
		plt.imshow(ress)
		plt.show()
		for y in xrange(h):
			for x in xrange(w):
				if res[y, x] != CANDIDATE:
					continue
				for j in xrange(8):
					dx, dy = NEIGHBORS[j]
					xx, yy = x + dx, y + dy
					if 0 <= yy < h and 0 <= xx < w and res[yy, xx] == STRONG:
						ress[y, x] = STRONG
						break
		plt.imshow(ress)
		plt.show()
		ress[ress == CANDIDATE] = WEAK
		plt.imshow(ress)
		plt.show()
		ress[ress == STRONG] = 1
		plt.imshow(ress)
		plt.show()
		return ress
