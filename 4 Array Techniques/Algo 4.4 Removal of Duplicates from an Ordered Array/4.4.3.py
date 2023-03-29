# Let's assume we have an array of size n and we want to perform some operation that involves accessing all elements of the array except the first two and the last two elements. One possible array configuration that will lead to (n-2) data movement operations is:
'''
Assuming that n represents the number of elements in the array, an array configuration that will lead to (n-2) data movement operations is:

Array: [a1, a2, a3, ..., an]

Operations:
1. Move a1 to a3
2. Move a2 to a4
3. Move a3 to a5
...
n-2. Move a(n-2) to an
In this configuration, each element is moved two positions to the right, except for the first two elements which are not moved. Therefore, there are (n-2) data movement operations.

'''