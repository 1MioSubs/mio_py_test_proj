import math
from time import perf_counter
from numba import njit


@njit(fastmath=True)
def is_prime(num):
	if num == 2:
		return True
	if num <= 1 or not num % 2:
		return False
	for div in range(3, int(math.sqrt(num)) + 1, 2):
		if not num % div:
			return False
	return True


@njit(fastmath=True)
def run_program(N):
	for i in range(N):
		#is_prime(i)

		res = is_prime(i)
		if i >= 99999500:
			if res == True:
				print(f'{i} - {res}')


if __name__ == '__main__':
	N = 100000000
	start = perf_counter()
	run_program(N)
	end = perf_counter()
	print(end - start)