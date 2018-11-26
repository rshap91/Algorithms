# Sorting_Algorithms
import random

# selection sort
def selection_sort(alist):
	''' For each element in alist, swap with lowest element in list
	Time Taken: O(n**2)
	where O is some constant
	where n is the length of alist
	'''
	# for each item
	for i in range(len(alist)-1):
		#print 'Current Index/ Value:', i, ' : ', alist[i]
		l_idx = i+1 
		#print 'min remaining value', alist[l_idx]
		# find the lowest item in remainder of list
		for j in range(i + 2, len(alist)):
			# save index of lowest item in l_idx
			if alist[j] < alist[l_idx]:
				l_idx = j
		#		print 'new min val: ', alist[l_idx]
		# if lowest item is less than current item
		if alist[l_idx] < alist[i]:
			# swap the two items
			alist[l_idx], alist[i] = alist[i], alist[l_idx]
		#	print 'swapped!', alist[l_idx], '<-->', alist[i]
	return alist



# bubble Sort
def bubble_sort(alist):
	''' Seems pretty intuitive. 
	Iterate through list and on each pass swap all consecutive elements
	so that the smaller item is first.
	Even if the smallest item in the list is the last item, 
	after n iterations it will have been moved to the front step by step
	Time Taken: <= O(n**2)
	Worst Case Scenario is O(n**2) depending on where smallest item is.

	When you run it, notice how large numbers get propegated towards the back of the lest in each iteration.
	'''
	iter_count = len(alist)
	for i in range(iter_count):
		#print 'current iteration:', i
		for j in range(1,iter_count):
		#	print 'current index: ', j
			if alist[j] < alist[j-1]:
				alist[j-1], alist[j] = alist[j], alist[j-1]
		#		print 'swapped! ', alist[j], '<-->', alist[j-1]
		#		print alist
	return alist


# Improved bubble_sort
def improved_bubble(alist):
	''' Notice how in the buble sort, even when it's nearing the end
	it still iterates through all the numbers in the list even though we 
	already know they've been moved back as far as they can go.
	This version cuts down on that by removing extra iterations at the end
	based on how many you already have. 
	Additionally, if nothing gets swapped throughout the whole iteration 
	it means the sort is done... i think
	'''
	iter_count = len(alist)
	swapped = 1
	for i in range(iter_count):
		#print 'current iteration: ', i
		if swapped:
			swapped = 0
			# this cuts down on iterations at the end
			for j in range(iter_count-i-1):
		#		print 'current idx:', j
				if alist[j] > alist[j+1]:
					alist[j+1],alist[j] = alist[j], alist[j+1]
		#			print 'swapped!', alist[j], '<-->', alist[j+1]
		#			print alist
					swapped = 1
	return alist




# Test Performance
l_small = [random.randint(1,100) for num in range(1, 100)]
l_small2 = [n for n in l_small]
l_small3 = [n for n in l_small]

l_large = [random.randint(1,10000) for num in range(1, 10000)]
l_large2 = [n for n in l_large]
l_large3 = [n for n in l_large]


%timeit -r5 selection_sort(l_small) # 461 µs per loop
%timeit -r5 bubble_sort(l_small2) # 869 µs per loop
%timeit -r5 improved_bubble(l_small3) # 13 µs per loop


%timeit -r5 selection_sort(l_large) # 4.84 s per loop
%timeit -r5 bubble_sort(l_large2) #  10.7 s per loop
%timeit -r5 improved_bubble(l_large3) # 1.21 ms per loop




# MERGE SORT 
def mergeSort(alist):
	print("Splitting ",alist)
	if len(alist)>1:
		mid = len(alist)//2
		lefthalf = alist[:mid]
		righthalf = alist[mid:]

		mergeSort(lefthalf)
		mergeSort(righthalf)

		i=0
		j=0
		k=0
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				alist[k]=lefthalf[i]
				i=i+1
			else:
				alist[k]=righthalf[j]
				j=j+1
			k=k+1

		# if lengths of two halves are uneven (aka len(alist) is odd)
		while i < len(lefthalf):
			alist[k]=lefthalf[i]
			i=i+1
			k=k+1

		while j < len(righthalf):
			alist[k]=righthalf[j]
			j=j+1
			k=k+1
	print("Merging ",alist)

alist = [98,4,22,45,2,33,11,1,90,47,45]
mergeSort(alist)
print(alist)

