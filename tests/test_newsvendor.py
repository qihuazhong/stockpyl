import unittest

from scipy.stats import poisson

from inventory import newsvendor


# Module-level functions.

def print_status(class_name, function_name):
	"""Print status message."""
	print("module : test_newsvendor   class : {:30s} function : {:30s}".format(class_name, function_name))


def setUpModule():
	"""Called once, before anything else in this module."""
	print_status('---', 'setUpModule()')


def tearDownModule():
	"""Called once, after everything else in this module."""
	print_status('---', 'tearDownModule()')


class TestNewsvendorNormal(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		"""Called once, before any tests."""
		print_status('TestNewsvendorNormal', 'setUpClass()')

	@classmethod
	def tearDownClass(cls):
		"""Called once, after all tests, if setUpClass successful."""
		print_status('TestNewsvendorNormal', 'tearDownClass()')

	def test_example_4_3(self):
		"""Test that newsvendor_normal function correctly solves Example 4.3.
		"""
		print_status('TestNewsvendorNormal', 'test_example_4_3()')

		holding_cost = 0.18
		stockout_cost = 0.7
		demand_mean = 50
		demand_sd = 8

		base_stock_level, cost = newsvendor.newsvendor_normal(holding_cost, stockout_cost, demand_mean, demand_sd)
		self.assertAlmostEqual(base_stock_level, 56.603955927433887)
		self.assertAlmostEqual(cost, 1.997605193176645)

		base_stock_level, cost = newsvendor.newsvendor_normal(holding_cost, stockout_cost, demand_mean, demand_sd, 40)
		self.assertAlmostEqual(base_stock_level, 40)
		self.assertAlmostEqual(cost, 7.356131552870388)

	def test_problem_4_1(self):
		"""Test that newsvendor_normal function correctly solves Problem 4.1.
		"""
		print_status('TestNewsvendorNormal', 'test_problem_4_1()')

		holding_cost = 65-22
		stockout_cost = 129-65+15
		demand_mean = 900
		demand_sd = 60

		base_stock_level, cost = newsvendor.newsvendor_normal(holding_cost, stockout_cost, demand_mean, demand_sd)
		self.assertAlmostEqual(base_stock_level, 9.227214038234755e+02)
		self.assertAlmostEqual(cost, 2.718196781782411e+03)

		base_stock_level, cost = newsvendor.newsvendor_normal(holding_cost, stockout_cost, demand_mean, demand_sd, 1040)
		self.assertAlmostEqual(base_stock_level, 1040)
		self.assertAlmostEqual(cost, 6.044298415188692e+03)

	def test_bad_type(self):
		"""Test that newsvendor_normal function raises exception on bad type.
		"""
		print_status('TestNewsvendorNormal', 'test_bad_type()')

		holding_cost = "taco"
		stockout_cost = 0.7
		demand_mean = 50
		demand_sd = 8
		with self.assertRaises(TypeError):
			base_stock_level, cost = newsvendor.newsvendor_normal(holding_cost, stockout_cost, demand_mean, demand_sd)

	def test_negative_parameter(self):
		"""Test that newsvendor_normal function raises exception on negative parameter.
		"""
		print_status('TestNewsvendorNormal', 'test_negative_parameter()')

		holding_cost = -2
		stockout_cost = 0.7
		demand_mean = 50
		demand_sd = 8
		with self.assertRaises(AssertionError):
			base_stock_level, cost = newsvendor.newsvendor_normal(holding_cost, stockout_cost, demand_mean, demand_sd)


class TestNewsvendorPoisson(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		"""Called once, before any tests."""
		print_status('TestNewsvendorPoisson', 'setUpClass()')

	@classmethod
	def tearDownClass(cls):
		"""Called once, after all tests, if setUpClass successful."""
		print_status('TestNewsvendorPoisson', 'tearDownClass()')

	def test_example_4_7(self):
		"""Test that newsvendor_poisson function correctly solves Example 4.7
		(without fixed cost).
		"""
		print_status('TestNewsvendorPoisson', 'test_example_4_7()')

		holding_cost = 1
		stockout_cost = 4
		demand_mean = 6

		base_stock_level, cost = newsvendor.newsvendor_poisson(holding_cost, stockout_cost, demand_mean)
		self.assertEqual(base_stock_level, 8)
		self.assertAlmostEqual(cost, 3.570106945770946)

		base_stock_level, cost = newsvendor.newsvendor_poisson(holding_cost, stockout_cost, demand_mean, 5)
		self.assertEqual(base_stock_level, 5)
		self.assertAlmostEqual(cost, 6.590296024616344)

	def test_problem_4_8a(self):
		"""Test that newsvendor_poisson function correctly solves Problem 4.8a.
		"""
		print_status('TestNewsvendorPoisson', 'test_problem_4_8a()')

		holding_cost = 200
		stockout_cost = 270
		demand_mean = 18

		base_stock_level, cost = newsvendor.newsvendor_poisson(holding_cost, stockout_cost, demand_mean)
		self.assertEqual(base_stock_level, 19)
		self.assertAlmostEqual(cost, 7.860884409351115e+02)

		base_stock_level, cost = newsvendor.newsvendor_poisson(holding_cost, stockout_cost, demand_mean, 13)
		self.assertAlmostEqual(base_stock_level, 13)
		self.assertAlmostEqual(cost, 1.445751062891969e+03)

	def test_bad_type(self):
		"""Test that newsvendor_poisson function raises exception on bad type.
		"""
		print_status('TestNewsvendorPoinsson', 'test_bad_type()')

		holding_cost = "taco"
		stockout_cost = 0.7
		demand_mean = 50
		with self.assertRaises(TypeError):
			base_stock_level, cost = newsvendor.newsvendor_poisson(holding_cost, stockout_cost, demand_mean)

	def test_negative_parameter(self):
		"""Test that newsvendor_poisson function raises exception on negative parameter.
		"""
		print_status('TestNewsvendorPoisson', 'test_negative_parameter()')

		holding_cost = -2
		stockout_cost = 0.7
		demand_mean = 50
		demand_sd = 8
		with self.assertRaises(AssertionError):
			base_stock_level, cost = newsvendor.newsvendor_poisson(holding_cost, stockout_cost, demand_mean)


class TestNewsvendorDiscrete(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		"""Called once, before any tests."""
		print_status('TestNewsvendorDiscrete', 'setUpClass()')

	@classmethod
	def tearDownClass(cls):
		"""Called once, after all tests, if setUpClass successful."""
		print_status('TestNewsvendorDiscrete', 'tearDownClass()')

	def test_example_4_7_with_distrib(self):
		"""Test that newsvendor_discrete function correctly solves Example 4.7
		(without fixed cost) when provided with rv_discrete object.
		"""
		print_status('TestNewsvendorDiscrete', 'test_example_4_7_with_distrib()')

		holding_cost = 1
		stockout_cost = 4
		demand_mean = 6

		demand_distrib = poisson(demand_mean)

		base_stock_level, cost = newsvendor.newsvendor_discrete(holding_cost, stockout_cost, demand_distrib)
		self.assertEqual(base_stock_level, 8)
		self.assertAlmostEqual(cost, 3.570106945770946)

		base_stock_level, cost = newsvendor.newsvendor_discrete(holding_cost, stockout_cost, demand_distrib, base_stock_level=5)
		self.assertEqual(base_stock_level, 5)
		self.assertAlmostEqual(cost, 6.590296024616344)

	def test_example_4_7_with_pmf(self):
		"""Test that newsvendor_discrete function correctly solves Example 4.7
		(without fixed cost) when provided with pmf dict.
		"""
		print_status('TestNewsvendorDiscrete', 'test_example_4_7_with_pmf()')

		holding_cost = 1
		stockout_cost = 4
		demand_mean = 6

		d = range(0, 41)
		f = [poisson.pmf(d_val, demand_mean) for d_val in d]
		demand_pmf = dict(zip(d, f))

		base_stock_level, cost = newsvendor.newsvendor_discrete(holding_cost, stockout_cost, demand_pmf=demand_pmf)
		self.assertEqual(base_stock_level, 8)
		self.assertAlmostEqual(cost, 3.570106945770946)

		base_stock_level, cost = newsvendor.newsvendor_discrete(holding_cost, stockout_cost, demand_pmf=demand_pmf, base_stock_level=5)
		self.assertEqual(base_stock_level, 5)
		self.assertAlmostEqual(cost, 6.590296024616344)

	def test_problem_4_7b(self):
		"""Test that newsvendor_discrete function correctly solves Problem 4.7(b).
		"""
		print_status('TestNewsvendorDiscrete', 'test_problem_4_7b()')

		holding_cost = 500000
		stockout_cost = 1000000
		demand_pmf = {1: 0.25, 2: 0.05, 3: 0.1, 4: 0.2, 5: 0.15, 6: 0.10, 7: 0.10, 8: 0.05}

		base_stock_level, cost = newsvendor.newsvendor_discrete(holding_cost, stockout_cost, demand_pmf=demand_pmf)
		self.assertEqual(base_stock_level, 5)
		self.assertAlmostEqual(cost, 1225000)

		base_stock_level, cost = newsvendor.newsvendor_discrete(holding_cost, stockout_cost, demand_pmf=demand_pmf, base_stock_level=3)
		self.assertAlmostEqual(base_stock_level, 3)
		self.assertAlmostEqual(cost, 1.725000000000000e+06)

	def test_bad_type(self):
		"""Test that newsvendor_normal function raises exception on bad type.
		"""
		print_status('TestNewsvendorDiscrete', 'test_bad_type()')

		holding_cost = "taco"
		stockout_cost = 0.7
		demand_mean = 50
		demand_sd = 8
		with self.assertRaises(TypeError):
			base_stock_level, cost = newsvendor.newsvendor_normal(holding_cost, stockout_cost, demand_mean, demand_sd)

	def test_negative_parameter(self):
		"""Test that newsvendor_normal function raises exception on negative parameter.
		"""
		print_status('TestNewsvendorDiscrete', 'test_negative_parameter()')

		holding_cost = -2
		stockout_cost = 0.7
		demand_mean = 50
		demand_sd = 8
		with self.assertRaises(AssertionError):
			base_stock_level, cost = newsvendor.newsvendor_normal(holding_cost, stockout_cost, demand_mean, demand_sd)
