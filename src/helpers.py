from anytree import Node
import cowsay
import random

def print_random_cowsay_way(result):
	c = random.randint(1,10)
	if c == 1:
		cowsay.cow(result)
	elif c == 2:
		print(cowsay.get_output_string('trex', result))
	elif c == 3:
		cowsay.dragon(result)
	elif c == 4:
		cowsay.daemon(result)
	elif c == 5:
		cowsay.ghostbusters(result)
	elif c == 6:
		cowsay.kitty(result)
	elif c == 7:
		cowsay.turtle(result)
	elif c == 8:
		cowsay.tux(result)
	elif c == 9:
		cowsay.pig(result)
	else:
		cowsay.cheese(result)
	pass

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