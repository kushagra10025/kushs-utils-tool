import src.globals as glbs
import src.perform_toss
import src.roll_dice

from src.project_templates.cpp_template import cpp_template
from src.cli_args_parser import CliArgsParser
from src.price_tracker import PriceTracker

def price_alert_func(url, expected_price, sender_email, sender_pass, receiver_email):
	price_tracker = PriceTracker(URL=url, expected_price=expected_price,sender_email=sender_email,sender_password=sender_pass,receiver_email=receiver_email)
	price_tracker.check_price()

def determine_project_to_create(plang : str,ppath:str,pname:str):
	if plang == 'cpp':
		print("=== Start Creating CPP Project ===")
		cpp_t = cpp_template(base_dir=ppath,project_name=pname)
		cpp_t.print_structure()
		print()
		cpp_t.create_strcuture()
		print("=== Done Creating CPP Project ===")
	else:
		print("DEVELOPMENT TERRITORY! DO NOT TRESPASS!!")
	pass

def args_main():
	args_parser = CliArgsParser()
	args_parser.all_init()

	args_parser.create_parser_args()
	args_parser.modify_parser_args()
	args_parser.delete_parser_args()
	args_parser.hackto_parser_args()

	args = args_parser.final_parse_args()

	if args.command == 'create':
		print("Creating '%s' in '%s' at '%s'" % (args.pname,args.plang,args.ppath))
		determine_project_to_create(args.plang,args.ppath,args.pname)
	elif args.command == 'modify':
		print("DEVELOPMENT TERRITORY! DO NOT TRESPASS!!")
	elif args.command == 'delete':
		print("DEVELOPMENT TERRITORY! DO NOT TRESPASS!!")
	elif args.command == 'hackto':
		print("Hacktober Contributed Scripts are here!")
		if args.hackto_command == 'price_alert':
			print("Price Alert Program Started")
			price_alert_func(args.url,args.eprice,args.s_email,args.s_pass,args.r_email)
		if args.hackto_command == 'random':
			print("Random Number Generators here! -h for more details")
			if args.roll_dice == 'ROLL_DICE':
				src.roll_dice.random_dice_roll()
			if args.toss_coin == 'FLIP_COIN':
				src.perform_toss.flipCoin()

	pass

if __name__ == "__main__":
	args_main()


