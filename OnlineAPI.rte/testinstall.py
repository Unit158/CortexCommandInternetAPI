import io, sys
file = io.FileIO(b"output", "w")

if(sys.version_info.major != 3): # version_info.major vs version_info[0]? I think version_info.major looks prettier
   file.write(b"You have the wrong version of python. You must be running python 3.3. Check http://python.org/.\n")

try:
    import wx
except ImportError:
    file.write(b"wxPython has not been installed.\n")
	
try:
    import constructs
except ImportError:
	file.write(b"Constructs has not been installed.\n")
	
try:
    import DIB
except ImportError:
    file.write(b"The DIB library has not been installed.\n")