from anytree import Node,RenderTree, LevelOrderIter
import src.directory as dir
import src.globals as glbs
import src.helpers as helpers
import re

# FIXME Abstract this into a template class then extend this cpp_template

class cpp_template:
	def __init__(self,base_dir=glbs.default_dir_path,project_name=glbs.default_dir_name):
		self.t_name = "cpp"
		self.base_dir = base_dir

		self.root_dir = Node(project_name)
		venv_dir = Node("venv", parent=self.root_dir)
		src_dir = Node("src", parent=self.root_dir)
		main_cpp_file = Node("main.cpp", parent=src_dir)
		conanfile_txt_file = Node("conanfile.txt", parent=self.root_dir)
		cmakelists_txt_file = Node("CMakeLists.txt",parent=self.root_dir)
		out_dir = Node("out",parent=self.root_dir)
		build_dir = Node("build",parent=out_dir)
	
	def print_structure(self):
		for pre, fill, node in RenderTree(self.root_dir):
			print("%s%s" % (pre, node.name))

	def create_strcuture(self):
		regex = re.compile('\.')
		for x in LevelOrderIter(self.root_dir):
			path = helpers.get_path_from_root_to_parent(x)
			path = self.base_dir + path
			if regex.search(x.name) == None:
				dir.create_directory(dir_name=x.name,dir_path=path)
			else:
				dir.create_file(file_name=x.name,file_path=path)
