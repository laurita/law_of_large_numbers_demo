import random
import matplotlib.pyplot as plt

class LawOfLargeNumbersDemo(object):
	
	def __init__(self, num_rolls):
		self.num_rolls = num_rolls

	def _roll(self):
		return random.randint(1,6)

	def _rollN(self, n):
		total = 0
		for i in range(n):
			total += self._roll()
		return total / n

	def run_demo(self):
		means = []
		for i in range(self.num_rolls):
			means.append(self._rollN(i+1))
		plot_average_dice_roll(means, self.num_rolls)
		
def plot_average_dice_roll(distribution, num_rolls = 1000):
	plt.ion()
	plt.plot(list(range(1, num_rolls+1)), distribution, label = 'Observed average')
	# Theoretical mean of a dice roll is (1+2+3+4+5+6)/6 = 3.5
	plt.plot(list(range(1, num_rolls+1)), [3.5] * num_rolls, label = 'Theoretical mean')

	plt.xlabel('Number of rolls')
	plt.ylabel('Average')

	plt.title('Average dice roll by number of rolls')

	plt.legend()

	plt.show(block=True)