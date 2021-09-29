import src.globals as glbs
from src.project_templates.cpp_template import cpp_template
from src.cli_args_parser import CliArgsParser

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

	args = args_parser.final_parse_args()

	if args.command == 'create':
		print("Creating '%s' in '%s' at '%s'" % (args.pname,args.plang,args.ppath))
		determine_project_to_create(args.plang,args.ppath,args.pname)
	elif args.command == 'modify':
		print("DEVELOPMENT TERRITORY! DO NOT TRESPASS!!")
	elif args.command == 'delete':
		print("DEVELOPMENT TERRITORY! DO NOT TRESPASS!!")
	
	pass

if __name__ == "__main__":
	args_main()


