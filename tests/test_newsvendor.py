import unittest

import numpy as np
from scipy.stats import norm
from scipy.stats import poisson
from scipy.stats import lognorm

from pyinv import newsvendor
from pyinv.instances import *


# Module-level functions.

def print_status(class_name, function_name):
	"""Print status message."""
	print("module : test_newsvendor   class : {:30s} function : {:30s}".format(class_name, function_name))


def set_up_module():
	"""Called once, before anything else in this module."""
	print_status('---', 'set_up_module()')


def tear_down_module():
	"""Called once, after everything else in this module."""
	print_status('---', 'tear_down_module()')


class TestNewsvendorNormal(unittest.TestCase):
	@classmethod
	def set_up_class(cls):
		"""Called once, before any tests."""
		print_status('TestNewsvendorNormal', 'set_up_class()')

	@classmethod
	def tear_down_class(cls):
		"""Called once, after all tests, if set_up_class successful."""
		print_status('TestNewsvendorNormal', 'tear_down_class()')

	def test_example_4_3(self):
		"""Test that newsvendor_normal function correctly solves Example 4.3.
		"""
		print_status('TestNewsvendorNormal', 'test_example_4_3()')

		holding_cost, stockout_cost, demand_mean, demand_sd = \
			get_named_instance("example_4_3")

		base_stock_level, cost = newsvendor.newsvendor_normal(holding_cost, stockout_cost, demand_mean, demand_sd)
		self.assertAlmostEqual(base_stock_level, 56.603955927433887)
		self.assertAlmostEqual(cost, 1.997605193176645)

		base_stock_level, cost = newsvendor.newsvendor_normal(holding_cost, stockout_cost, demand_mean, demand_sd, base_stock_level=40)
		self.assertAlmostEqual(base_stock_level, 40)
		self.assertAlmostEqual(cost, 7.356131552870388)

	def test_problem_4_1(self):
		"""Test that newsvendor_normal function correctly solves Problem 4.1.
		"""
		print_status('TestNewsvendorNormal', 'test_problem_4_1()')

		holding_cost, stockout_cost, demand_mean, demand_sd = \
			get_named_instance("problem_4_1")

		base_stock_level, cost = newsvendor.newsvendor_normal(holding_cost, stockout_cost, demand_mean, demand_sd)
		self.assertAlmostEqual(base_stock_level, 9.227214038234755e+02)
		self.assertAlmostEqual(cost, 2.718196781782411e+03)

		base_stock_level, cost = newsvendor.newsvendor_normal(holding_cost, stockout_cost, demand_mean, demand_sd, base_stock_level=1040)
		self.assertAlmostEqual(base_stock_level, 1040)
		self.assertAlmostEqual(cost, 6.044298415188692e+03)

	def test_example_4_4(self):
		"""Test that newsvendor_normal function correctly solves the first
		part of Example 4.4 (L=4, R=1).
		"""
		print_status('TestNewsvendorNormal', 'test_example_4_4()')

		holding_cost, stockout_cost, demand_mean, demand_sd, lead_time = \
			get_named_instance("example_4_4")

		base_stock_level, cost = newsvendor.newsvendor_normal(holding_cost, stockout_cost, demand_mean, demand_sd, lead_time=lead_time)
		self.assertAlmostEqual(base_stock_level, 2.647668943741548e+02)
		self.assertAlmostEqual(cost, 4.466781004149578)

		base_stock_level, cost = newsvendor.newsvendor_normal(holding_cost, stockout_cost, demand_mean, demand_sd, lead_time=lead_time, base_stock_level=180)
		self.assertAlmostEqual(base_stock_level, 180)
		self.assertAlmostEqual(cost, 49.000164748034095)

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


class TestNewsvendorNormalCost(unittest.TestCase):
	@classmethod
	def set_up_class(cls):
		"""Called once, before any tests."""
		print_status('TestNewsvendorNormalCost', 'set_up_class()')

	@classmethod
	def tear_down_class(cls):
		"""Called once, after all tests, if set_up_class successful."""
		print_status('TestNewsvendorNormalCost', 'tear_down_class()')

	def test_example_4_3(self):
		"""Test that newsvendor_normal_cost function correctly evaluates cost for
		Example 4.3.
		"""
		print_status('TestNewsvendorNormalCost', 'test_example_4_3()')

		holding_cost, stockout_cost, demand_mean, demand_sd = \
			get_named_instance("example_4_3")

		cost = newsvendor.newsvendor_normal_cost(40, holding_cost, stockout_cost, demand_mean, demand_sd)
		self.assertAlmostEqual(cost, 7.356131552870388)

		cost = newsvendor.newsvendor_normal_cost(60, holding_cost, stockout_cost, demand_mean, demand_sd)
		self.assertAlmostEqual(cost, 2.156131552870387)

		cost = newsvendor.newsvendor_normal_cost(120, holding_cost, stockout_cost, demand_mean, demand_sd, lead_time=3)
		self.assertAlmostEqual(cost, 56.000000752740092)

	def test_problem_4_1(self):
		"""Test that newsvendor_normal_cost function correctly evaluates cost for Problem 4.1.
		"""
		print_status('TestNewsvendorNormalCost', 'test_problem_4_1()')

		holding_cost, stockout_cost, demand_mean, demand_sd = \
			get_named_instance("problem_4_1")

		cost = newsvendor.newsvendor_normal_cost(1100, holding_cost, stockout_cost, demand_mean, demand_sd)
		self.assertAlmostEqual(cost, 8.600820410122849e+03)

		cost = newsvendor.newsvendor_normal_cost(922, holding_cost, stockout_cost, demand_mean, demand_sd)
		self.assertAlmostEqual(cost, 2.718393552026199e+03)

		cost = newsvendor.newsvendor_normal_cost(4000, holding_cost, stockout_cost, demand_mean, demand_sd, lead_time=3)
		self.assertAlmostEqual(cost, 1.720164082024570e+04)


