import argparse
import src.globals as glbs

class CliArgsParser:
	def __init__(self):
		self.parser = argparse.ArgumentParser(description="Kushagra\'s Utils Program!")
		self.subparser = self.parser.add_subparsers(dest="command",description="Available Commands")
		
		self.parser.add_argument('-v','--version',action='version',version="%(prog)s 0.0.1")

		pass

	# Parser Groups are Currently Not Defined
	# TODO Define Parser Groups
	# def init_parser_groups(self):
	# 	self.command_group = self.parser.add_argument_group("Perform Executions")
	# 	self.settings_group = self.parser.add_argument_group("Apply Settings")
	# 	pass

	def init_subparser_parsers(self):
		self.create_parser = self.subparser.add_parser("create",help="Create Project from Templates")
		self.modify_parser = self.subparser.add_parser("modify",help="Modify Project Templates Metadata")
		self.delete_parser = self.subparser.add_parser("delete",help="Delete Exisiting Projects")
		pass

	def all_init(self):
		# self.init_parser_groups()
		self.init_subparser_parsers()
		pass

	def create_parser_args(self):
		# Optional Arguments
		self.create_parser.add_argument(
			'--plang',
			default='cpp',
			choices=['cpp','java','python'],
			help='Specify Projects Major Language (default = cpp)'
		)

		self.create_parser.add_argument(
			'--pname',
			metavar='project_name',
			default=glbs.default_dir_name,
			help='Specify Project\'s Name (default = %s)'%glbs.default_dir_name
		)

		self.create_parser.add_argument(
			'--ppath',
			metavar='project_path',
			default=glbs.default_dir_path,
			help='Speficy Project\'s Path (default = %s)'%glbs.default_dir_path
		)

		# Positional Arguments
		# TODO Add Create Parser Positional Arguments
		pass

	def modify_parser_args(self):
		# Optional Arguments
		self.modify_parser.add_argument(
			'--test1',
			help="Test for Modify Settings Group 1"
		)
		
		self.modify_parser.add_argument(
			'--test2',
			help="Test for Modify Settings Group 2"
		)

		# Positional Arguments
		# TODO Add Modify Parser Positional Arguments
		pass

	def delete_parser_args(self):
		# Optional Arguments
		self.delete_parser.add_argument(
			'--test3',
			help="Test for Delete Settings Group 3"
		)
		
		self.delete_parser.add_argument(
			'--test4',
			help="Test for Delete Settings Group 4"
		)

		# Positional Arguments
		# TODO Add Delete Parser Positional Arguments
		pass

	def final_parse_args(self):
		# args = vars(parser.parse_args()) - Returns Dict
		self.args = self.parser.parse_args()

		print(self.args)
		return self.args