filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.

new_filenames = []
for filename in filenames:
    if filename.endswith("hpp"):
        new_filenames.append(filename.replace(".hpp", ".h"))
    else:
        new_filenames.append(filename)


print(new_filenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
new_filenames = [f.replace(".hpp",".h") for f in filenames]  # Start your code here


print(new_filenames) 
# Should print ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]