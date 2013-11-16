class GameServer:
	
	
	def __init__(self):
		
		global name
		global motd
		global port
		global config
		global logfile
		global logverbosity
		global sandbox
		global anticheat
		global login
		global admins
		global connections
		global issystemserver
		
		#Used by the API and plugins, to be initialized by plugins
		global udp
		global playerlist
		global commands
		global rooms
		
		self.plugins = []
		
		if(config):
		
			if(config.read(1) == ""):
			
				self.config = 0
		
		exitbool = 0
		
		if (not config):
		
			config = io.FileIO(b"ServerSettings.cfg", "w")
			
			config.write(b"name=A Cortex Command Server\n"+
				b"motd=Welcome!\n"+
				b"port=12525\n"+
				b"logverbosity=-1\n"+
				b"2 = Critical information and severe problems logged only!\n"+
				b"1 = Dangerous problems and important information logged only.\n"+
				b"0 = all info logged.\n"+
				b"-1 debug, will crash instead of severe. Will also print extra information.\n"+
				b"forcedsandbox=0\n"+
				b"anticheat=1\n"+
				b"requireslogin=0\n"+
				b"administrators=\n"+
				b"If there are no names, there are no admins. Much safer than everyone being admin :P\n"+
				b"bannedusers=\n"+
				b"whitelist=\n"+
				b"If there are no names, there will be no whitelist!\n"+
				b"limitconnections=4\n"+
				b"0 is no limit, otherwise, you can use any number.\n")
			exitbool = 1

		if (not logfile):
		
			self.logfile = io.open("./ServerLog.log", "w")
			sys.stdout.buffer.write("@START@"+FormatTime(" at %d/%m/%y %H:%M:%S : ")+"Log Started")
			logfile.write(b"@START@"+FormatTime(" at %d/%m/%y %H:%M:%S : ")+b"Log Started\n")

		if (exitbool == 1):
		
			sys.stdout.buffer.write("Configure your configuration file, restarting...")
			return

		name, motd, port, logverbosity, sandbox, anticheat, login, admins, connections = ParseFile([b"name=", b"motd=", b"port=", b"logverbosity=", 
		b"forcedsandbox=", b"anticheat=", b"requireslogin=", b"administrators=", 
		b"limitconnections="])
		
		port = int(port)
		logverbosity = int(logverbosity)
		sandbox = int(sandbox)
		anticheat = int(anticheat)
		login = int(login)
		connections = int(connections)
	
		Log(0, b"Starting server...")
		Log(0, b"Reading plugin files...") #TODO
		Log(0, b"Reading plugin files. Done.")
		
		udp = socket.socket(socket.SOCK_DGRAM, socket.AF_INET)
		udp.settimeout(0.0)
		
		Log(b"i", b"Server port set to: " + bytes(str(port), "UTF-8"))
		Log(b"i", b"Server name set to: " + name)
		Log(b"i", b"Server message set to: " + motd)
		Log(b"i", b"Server logging verbosity level set to: " + bytes(str(logverbosity), "UTF-8"))
		
		Log(0, b"Bound successfully") 
		Log(0, b"Starting server. Done.")
		Log(0, b"Server started.")
		
		run = 1
		runStart = time.clock()
		runTime = runStart
		
		while(run):
			
			udp.listen(0)
			datagram, externip, externport = udp.recvfrom()
			
			for mod in plugins:
				mod.update()
		
			if(datagram is not None and externip is not None and externport is not None):
				
				datagram = datagram.upper()
				
				if(datagram == b"CONNECT"):
				
					shouldAdd = 1
					
					for usr in Users.getusers(): # If there is a better way, please tell me.
					
						if(externip == usr.ip):
							shouldAdd == 0
						else:
							Users.Connected[Users.Connected + 1] = User.new(externip, externport)
				
				if(datagram == b"PING"):
					
					for usr in Users.getusers():
					
						if(externip == usr.ip): # Ouch? Slow?
							usr.send("PONG")