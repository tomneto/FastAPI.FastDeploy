from sys import stderr

from docs.descriptions import example  # This line imports the descriptions example description ;)


def loadDescription(endpoint, method):
	try:
		return getattr(eval(endpoint), method)()
	except Exception as e:
		stderr.write(str(e) + '\n')
		return ''
