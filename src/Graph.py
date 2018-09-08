# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Graph.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/24 18:35:31 by dhojt             #+#    #+#              #
#    Updated: 2018/08/06 19:03:53 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Line import Line
from And import And
from Base import Base
from Expr import Expr
from Fact import Fact

class Graph:
	def __init__(self, config):
		self.config = config
		self.__create_nodes()
		self.__clean_unused_nodes()
		self.__add_expr()
		#self.__expand_expr(config)

	def __create_nodes(self):
		self.data = {x:None for x in self.config.facts}
		self.config.graph = self.data
		for line in self.config.lines:
			self.__create_node(line)

	def __create_node(self, line):
		for char in line.data:
			if char in self.config.facts and not self.data[char]:
				self.data[char] = Fact(char)
			if char in self.config.facts and line.type == 3:
				self.data[char].make_true()

	def __clean_unused_nodes(self):
		for key in list(self.data.keys()):
			if not self.data[key]:
				del self.data[key]

	def __add_expr(self):
		for line in self.config.lines:
			if line.type == Line.RULE_TYPE:
				char = line.data.split(self.config.implies_sub)[1]
				data = line.data.split(self.config.implies_sub)[0]
				if not char.count(self.config.op_neg):
					self.data[char].add_true(Expr(data))
				else:
					self.data[char.split(self.config.op_neg)[1]].add_false(Expr(data))

	"""
	def __expand_expr(self, config):
		for key, fact in self.data.items():
			for condition in fact.trueif:
				condition.brackets(self.config)
			for condition in fact.falseif:
				condition.brackets(self.config)
	"""

	def solve(self):
		# Simulate Ands inside Expr.
		c = And("A+B")
		f = And("D+E")
		i = And("G+H")
		l = And("J+K")

		c.add_true(Base("A"))
		c.add_true(Base("B"))
		f.add_true(Base("D"))
		f.add_true(Base("E"))
		i.add_true(Base("G"))
		i.add_true(Base("H"))
		l.add_true(Base("J"))
		l.add_true(Base("K"))

		self.data["C"].trueif[0].add_true(c)
		self.data["F"].trueif[0].add_true(f)
		self.data["I"].trueif[0].add_true(i)
		self.data["L"].trueif[0].add_true(l)

		# Print before
		self.tmp_display()

		# Algo. Currently only checks once, but should check until satisfactory.
		for key, fact in self.data.items():
			print("\x1b[38;2;255;125;0mINVESTIGATE: %s\x1b[0m" % fact.name)
			fact.contradiction()
			fact.check(self.config)
			fact.display()
			print("")

		# Print after
		self.tmp_display()

		self.config.display()

	def tmp_display(self):	 							#TEMPORARY - DELETE
		for key, fact in self.data.items():				#TEMPORARY - DELETE
			fact.display()								#TEMPORARY - DELETE
		print("\n")										#TEMPORARY - DELETE
