def almostIncreasingSequence(sequence):
	elements_removed = 0	
	elements_removedb = 0	
	sequenceb = sequence.copy()

	for element in range(len(sequence)):
		print(f'list: {sequence}')

		for i in range(len(sequence)):					
			if i < (len(sequence) - 1) and i > 0:
				if sequence[i] < sequence[i - 1]:
					elements_removed+= 1
					print(f'x) To remove {sequence[i - 1]}')  
					sequence.pop(i - 1)
				elif sequence[i] > sequence[i - 1] and sequence[i] < sequence[i + 1]:
					print('A) OK')
				elif sequence[i] >= sequence[i - 1] and sequence[i] < sequence[i + 1]:
					elements_removed+= 1
					print(f'B) To remove {sequence[i]}')  
					sequence.pop(i)
				elif sequence[i] > sequence[i - 1] and sequence[i] < sequence[i + 1]:
					elements_removed+= 1
					print(f'C) To remove {sequence[i + 1]}')  
					sequence.pop(i + 1)
				elif sequence[i] > sequence[i - 1] and sequence[i] >= sequence[i + 1]:
					elements_removed+= 1
					print(f'D) To remove {sequence[i + 1]}')  
					sequence.pop(i + 1)			

	for element in range(len(sequenceb)):
		print(f'list: {sequenceb}')

		for i in range(len(sequenceb)):			
			if i < (len(sequenceb) - 1) and i > 0:
				if sequenceb[i] < sequenceb[i - 1]:
					elements_removedb+= 1
					print(f'x) To remove {sequenceb[i - 1]}')  
					sequenceb.pop(i - 1)
				elif sequenceb[i] > sequenceb[i - 1] and sequenceb[i] < sequenceb[i + 1]:
					print('A) OK')
				elif sequenceb[i] >= sequenceb[i - 1] and sequenceb[i] < sequenceb[i + 1]:
					elements_removedb+= 1
					print(f'B) To remove {sequenceb[i]}')  
					sequenceb.pop(i)
				elif sequenceb[i] > sequenceb[i - 1] and sequenceb[i] < sequenceb[i + 1]:
					elements_removedb+= 1
					print(f'C) To remove {sequenceb[i + 1]}')  
					sequenceb.pop(i + 1)
				elif sequenceb[i] > sequenceb[i - 1] and sequenceb[i] >= sequenceb[i + 1]:
					elements_removedb+= 1
					print(f'D) To remove {sequenceb[i]}')  
					sequenceb.pop(i)


	if elements_removed > elements_removedb:
		if elements_removedb <= 1:
			print(f'Total Elements removed: {elements_removedb}')
			print(f'Final list: {sequenceb}')
			return True
		else:
			print(f'Total Elements removed: {elements_removedb}')
			print(f'Final list: {sequenceb}')
			return False

	elif elements_removedb <= elements_removedb:
		if elements_removed <= 1:
			print(f'Total Elements removed: {elements_removed}')
			print(f'Final list: {sequence}')
			return True
		else:
			print(f'Total Elements removed: {elements_removed}')
			print(f'Final list: {sequence}')
			return False	


if __name__ == "__main__":
	# sequence = [1, 1, 2, 3, 4, 4] #False
	# sequence = [1, 2, 1, 2] #False
	# sequence = [1, 3, 2, 1] #False
	# sequence = [1, 2, 3, 4, 3, 6] #True
	sequence = [1, 2, 5, 3, 5] #True
	sequence2 = [1, 2, 3, 4, 3, 6] #True
	sequence3 = [10, 1, 2, 3, 4, 5, 6, 1] #False
	sequence4 = [1000, 1000, 2000, 3000, 4000, 5000, 5000]
	sequence5 = [6, 5, 4]


	print(almostIncreasingSequence(sequence))
	print(almostIncreasingSequence(sequence2))
	print(almostIncreasingSequence(sequence3))
	print(almostIncreasingSequence(sequence4))
	print(almostIncreasingSequence(sequence5))
	

	

	
