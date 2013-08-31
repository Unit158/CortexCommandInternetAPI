"""
Copyright (c) 2013 Unit158

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), the rights
to use, copy, modify, merge, publish and/or distribute the Software, and to 
permit persons to whom the Software is furnished to do so, subject to the following 
conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

These notices are subject to change at any time without notification.
These notices may be waived by the author's premission.

Honestly guys, I don't care if you make money from ads, but I don't want you
selling my software or mods of my software. Yes this includes plugins. 

You can e-mail me to work out a commercial licence if you want to sell mods.

E-mail to: chickenman158@hotmail.com


Alright, lame crap out of the way, let's get to the code!
"""

import time
import socket
import math
import string
import io
import hashlib

Timers = None
Users = None
Commands = None

#Timer = {}
#Timers = {}

#Plugin = {}
#Plugins = {}

#Command = {}
#Commands = {}

name = None
motd = None
port = None
config = io.FileIO("./ServerSettings.cfg", "r+")
logfile = io.FileIO("./ServerLog.log", "a+")
logverbosity = None
sandbox = None
anticheat = None
login = None
admins = None
connections = None
isroutingserver = 0

"""
	Set this to 1 if you want this to be a routing server.
"""

def DebugPrint(listtoprint):
	for i in listtoprint:
		print(tuple(listtoprint))
		return tuple(listtoprint)

def Log(level, stringtolog):
	if(logverbosity < -1):
		logverbosity = 0
		Log(0, "The verbosity is set too low, reset to 0")
	elif(logverbosity > 2):
		logverbosity = 2
		Log(2, "The verbosity is set too high, reset to 2")
	
	levelstr = "?UNKNOWN?"
	if(isinstance(level, number)):
		"""
		2 is severe/critical, 1 is dangerous/important, 0 is info, -1 is debug
		"""
		if(level == 2):
			levelstr = "*SEVERE*"
		elif(level == 1):
			levelstr = "!DANGEROUS!"
		elif(level == 0):
			levelstr = "#INFO#"
		elif(level == -1):
			levelstr = "%DEBUG%"
		else:
			Log(-1, "Level " + level + " is unknown")
	elif(isinstance(level, basestring)):
		tmpl = string.lower(level)
		if(tmpl == "c"):
			levelstr = "*CRITICAL*"
			level = 2
		elif(tmpl == "i"):
			levelstr = "!IMPORTANT!"
			level = 1
		else:
			levelstr = string.upper(tmpl) # For plugin levels.
			level = 2 # Always log plugin levels
	else:
		if(logverbosity == -1):
			raise Exception("The logging argument must be a number or string.") 
		else:
			Log(1, "The logging argument must be a number or a string, logging as unknown.")	

	print(levelstr+os.date(" at %d/%m/%y %H:%M:%S : ")+stringtolog) # Always print
	if(logverbosity < level):
		logfile.write(levelstr + os.date(" at %d/%m/%y %H:%M:%S : ") + stringtolog)

def ParseFile(pattern, file = config):
	s = ""
	varTable = []
	shouldrunloop = True
	
	if(isinstance(pattern, list)):
		
		while(shouldrunloop):
			
			s = file.readline()
			
			for i in pattern:
				
				_, findstart = s.find(i)
				findend, _ = s.find("\n", findstart)
				varTable[len(varTable)+1] = s.sub(findstart + 1, findend - 1)
			
		return tuple(varTable)
	
	elif(isinstance(pattern, str)):
		
		while(shouldrunloop):
			
			s = file.readline()
			_, findstart = s.find(pattern)
			findend, _ = s.find("\n", findstart)
			
		return s.sub(findstart + 1, findend - 1)
	
	else:
		
		if(logverbosity == -1):
			
			raise Exception("Pattern is not a list or a string")
		
		else:
			
			Log(1, "Pattern is not a list or a string, returning nil")

class Servers: #For routing servers only!
	
	def __init__(self):
		return
	
	def getroutingservers(self):
		return
	
	def getservers(self):
		return
	
class RoutingServer:
	
	def __init__(self):
		self.config = io.open("./ServerSettings.cfg", "r+")
		self.logfile = io.open("./ServerLog.log", "a+")
		exitbool = false
		if (config == nil):
			config = io.open("./RoutingServerSettings.cfg", "w")
			config.write("addresstoconnect=\n", "isencrypted=0\n")
			exitbool = True

		if (logfile == nil):
			logfile = io.open("./RoutingServerLog.log", "w")
			print("@START@"+os.date(" at %d/%m/%y %H:%M:%S : ")+"Log Started")
			logfile.write("@START@"+os.date(" at %d/%m/%y %H:%M:%S : ")+"Log Started")

		if (exitbool):
			print("Configure your configuration file, exiting...")
			return
		
		
