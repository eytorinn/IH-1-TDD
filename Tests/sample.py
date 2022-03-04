class FizzBuzz:
	@staticmethod
	def fizzBuzz(num):
		if not num % 15:
			return "FizzBuzz"

		if not num % 3:
			return "Fizz"

		if not num % 5:
			return "Buzz"

		return num