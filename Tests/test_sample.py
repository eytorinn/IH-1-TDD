from sample import FizzBuzz

def test_if_function_returns():
    assert FizzBuzz.fizzBuzz(1) != None

def test_if_function_is_FizzBuzz():
    for i in range(0,100,15):
        assert FizzBuzz.fizzBuzz(i) == 'FizzBuzz'
    
