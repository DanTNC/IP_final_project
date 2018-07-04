import numpy as np

# Conduct smoothing on the image
# @arr: the image (array-like)
# @Return: the processed image
def smoothing(arr):
	h, w = arr.shape
	new_res = np.zeros_like(arr)
	for i in xrange(h):
		for j in xrange(w):
			region = arr[max(0, i - 1): min(i + 2, h), max(0, j - 1): min(j + 2, w)]
			new_val = region.sum()/region.size
			new_res[i, j] = new_val
	return new_res

# Conduct thresholding on the image
# @arr: the image (array-like)
# @thres: the threshold
# @true_val: the value to be assigned when it's larger than threshold (don't change if set to None)
# @false_val: the value to be assigned when it's smaller than threshold (don't change if set to None)
# @Return: the processed image
def thresholding(arr, thres = 45, true_val = None, false_val = None):
	new_res = np.array(arr)
	h, w = arr.shape
	for i in xrange(h):
		for j in xrange(w):
			if arr[i, j] > thres:
				if true_val is not None:
					new_res[i, j] = true_val
			else:
				if false_val is not None:
					new_res[i, j] = false_val
	return new_res

# Conduct gradient on the image
# @arr: the image (array-like)
# @Return: the processed image
def gradient(arr):
	return sum(np.absolute(np.gradient(arr)))

# Conduct dilation on the image
# @arr: the image (array-like)
# @Return: the processed image
def dilation(arr):
	h, w = arr.shape
	new_res = np.full_like(arr, 0)
	for i in xrange(h):
		for j in xrange(w):
			if (arr[max(0, i - 1): min(i + 2, h), max(0, j - 1): min(j + 2, w)] == 255).any():
				new_res[i, j] = 255
	return new_res

# Conduct erosion on the image
# @arr: the image (array-like)
# @Return: the processed image
def erosion(arr):
	h, w = arr.shape
	new_res = np.full_like(arr, 0)
	for i in xrange(h):
		for j in xrange(w):
			if (arr[max(0, i - 1): min(i + 2, h), max(0, j - 1): min(j + 2, w)] == 255).all():
				new_res[i, j] = 255
	return new_res

# Conduct opening on the image
# @arr: the image (array-like)
# @Return: the processed image
def opening(arr):
	return dilation(erosion(arr))

# Conduct closing on the image
# @arr: the image (array-like)
# @Return: the processed image
def closing(arr):
	return erosion(dilation(arr))

# Return the requested functions (@funcs: in list of string)
def get_funcs(funcs):
	return [globals()[f] for f in funcs]
