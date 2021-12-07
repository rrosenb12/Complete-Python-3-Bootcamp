myfile = open('test.txt')
print(myfile.read())
# First Line
# Second Line
print(myfile.read())
# ''

myfile.seek(0)
# Resets cursor to the beginning of file
print(myfile.read())

myfile.readlines()
# Returns list of all the lines separated by a comma

myfile.close()

with open('test.txt') as my_new_file:
    contents = my_new_file.read()
    # opens the file but only uses it for the indented code so you don't have to manually close it

with open ('test.txt',mode='r') as my_file:
    my_file.read()

# mode='r' is read only
# mode='w' is write only (will overwrite files or create new)
## Will create a file that doesn't exist if you try to open it with mode='w'
# mode='a' is append only (will add on to files)
# mode='r+' is reading and writing
# mode='w+' is writing and reading (overwrites existing files or creates new file)

with open('writing_files.txt',mode='w+') as writing_file:
    print(writing_file.read())
    # creates new file and reads its contents

with open ('writing_files.txt',mode='a') as f:
    f.write('first line')

with open ('writing_files.txt',mode='r') as f:
    print(f.read())