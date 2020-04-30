
def almostIncreasingSequence(sequence):
	dropped = False
	last = prev = min(sequence) - 1
	print(last)

	for element in sequence:
		if element <= last:
			if dropped:
				return False
			else:
				dropped = True
			if element <= prev:
				prev = last
			elif element >= prev:
				prev = last = element
		else:
			print(f'preva: {prev}, lasta:{last}, element: {element}')
			prev, last = last, element
			print(f'prevb: {prev}, lastb:{last}')
	return True

	
if __name__ == "__main__":
	sequence = [1, 1, 2, 3, 4, 4] #False
	# sequence = [1, 2, 1, 2] #False
	sequencea = [1, 3, 2, 1] #False
	# sequence = [1, 2, 3, 4, 3, 6] #True
	# sequence = [1, 2, 5, 3, 5] #True
	# sequence2 = [1, 2, 3, 4, 3, 6] #True
	# sequence3 = [10, 1, 2, 3, 4, 5, 6, 1] #False
	# sequence4 = [1000, 1000, 2000, 3000, 4000, 5000, 5000]
	# sequence5 = [6, 5, 4] #False
	# sequence6 = [-9996, -9995, -9994, -9993, -9991, -9989, -9987, -9986, -9985, -9983, -9982, -9980, -9978, -9977, -9976, -9975, -9974, -9972, -9968, -9966, -9965, -9961, -9957, -9956, -9955, -9954, -9952, -9948, -9942, -9939, -9938, -9936, -9935, -9932, -9931, -9927, -9925, -9923, -9922, -9921, -9920, -9919, -9918, -9908, -9905, -9902, -9901, -9900, -9899, -9897, -9896, -9894, -9888, -9886, -9880, -9878, -9877, -9876, -9874, -9872, -9871, -9870, -9869, -9868, -9867, -9865, -9857, -9856, -9855, -9854, -9853, -9852, -9851, -9849, -9848, -9846, -9845, -9843, -9842, -9841, -9840, -9837, -9834, -9828, -9826, -9824, -9823, -9820, -9816, -9814, -9812, -9811, -9810, -9809, -9807, -9806, -9804, -9803, -9801, -9800]
	sequence7 = [5, 5, 5] #False
	sequence8 = [10, 1, 2, 3, 4, 5] #True
	sequence9 = [1, 3, 2, 4, 3] #False

	print(almostIncreasingSequence(sequence))
	print(almostIncreasingSequence(sequencea))
	print(almostIncreasingSequence(sequence7))
	print(almostIncreasingSequence(sequence8))
	print(almostIncreasingSequence(sequence9))

	

	
