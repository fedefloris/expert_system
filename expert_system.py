#!/usr/bin/env python3.6

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    expert_system.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dhojt <dhojt@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/12 00:09:39 by dhojt             #+#    #+#              #
#    Updated: 2018/07/17 21:30:28 by dhojt            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import argparse
sys.path.extend(["./src/", "./src/parser/", "./src/inference_engine/"])

from Config import Config
from Parser import Parser
from Lexer import Lexer
from ParsingError import ParsingError
from InferenceEngine import InferenceEngine

def parse_arguments():
	parser = argparse.ArgumentParser(description='A propositional calculus expert system.')
	parser.add_argument("-c", "--config", metavar="file", help="file with symbols values")
	parser.add_argument("-v", "--verbose", action="store_true",
		help="displays investigation steps of the inference engine")
	parser.add_argument("-o", "--output", action="store_true",
		help="displays original input but prints facts in correct colour")
	parser.add_argument("file", help="file with rules and facts")
	if len(sys.argv) == 1:
		parser.print_help()
		parser.exit()
	return (parser.parse_args())

def main():
	args = parse_arguments()
	try:
		config = Config(args.config, args)
		lexer = Lexer(config, args.file)
		parser = Parser(config)
	except ParsingError as ex:
		exit(ex)
	engine = InferenceEngine(config)
	engine.induce()

if __name__== "__main__":
	main()
