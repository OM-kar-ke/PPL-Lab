try:
   fh = open("testfile", "r")
   fh.write("Test output")
except IOError:
   print("Error: File not Found")
else:
   print("Written content in the file successfully")


try :
   x = 1 / 0
   print(x)
except ZeroDivisionError:
   print("Error: Divide by zero")
else :
   print("Division successful")


try :
   x = 5 * test
   print(x)
except NameError:
   print("Error: Variable not defined")
else :
   print("Calculation successful")


try :
   x = '2' + 6
   print(x)
except TypeError:
   print("Error: Conversion not possible")
else :
   print("Conversion successful")


try :
   import test.h
except ImportError:
   print("Error: Import not possible")
else :
   print("Import successful")







