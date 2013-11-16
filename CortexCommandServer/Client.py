class Client(Server):

	def __init__(self):
		try:
			self.config = io.FileIO("./ClientSettings.cfg", "r+")
		except IOError:
			self.config = 0
		
		try:
			self.logfile = io.FileIO("./ClientLog.log", "a+")
		except IOError:
			self.logfile = 0
		
		exitbool = 0
		
		if (not self.config):
		
			self.config = io.open("./ClientSettings.cfg", "w")
			self.config.write("", "#Only edit the lines below if you know the consequences of editing them.\n",  "localloopport=12525", "localloopaddress=127.0.0.1")
			
			exitbool = 1

		if (not self.logfile):
			
			self.logfile = io.open("./ClientLog.log", "w")
			sys.stdout.buffer.write("@START@"+FormatTime(" at %d/%m/%y %H:%M:%S : ")+"Log Started")
			self.logfile.write("@START@"+FormatTime(" at %d/%m/%y %H:%M:%S : ")+"Log Started\n")

		if (exitbool):
			sys.stdout.buffer.write(b"Configure your configuration file, exiting...")
			return