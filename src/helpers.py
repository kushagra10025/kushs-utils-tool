from anytree import Node

def get_path_from_root_to_parent(x: Node):
	"""
	Helper function for AnyTree - Helps in getting the path from root to parent
	:param x(Node): Node for which root to parent path is required
	:return: Path as a string
	"""
	path_root_to_x = ["%r" % x.separator.join([""] + [str(node.name) for node in x.path])]
	path_root_to_x = ''.join(path_root_to_x)
	path_from_root_to_parent = path_root_to_x.split("/")
	path_from_root_to_parent = path_from_root_to_parent[:-1]
	path_from_root_to_parent = [u + '/' for u in path_from_root_to_parent]
	path_from_root_to_parent = ''.join(path_from_root_to_parent)
	path_from_root_to_parent = path_from_root_to_parent.translate({ord('\''):None})

	return path_from_root_to_parent