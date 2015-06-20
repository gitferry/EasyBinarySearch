def  binary_search(source_array, target):
	low = middle = 0
	high = len(source_array) - 1

	while(low <= high):
		middle = (low + high) / 2
		temp = source_array[middle]
		if temp == target:
			return middle
		else if temp > target:
			high = middle - 1
		else:
			low = middle + 1

	return -1


