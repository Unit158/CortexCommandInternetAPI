class SystemServer:

	def __init__(self):
		try:
			self.config = io.FileIO("./SystemServerSettings.cfg", "r+")
		except IOError:
			self.config = 0
		
		try:
			self.logfile = io.FileIO("./SystemServerLog.log", "a+")
		except IOError:
			self.logfile = 0
		
		exitbool = 0
		
		if (not self.config):
		
			self.config = io.open("./SystemServerSettings.cfg", "w")
			self.config.write(b"addresstoconnect=\n",  b"expecteduptimehours=")
			
			exitbool = 1

		if (not self.logfile):
			
			self.logfile = io.open("./SystemServerLog.log", "w")
			sys.stdout.buffer.write(b"@START@"+FormatTime(" at %d/%m/%y %H:%M:%S : ")+b"Log Started")
			self.logfile.write(b"@START@"+FormatTime(" at %d/%m/%y %H:%M:%S : ")+b"Log Started\n")

		if (exitbool):
			sys.stdout.buffer.write(b"Configure your configuration file, exiting...")
			return
		
		run = 1
		
		tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connectaddr, estimup = ParseFile(self.config)
		
		while(run):
			tcp.