class TestNewsvendorPoisson(unittest.TestCase):
	@classmethod
	def set_up_class(cls):
		"""Called once, before any tests."""
		print_status('TestNewsvendorPoisson', 'set_up_class()')

	@classmethod
	def tear_down_class(cls):
		"""Called once, after all tests, if set_up_class successful."""
		print_status('TestNewsvendorPoisson', 'tear_down_class()')

	def test_example_4_7(self):
		"""Test that newsvendor_poisson function correctly solves Example 4.7
		(without fixed cost).
		"""
		print_status('TestNewsvendorPoisson', 'test_example_4_7()')

		holding_cost, stockout_cost, _, demand_mean = \
			get_named_instance("example_4_7")

		base_stock_level, cost = newsvendor.newsvendor_poisson(holding_cost, stockout_cost, demand_mean)
		self.assertEqual(base_stock_level, 8)
		self.assertAlmostEqual(cost, 3.570106945770946)

		base_stock_level, cost = newsvendor.newsvendor_poisson(holding_cost, stockout_cost, demand_mean, base_stock_level=5)
		self.assertEqual(base_stock_level, 5)
		self.assertAlmostEqual(cost, 6.590296024616344)

	def test_problem_4_8a(self):
		"""Test that newsvendor_poisson function correctly solves Problem 4.8a.
		"""
		print_status('TestNewsvendorPoisson', 'test_problem_4_8a()')

		holding_cost, stockout_cost, demand_mean = \
			get_named_instance("problem_4_8a")

		base_stock_level, cost = newsvendor.newsvendor_poisson(holding_cost, stockout_cost, demand_mean)
		self.assertEqual(base_stock_level, 19)
		self.assertAlmostEqual(cost, 7.860884409351115e+02)

		base_stock_level, cost = newsvendor.newsvendor_poisson(holding_cost, stockout_cost, demand_mean, base_stock_level=13)
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


class TestNewsvendorPoissonCost(unittest.TestCase):
	@classmethod
	def set_up_class(cls):
		"""Called once, before any tests."""
		print_status('TestNewsvendorPoissonCost', 'set_up_class()')

	@classmethod
	def tear_down_class(cls):
		"""Called once, after all tests, if set_up_class successful."""
		print_status('TestNewsvendorPoissonCost', 'tear_down_class()')

	def test_example_4_7(self):
		"""Test that newsvendor_poisson_cost function correctly evaluates cost for
		Example 4.7 (without fixed cost).
		"""
		print_status('TestNewsvendorPoissonCost', 'test_example_4_7()')

		holding_cost, stockout_cost, _, demand_mean = \
			get_named_instance("example_4_7")

		cost = newsvendor.newsvendor_poisson_cost(8, holding_cost, stockout_cost, demand_mean)
		self.assertAlmostEqual(cost, 3.570106945770946)

		cost = newsvendor.newsvendor_poisson_cost(5, holding_cost, stockout_cost, demand_mean)
		self.assertAlmostEqual(cost, 6.590296024616344)

	def test_problem_4_8a(self):
		"""Test that newsvendor_poisson_cost function correctly evaluates cost for
		Problem 4.8a.
		"""
		print_status('TestNewsvendorPoissonCost', 'test_problem_4_8a()')

		holding_cost, stockout_cost, demand_mean = \
			get_named_instance("problem_4_8a")

		cost = newsvendor.newsvendor_poisson_cost(19, holding_cost, stockout_cost, demand_mean)
		self.assertAlmostEqual(cost, 7.860884409351115e+02)

		cost = newsvendor.newsvendor_poisson_cost(13, holding_cost, stockout_cost, demand_mean)
		self.assertAlmostEqual(cost, 1.445751062891969e+03)


