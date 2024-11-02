

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
	return 0


def test_base_case1():
	response = layup_sequence(1)
	assert response == 1


def test_base_case2():
	response = layup_sequence(2)
	assert response == 2


@pytest.parametrize("n_value", [0, -5, -100])
def test_values_less_than_1_return_0(n_value):
	response = layup_sequence(n_value)
	assert response == 0

def test_5():
	# TODO
	expected = -1 
	response = layup_sequence(5)
	assert response == expected


def main():
	# TODO



if __name__ == '__main__':
	main()