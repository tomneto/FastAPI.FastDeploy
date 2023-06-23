import os.path

def relative(path):
	return os.path.join(os.path.dirname(__file__), path)

