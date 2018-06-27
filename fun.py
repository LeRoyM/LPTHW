
print "Please enter the name of the file that you are using:"
file = raw_input("> ")
txt = open(file)
print "Heres your file: %r" % file
print txt.read()
txt.close()


