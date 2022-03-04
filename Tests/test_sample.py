from sample import FizzBuzz

def test_if_function_returns():
    assert FizzBuzz.fizzBuzz(1) != None

def test_if_function_is_FizzBuzz():
    for i in range(0,100,15):
        assert FizzBuzz.fizzBuzz(i) == 'FizzBuzz'

def test_if_function_is_Buzz():
    for i in range(0,100,5):
        if i % 15 == 0:
            pass
        else:
            assert FizzBuzz.fizzBuzz(i) == 'Buzz'
    
def test_if_function_is_Fizz():
    for i in range(0,100,3):
        if i % 15 == 0:
            pass
        else:
            assert FizzBuzz.fizzBuzz(i) == 'Fizz'

    
