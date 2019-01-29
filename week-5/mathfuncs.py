import math


def area_circle(r):
	"""
	Calculate the area of a circle.
	Takes the radius as numeric input parameter and returns the area.
	"""
	return (r ** 2) * math.pi


def area_rect(w, h):
	"""
	Calculate the area of a rectangle.
	Takes the width and height as numeric input parameters and returns the area.
	"""
	return w * h


def area_triangle(w, h):
	"""
	Calculate the area of a triangle.
	Takes the width and height as numeric input parameters and returns the area.
	"""
	return w * h / 2


def fact(n):
	"""
	Factorize the value n.
	"""
	if n <= 1:
		return 1
	else:
		return n * fact(n-1)


def fib(n):
	"""
	Calculate the nth element in the fibonacci sequence.
	"""
	if n < 2:
		return n
	else:
		return fib(n-1) + fib(n-2)
