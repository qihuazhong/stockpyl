from random import randint
import unittest
import numpy as np
import copy

from stockpyl.demand_source import DemandSource
import stockpyl.gsm_serial as gsm_serial
import stockpyl.gsm_tree as gsm_tree
from stockpyl.instances import load_instance
from stockpyl.supply_chain_network import SupplyChainNetwork
from stockpyl.supply_chain_node import SupplyChainNode


# Module-level functions.

def print_status(class_name, function_name):
	"""Print status message."""
	print("module : test_gsm_serial   class : {:30s} function : {:30s}".format(class_name, function_name))


def set_up_module():
	"""Called once, before anything else in this module."""
	print_status('---', 'set_up_module()')


def tear_down_module():
	"""Called once, after everything else in this module."""
	print_status('---', 'tear_down_module()')


class TestOptimizeCommittedServiceTimes(unittest.TestCase):

	@classmethod
	def set_up_class(cls):
		"""Called once, before any tests."""
		print_status('TestOptimizeCommittedServiceTimes', 'set_up_class()')

	@classmethod
	def tear_down_class(cls):
		"""Called once, after all tests, if set_up_class successful."""
		print_status('TestOptimizeCommittedServiceTimes', 'tear_down_class()')

	def test_example_6_4(self):
		"""Test that optimize_committed_service_times() works for network in
		Example 6.4.
		"""

		print_status('TestOptimizeCommittedServiceTimes', 'test_example_6_4')

		network = load_instance("example_6_4")

		opt_cost, opt_cst = \
			gsm_serial.optimize_committed_service_times(network=network)

		self.assertEqual(opt_cost, 2 * np.sqrt(2))
		self.assertDictEqual(opt_cst, {1: 1, 2: 0, 3: 0})

	def test_problem_6_7(self):
		"""Test that optimize_committed_service_times() works for network in
		Problem 6.7.
		"""

		print_status('TestOptimizeCommittedServiceTimes', 'test_problem_6_7')

		network = load_instance("problem_6_7")

		opt_cost, opt_cst = \
			gsm_serial.optimize_committed_service_times(network=network)

		self.assertAlmostEqual(opt_cost, 160 * np.sqrt(5))
		self.assertDictEqual(opt_cst, {1: 0, 2: 3, 3: 2})

	def test_problem_6_8(self):
		"""Test that optimize_committed_service_times() works for network in
		Problem 6.8.
		"""

		print_status('TestOptimizeCommittedServiceTimes', 'test_problem_6_8')

		network = load_instance("problem_6_8")

		opt_cost, opt_cst = \
			gsm_serial.optimize_committed_service_times(network=network)

		self.assertAlmostEqual(opt_cost, 1378.31, 1)
		self.assertDictEqual(opt_cst, {1: 3, 2: 10, 3: 0, 4: 28, 5: 13, 6: 5, 7: 0, 8: 18, 9: 13, 10: 12})

	def test_random_instances(self):
		"""Test that optimize_committed_service_times() works for randomly
		generated networks, when compared to tree DP.
		"""

		print_status('TestOptimizeCommittedServiceTimes', 'test_random_instances')

		NUM_TRIALS = 10

		for _ in range(NUM_TRIALS):

			# Build network.
			network = SupplyChainNetwork()
			num_nodes = np.random.randint(3, 20)
			z_alpha = np.random.rand() * 4
			for n in range(1, num_nodes + 1):
				node = SupplyChainNode(
					index=n,
					network=network,
					processing_time=np.random.randint(0, 10),
					local_holding_cost=n + n * np.random.rand(),
					demand_bound_constant = z_alpha
				)
				if n == 1:
					node.external_outbound_cst = np.random.randint(0, 5)
					node.demand_source = DemandSource(type='N', mean=0, standard_deviation=np.random.rand() * 100)
				elif n == num_nodes:
					node.external_inbound_cst = np.random.randint(10)	
				network.add_node(node)
				if n > 1:
					network.add_edge(n, n - 1)
			
			# Solve using serial DP.
			opt_cost, opt_cst = \
				gsm_serial.optimize_committed_service_times(network=network)

			# Solve using tree DP.
			tree = gsm_tree.preprocess_tree(network)
			opt_cost_tree, opt_cst_tree = \
				gsm_tree.optimize_committed_service_times(tree=tree)

			self.assertAlmostEqual(opt_cost, opt_cost_tree)
			self.assertDictEqual(opt_cst, opt_cst_tree)

