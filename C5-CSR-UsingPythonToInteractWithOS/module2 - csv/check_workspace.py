import os

dir = os.getcwd()
for name in os.listdir(dir):
	fn = os.path.join(dir, name)
	if os.path.isdir(fn):
		print(f"{fn} is a dir")
	else:
		print(f"{fn} is a file")