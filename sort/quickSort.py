#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Adam Buran"
__version__ = ""
__contact__ = "aburan28@gmail.com"
import math




def quickSort(A,left,right):
	"""
	Running Time
	------------
	Average: O(n*log(n))
	Best: O(n*log(n))
	Worst: O(n^2)
	"""
	if left < right:
		if right - left == 1:
			if A[left] > A[right]: swap(A, left, right)
		else:
			mid = int(math.floor((left+right)/2))
			med_3 = sorted([A[left], A[mid], A[right]])
			A[left], A[mid], A[right] = med_3[0], med_3[1], med_3[2]

			if right - left  > 2:
				swap(A, left+1, mid)
				i, j, pivot_value = left + 1, right, A[left + 1]
				while i < j:
					i = i + 1
					while A[i] < pivot_value: i = i + 1
					j = j - 1
					while A[j] > pivot_value: j = j - 1
					A[i], A[j] = A[j], A[i]
				A[i], A[j] = A[j], A[i]
				A[j], A[left+1] = A[left+1], A[j]
				quickSort(A, left, j-1)
				quickSort(A, j+1, right)