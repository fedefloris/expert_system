# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parse.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 20:49:23 by dhojt             #+#    #+#              #
#    Updated: 2018/07/16 01:00:49 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import ft

char_fact = "="
char_query = "?"

def read_file():
	if len(sys.argv) != 2:
		exit(2)
	try:
		f = open(sys.argv[1], "r")
	except IOError:
		exit(2)
	if f.mode != "r":
		exit(2)
	lines = f.readlines()
	f.close
	return (lines)


# LINE TYPES
# 0 Error
# 1 Blank Line
# 2 Rule
# 3 Fact
# 4 Query


def parse():
	def get_type(line):
		def is_rule(line):
			for x in line:
				if not (ft.is_upper(x) or ft.char_matches(x, "+|!^<=>()")):
					return (0)
			count = 0
			for x in line:
				if ft.is_upper(x):
					count += 1
				elif ft.char_matches(x, "+|^="):
					count -= 1
				if count > 1 or count < 0:
					return (0)
			if line.count("=>") + line.count("<=>") != 1 or line.count("=") != 1:
				return (0)
			return (1)


		def is_fact(line):
			for x in line:
				if not (ft.is_upper(x) or x == char_fact):
					return (0)
			if line[0] != char_fact:
				return (0)
			if line.count(char_fact) != 1:
				return (0)
			return (1)


		def is_query(line):
			for x in line:
				if not (ft.is_upper(x) or x == char_query):
					return (0)
			if line[0] != char_query:
				return (0)
			if line.count(char_query) != 1:
				return (0)
			return (1)


		def is_blank_line(line):
			if len(line) == 0:
				return (1)
			return (0)

		if is_blank_line(line):
			return (1)
		if is_query(line):
			return (4)
		if is_fact(line):
			return (3)
		if is_rule(line):
			return (2)
		return (0)

	class Line:
		def __init__(self, string, line_num):
			self.string = string.replace("\n", "")
			self.data = string.replace("\n", "")
			self.data = self.data.replace("\t", "")
			self.data = self.data.replace(" ", "")
			self.data = self.data.split("#")[0]
			self.type = get_type(self.data)
			self.num = line_num

	line_num = 1
	lines = []
	for line in read_file():
		tmp = Line(line, line_num)
		lines.append(tmp)
		line_num += 1
	return (lines)