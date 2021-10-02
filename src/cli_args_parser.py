import argparse
import src.globals as glbs

class CliArgsParser:
	def __init__(self):
		self.parser = argparse.ArgumentParser(description="Kushagra\'s Utils Program!")
		self.subparser = self.parser.add_subparsers(dest="command",description="Available Commands")
		
		self.parser.add_argument('-v', '--version', action='version', version="%(prog)s 0.0.2")

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
		self.hackto_parser = self.subparser.add_parser("hackto",help="Utility scripts by community during Hacktober")
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

	def hackto_parser_args(self):	
		self.sub_hackto_parser = self.hackto_parser.add_subparsers(dest="hackto_command",description="Community scripts from hacktobers")

		# START RANDOM CHANCES SECTION
		self.hackto_random_parser = self.sub_hackto_parser.add_parser("random",help="Random Chances Things!")
		self.hackto_random_parser.add_argument("--roll_dice",action='store_const',const='ROLL_DICE',help="Roll A Double Dice!")
		self.hackto_random_parser.add_argument("--toss_coin",action='store_const',const='FLIP_COIN',help="Toss A Coin!")
		self.hackto_random_parser.add_argument("--sort_hat", action='store_const', const='SORT_HAT', help="Get sorted at Hogwartz!")
		# END RANDOM CHANCES SECTION
		
		# START PRICE_ALERT SECTION
		self.hackto_price_alert_parser = self.sub_hackto_parser.add_parser("price_alert",help="Get Price alert for Amazon.in products")
		self.hackto_price_alert_parser.add_argument(
			'url',
			help='Enter the Amazon.in URL for the product'
		)
		self.hackto_price_alert_parser.add_argument(
			'eprice',
			help='Enter the Expected price in INR for the product'
		)
		self.hackto_price_alert_parser.add_argument(
			'--s_email',
			default=glbs.default_sender_email,
			help='Sender Email'
		)
		self.hackto_price_alert_parser.add_argument(
			'--s_pass',
			default=glbs.deafult_sender_password,
			help='Sender Password'
		)
		self.hackto_price_alert_parser.add_argument(
			'--r_email',
			default=glbs.default_receiver_email,
			help='Receiver Email'
		)
		# END PRICE ALERT SECTION

		pass

	def final_parse_args(self):
		# args = vars(parser.parse_args()) - Returns Dict
		self.args = self.parser.parse_args()

		# print(self.args)
		return self.args