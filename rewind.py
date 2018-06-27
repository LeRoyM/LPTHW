from sys import argv

script, input_file = argv

current_file = open(input_file)

print "First read: " + current_file.readline()
x = current_file.tell()
print x
print "Second read: " + current_file.readline()
current_file.seek(x)
print "Third read: " + current_file.readline()
x = current_file.tell()
print x