class Server:
	
	def __init__(self):
		exitbool = false
		if (config == nil):
			config = io.open("./ServerSettings.cfg", "w")
			config.write("name=A Cortex Command Server\n", 
				"motd=Welcome!\n",
				"port=12525\n",
				"logverbosity=-1\n",
				"2 = Critical information and severe problems logged only!\n",
				"1 = Dangerous problems and important information logged only.\n",
				"0 = all info logged.\n",
				"-1 debug, will crash instead of severe. Will also print extra information.\n",
				"forcedsandbox=0\n",
				"anticheat=1\n",
				"requireslogin=0\n",
				"administrators=\n",
				"If there are no names, there are no admins. Much safer than everyone being admin :P\n",
				"bannedusers=\n",
				"whitelist=\n",
				"If there are no names, there will be no whitelist!\n",
				"limitconnections=4\n",
				"0 is no limit, otherwise, you can use any number.\n")
			exitbool = True

		if (logfile == nil):
			logfile = io.open("./ServerLog.log", "w")
			print("@START@"+os.date(" at %d/%m/%y %H:%M:%S : ")+"Log Started")
			logfile.write("@START@"+os.date(" at %d/%m/%y %H:%M:%S : ")+"Log Started")

		if (exitbool):
			print("Configure your configuration file, restarting...")
			return

	name, motd, port, logverbosity, sandbox, anticheat, login, admins,
	connections = ParseFile(["name=", "motd=", "port=", "logverbosity=", 
	"forcedsandbox=", "anticheat=", "requireslogin=", "administrators=", 
	"limitconnections="])
	
	port = int(port)
	logverbosity = int(logverbosity)
	sandbox = int(sandbox)
	anticheat = int(anticheat)
	login = int(login)
	connections = int(connections)
	
	Log(0, "Starting server...")
	Log(0, "Reading plugin files...") #TODO
	Log(0, "Reading plugin files. Done.")
	
	udp = socket.socket(socket.SOCK_DGRAM, socket.AF_INET)
	udp.settimeout(0.0) # Sorry for people with slow connections :(
	
	Log("i", "Server port set to: " + tostring(port))
	Log("i","Server name set to: " + name)
	Log("i","Server message set to: " + motd)
	Log("i","Server logging verbosity level set to: " + tostring(logverbosity))
	
	Log(0, udp.setsockname("*", tonumber(port)))
	Log(0, "Bound successfully") 
	Log(0, "Starting server. Done.")
	Log(0, "Server started.")
	run = True
	runStart = time.time()
	runTime = runStart
	while(run):
		datagram, externip, externport = udp.receivefrom()
		for _,_0 in pairs(Timers):
			print("")
		
		if(datagram != nil and externip != nil and externport != nil):
			for usr in Users.Connected:
				if(externip != usr.ip and True):
					Users.Connected[Users.Connected + 1] = User.new(externip, externport)
				else:
					udp.sendto("Error: Server full", externip, externport) 

	
class Timer:

	def __init__(self):
		return
	
	def GetRunningTime(self):
		return
	
	def ResetTimer(self):
		return
	
class Plugin:

	def __init__(self):
		return
		
#	def

class Command:

	def __init__(self, pattern, permission):
		return
		
	def __call__(self):
		return
		
#	def 
#		
class Users:
	
	def __init__(self):
		self.users = []
		self.admins = []
	
	def getusers(self):
		return self.users
		
	
	def getadmins(self):
		return self.admins
		
	
	def getregisteredusers(self):
		return self.registeredusers
		
	
	def registeruser(self):
		return
		
	
	def deleteregistereduser(self):
		return
		
		
	def getloggedinusers(self):
		return
		
	
	def loginuser(self):
		return
		
	
	def logoutuser(self):
		return
		
	
	def getbannedusers(self):
		return
		
	
	def banuser(self):
		return
		
	
	def unbanuser(self):
		return
		
	
	def getwhitelist(self):
		return
		
	
	def whitelistuser(self):
		return
		
	
	def unwhitelistuser(self):
		return
		
	
class User:

	def __init__(self, ip, port):
		self.ip = ip
		self.port = port
		return

class Room:

	def __init__(self, maxplayers, map, description = "A room"):
		self.maxplayers = 0
		self.players = []
		self.map = map
		self.desc = ""
		return

class Map:

	def __init__(self, image):
		self.image = image
		return
		