# Import the 'modules' that are required for execution

import pytest


# A simple addition function that adds/concatenates two input values
def add_operation(input_1, input_2):
    return input_1 + input_2


# We make use of the parametrize decorator to supply input arguments
# to the test function

@pytest.mark.parametrize('inp_1, inp_2,result',
                         [
                             (9, 6, 15),
                             ('Cross browser testing on ', 'LambdaTest', 'Cross browser testing on LambdaTest')
                         ]
                         )
def test_add_integers_strings(inp_1, inp_2, result):
    result_1 = add_operation(inp_1, inp_2)
    print(result_1)
    assert result_1 == result