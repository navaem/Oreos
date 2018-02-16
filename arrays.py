'''
arrays.py 
This program tests the time of two methodologies of tracing through a 2-D array.
@author Eduardo Nava
@version 1.0

'''
import time;





N = input("Enter \n");

A = [[[]for rows in range(N)] for cols in range(N)];
B = [[[]for rows in range(N)] for cols in range(N)];

aStart = time.clock();
#Option A
for i in range(0, N):
	for j in range(0, N):
		A[i][j] = 0.0;
for i in range(0, N):
	A[i][i] = 1.0;
aEnd = time.clock();
print aEnd-aStart;

bStart = time.clock();
#Option B
for i in range(0, N):
	for j in range(0, N):
		if i == j:
			B[i][j] = 1.0;
		else:
			B[i][j] = 0.0;
bEnd = time.clock();

