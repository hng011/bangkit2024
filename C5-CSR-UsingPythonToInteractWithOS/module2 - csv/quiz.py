# NO 1
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, "w") as f:
    filesize = f.write(comments)
  return(filesize)

# NO 2
import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename, "w") as file:
    pass

  # Return the list of files in the new directory

  return os.listdir(os.getcwd())

# NO 3
import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename, "w") as f:
    pass

  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  date = str(datetime.datetime.fromtimestamp(timestamp)).split(" ")[0]
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{date}".format(date=date))

# Should be today's date in the format of yyyy-mm-dd

# NO 4
import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  relative_parent = os.path.join(os.getcwd(), "..")

  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)

# NO 4B
import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  relative_parent = os.path.join("..", "/")

  # Return the absolute path of the parent directory
  return relative_parent

print(parent_directory())
