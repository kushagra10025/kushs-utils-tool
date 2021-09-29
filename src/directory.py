import pathlib as pl
import src.globals as glbs

def create_file(file_name=glbs.default_file_name,file_path=glbs.default_dir_path):
	"""
	Create file if not exist at the given path
	:param file_name: Name of the File.
	:param file_path: Path of where to create the File.
	"""
	# NOTE Detect File type and write the template for that file in there
	final_dir_path=pl.Path().joinpath(file_path,file_name)
	try:
		final_dir_path.touch(exist_ok=False)
		print("File '%s' Successfully created" % (file_name))

	except FileExistsError:
		print("File '%s' already exists" % (file_name))


def create_directory(dir_name=glbs.default_dir_name, dir_path=glbs.default_dir_path):
	""" 
	Create directory if not exist. Even creates the parent directory if  it does not exist
	:param dir_name: Name of Directory
	:param dir_path: Path where to create the directory 
	"""
	
	final_dir_path = pl.Path().joinpath(dir_path,dir_name)
	try:
		final_dir_path.mkdir(parents=True,exist_ok=False)
		print("Directory '%s' Successfully created" % (dir_name))
	except FileExistsError:
		print("Directory '%s' already exists" % (dir_name))