class TestNewsvendorContinuous(unittest.TestCase):
	@classmethod
	def set_up_class(cls):
		"""Called once, before any tests."""
		print_status('TestNewsvendorContinuous', 'set_up_class()')

	@classmethod
	def tear_down_class(cls):
		"""Called once, after all tests, if set_up_class successful."""
		print_status('TestNewsvendorContinuous', 'tear_down_class()')

	def test_example_4_1_with_distrib(self):
		"""Test that newsvendor_continuous function correctly solves Example 4.1
		when provided with rv_continuous object.
		"""
		print_status('TestNewsvendorContinuous', 'test_example_4_1_with_distrib()')

		holding_cost, stockout_cost, demand_mean, demand_sd = \
			get_named_instance("example_4_1")

		demand_distrib = norm(demand_mean, demand_sd)

		base_stock_level, cost = newsvendor.newsvendor_continuous(holding_cost, stockout_cost, demand_distrib)
		self.assertAlmostEqual(base_stock_level, 56.603955927433887)
		self.assertAlmostEqual(cost, 1.997605193176645, places=5)

		base_stock_level, cost = newsvendor.newsvendor_continuous(holding_cost, stockout_cost, demand_distrib, base_stock_level=40)
		self.assertAlmostEqual(base_stock_level, 40)
		self.assertAlmostEqual(cost, 7.356131552870388, places=5)

	def test_example_4_1_with_pdf(self):
		"""Test that newsvendor_continuous function correctly solves Example 4.1
		when provided with pdf function.
		"""
		print_status('TestNewsvendorContinuous', 'test_example_4_1_with_pdf()')

		# TODO

	def test_problem_4_8b(self):
		"""Test that newsvendor_continuous function correctly solves Problem
		4.8(b).
		"""
		print_status('TestNewsvendorContinuous', 'test_problem_4_8b()')

		holding_cost, stockout_cost, mu, sigma = \
			get_named_instance("problem_4_8b")

		demand_distrib = lognorm(sigma, 0, np.exp(mu))

		base_stock_level, cost = newsvendor.newsvendor_continuous(holding_cost, stockout_cost, demand_distrib)
		self.assertAlmostEqual(base_stock_level, 2.956266448071368e+02)
		self.assertAlmostEqual(cost, 29.442543582135290, places=5)

		base_stock_level, cost = newsvendor.newsvendor_continuous(holding_cost, stockout_cost, demand_distrib, base_stock_level=350)
		self.assertAlmostEqual(base_stock_level, 350)
		self.assertAlmostEqual(cost, 34.588836685654854, places=5)

	def test_bad_type(self):
		"""Test that newsvendor_continuous function raises exception on bad type.
		"""
		print_status('TestNewsvendorContinuous', 'test_bad_type()')

		holding_cost = "taco"
		stockout_cost = 0.7
		demand_mean = 50
		demand_sd = 8

		demand_distrib = norm(demand_mean, demand_sd)

		with self.assertRaises(TypeError):
			base_stock_level, cost = newsvendor.newsvendor_continuous(holding_cost, stockout_cost, demand_distrib)

	def test_negative_parameter(self):
		"""Test that newsvendor_continuous function raises exception on negative parameter.
		"""
		print_status('TestNewsvendorContinuous', 'test_negative_parameter()')

		holding_cost = -2
		stockout_cost = 0.7
		demand_mean = 50
		demand_sd = 8

		demand_distrib = norm(demand_mean, demand_sd)

		with self.assertRaises(AssertionError):
			base_stock_level, cost = newsvendor.newsvendor_continuous(holding_cost, stockout_cost, demand_distrib)


class TestNewsvendorDiscrete(unittest.TestCase):
	@classmethod
	def set_up_class(cls):
		"""Called once, before any tests."""
		print_status('TestNewsvendorDiscrete', 'set_up_class()')

	@classmethod
	def tear_down_class(cls):
		"""Called once, after all tests, if set_up_class successful."""
		print_status('TestNewsvendorDiscrete', 'tear_down_class()')

	def test_example_4_7_with_distrib(self):
		"""Test that newsvendor_discrete function correctly solves Example 4.7
		(without fixed cost) when provided with rv_discrete object.
		"""
		print_status('TestNewsvendorDiscrete', 'test_example_4_7_with_distrib()')

		holding_cost, stockout_cost, _, demand_mean = \
			get_named_instance("example_4_7")

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

		holding_cost, stockout_cost, _, demand_mean = \
			get_named_instance("example_4_7")

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

		holding_cost, stockout_cost, demand_pmf = \
			get_named_instance("problem_4_7b")

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
		stockout_cost = 4
		demand_mean = 6

		demand_distrib = poisson(demand_mean)

		with self.assertRaises(TypeError):
			base_stock_level, cost = newsvendor.newsvendor_discrete(holding_cost, stockout_cost, demand_mean, demand_distrib)

	def test_negative_parameter(self):
		"""Test that newsvendor_normal function raises exception on negative parameter.
		"""
		print_status('TestNewsvendorDiscrete', 'test_negative_parameter()')

		holding_cost = -4
		stockout_cost = 4
		demand_mean = 6

		demand_distrib = poisson(demand_mean)

		with self.assertRaises(AssertionError):
			base_stock_level, cost = newsvendor.newsvendor_discrete(holding_cost, stockout_cost, demand_mean, demand_distrib)
