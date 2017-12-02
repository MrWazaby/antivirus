def windowsCorrect(fileName):
	# Read in the file
	with open(fileName, 'r') as file :
	  filedata = file.read()

	# Replace the target string
	filedata = filedata.replace('./', '')

	# Write the file out again
	with open(fileName, 'w') as file:
	  file.write(filedata)
	  
