Module 2 O(n log n) Behavior

This module contains the following files

  * insertion.py implements InsertionSort
  * merge.py implements mergeSort
  * project_merge.py implements mergeSort on external file

	Also contains compareSortTimes() which compares
	performance of mergeSort against Python's internal
	sort implementation

To run the project, load 'project_merge.py' and create a file which will be sorted. Do so as follows:

  >>> createRandom(100, 'sample-file.txt')

This creates 100 random integers in the range [1,1000] in the given file. If you want to create larger numbers, say:

  >>> createRandom(100, 'sample-file.txt', 10000)

which would create numbers in the range [1,10000]

To show the integers in the file, use the 'output' function

  >>> output('sample-file.txt')

To sort the external file, say:

  >>> mergeSortFile('sample-file.txt')

