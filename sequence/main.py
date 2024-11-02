import pytest

def layup_sequence(n: int):
	"""
	Implement the Layup Sequence and return the value at N where the squence is defined as:
	S(N) = 1 if N = 1
	S(N) = 2 if N = 2
	S(N) = S(N-1) + S(N-2) if N is even
	S(N) = S(N-1) - S(N-2) if N is odd

	Note: The squence is only defined for N > 1. For input N<=0, the function returns 0.


	Returns:
	  The value of the Layup Sequence at index N.
	"""
	if n <= 0:
		return 0

	if n == 1:
		return 1

	if n == 2:
		return 2

	if (n % 2) == 0:
		return layup_sequence(n-1) + layup_sequence(n-2)
	return layup_sequence(n-1) - layup_sequence(n-2)


def test_base_case1():
	response = layup_sequence(1)
	assert response == 1


def test_base_case2():
	response = layup_sequence(2)
	assert response == 2


@pytest.mark.parametrize("n_value", [0, -5, -100])
def test_values_less_than_1_return_0(n_value):
	response = layup_sequence(n_value)
	assert response == 0

def test_5():
	"""
	S(5)
	= S(4) - S(3)
	= [S(3) + S(2)] - [S(2) - S(1)]
	= [S(2) - S(1) + 2] - [2 - 1]
	= [2 - 1 + 2] - [2 - 1]
	= 3 - 1
	= 2
	"""
	expected = 2
	response = layup_sequence(5)
	assert response == expected


def main():
	return 0


if __name__ == '__main__':
	main()