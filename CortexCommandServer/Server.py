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

These notices are subject to change from the author at any time without notification.
These notices may be waived with the author's written premission.

Honestly guys, I don't care if you make money from ads, but I don't want you
selling my software or mods of my software. Yes this includes plugins. 

You can e-mail me to work out a commercial licence if you want to sell mods.

E-mail to: chickenman158@gmail.com


Alright, lame crap out of the way, let's get to the code!
"""

import time
import traceback
import socket
import math
import string
import io
import hashlib
import re
import sys

name = ""
motd = ""
port = 0

try:
	
	config = io.FileIO("./ServerSettings.cfg", "r+")
	
except IOError:
	
	config = 0

try:
	
	logfile = io.FileIO("./ServerLog.log", "a+")

except IOError:

	logfile = 0
	
logverbosity = 0
sandbox = 0
anticheat = 1
login = 0
admins = ""
connections = ""
isroutingserver = 0

"""
	Set this to 1 if you want this to be a routing server.
"""

def FormatTime(stringtoformat):

	#Stolen code. Credits to badp on Stack Overflow. Stolen from here:
	#http://stackoverflow.com/a/2487161
	
	localtime = time.localtime()
	timeString = time.strftime(str(stringtoformat), localtime)
	
	#tz = -(time.altzone if localtime.tm_isdst else time.timezone)
	#timeString += "Z" if tz == 0 else "+" if tz > 0 else "-"
	#timeString += time.strftime("%H'%M'", time.gmtime(abs(tz)))
	
	return bytes(timeString, "UTF-8")
	
def DebugPrint(listtoprint):

	for i in listtoprint:
	
		sys.stdout.buffer.write(i)
		
	return tuple(listtoprint)

def Log(level, bytestolog):
	global logverbosity
	global logfile
	
	if(isinstance(bytestolog, str)):
		raise TypeError("Second argument must be bytes.")
	
	try:
		global logverbosity
		global logfile
		
		if(logverbosity < -1):
			logverbosity = 0
			Log(0, b"The verbosity is set too low, reset to 0")
		elif(logverbosity > 2):
			logverbosity = 2
			Log(2, b"The verbosity is set too high, reset to 2")
		
		levelbytes = b"?UNKNOWN?"
		if(isinstance(level, int)):
			"""
			2 is severe/critical, 1 is dangerous/important, 0 is info, -1 is debug
			"""
			if(level == 2):
				levelbytes = b"*SEVERE*"
			elif(level == 1):
				levelbytes = b"!DANGEROUS!"
			elif(level == 0):
				levelbytes = b"#INFO#"
			elif(level == -1):
				levelbytes = b"%DEBUG%"
			else:
				Log(-1, b"Level " + str(level) + b" is unknown.")
		elif(isinstance(level, bytes)):
			tmpl = bytes.lower(level)
			if(tmpl == b"c"):
				levelbytes = b"*CRITICAL*"
				level = 2
			elif(tmpl == b"i"):
				levelbytes = b"!IMPORTANT!"
				level = 1
			else:
				levelbytes = bytes.upper(tmpl) # For plugin levels.
				level = 2 # Always log plugin levels
		else:
			if(logverbosity == -1):
				raise Exception(b"The logging argument must be a number or string.") 
			else:
				Log(1, b"The logging argument must be a number or a string, logging as unknown.")	

		sys.stdout.buffer.write(levelbytes+FormatTime(" at %d/%m/%y %H:%M:%S : ")+bytestolog+b"\n") # Always print
		if(logverbosity < level):
			logfile.write(levelbytes + FormatTime(" at %d/%m/%y %H:%M:%S : ")+ bytestolog+ b"\n")
	
	except NameError:	
		traceback.print_exc()
		sys.stdout.buffer.write("*SEVERE*" + FormatTime(" at %d/%m/%y %H:%M:%S : ").decode("UTF-8") + "An important variable has not yet been assigned!") # Always print
		logfile.write(b"*SEVERE*" + FormatTime(" at %d/%m/%y %H:%M:%S : ") + b"An important variable has not yet been assigned! \n")
		logverbosity = 0
	
def ParseFile(pattern, file = config):
	
	if(isinstance(pattern, list)):
		
		varTable = []
		
		for i in pattern:
		
			hasfound = 0
			file.seek(0)
			
			for s in file:
				
				if(re.match(b"#(?!.*)", s)):
				
					pass
					
				else:
				
					matchobj = re.search(i+b"(.*)$", s)
					
					if(matchobj == None):
						
						pass
				
					else:
					
						hasfound = 1
						varTable.append(matchobj.group(1))
						break
						
			if(not hasfound):
			
				Log(-1, DebugPrint([b"Pattern " + i + b" was not found with ParseFile() regex!"]))
		
		return tuple(varTable)
	
	elif(isinstance(pattern, bytearray)):
		
		for s in file:
			
			matchobj = re.search(i+b".*[\n]", s)
			
			if(matchobj != None):
			
				Log(-1, b"Pattern " + pattern + b" was not found with ParseFile() regex!")
				
			else:
			
				return DebugPrint([matchobj.extend("")])
	
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
		try:
			self.config = io.FileIO("./RoutingServerSettings.cfg", "r+")
		except IOError:
			self.config = 0
		
		try:
			self.logfile = io.FileIO("./RoutingServerLog.log", "a+")
		except IOError:
			self.logfile = 0
		
		exitbool = 0
		
		if (not self.config):
		
			self.config = io.open("./RoutingServerSettings.cfg", "w")
			self.config.write("addresstoconnect=\n", "isencrypted=0\n")
			
			exitbool = 1

		if (not self.logfile):
			
			self.logfile = io.open("./RoutingServerLog.log", "w")
			sys.stdout.buffer.write("@START@"+FormatTime(" at %d/%m/%y %H:%M:%S : ")+"Log Started")
			self.logfile.write("@START@"+FormatTime(" at %d/%m/%y %H:%M:%S : ")+"Log Started\n")

		if (exitbool):
			sys.stdout.buffer.write("Configure your configuration file, exiting...")
			return
		
		run = 1
		
		udp = socket.socket(socket.AF_INET, socket.DGRAM)
		
		while(run):
			
class Server:
	
	
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
		global isroutingserver
		
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
		runStart = time.time()
		runTime = runStart
		
		while(run):
			
			datagram, externip, externport = udp.recvfrom()
			
			for _,_0 in pairs(Timers):
				sys.stdout.buffer.write("")
		
			if(datagram != None and externip != None and externport != None):
				
				for usr in Users.ConnectedIPs():
					
					if(externip != usr.ip and 1):
						Users.Connected[Users.Connected + 1] = User.new(externip, externport)

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
		
class Command:

	def __init__(self, pattern, permission):
		return
		
	def __call__(self):
		return
		
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
		
	def getImage():
		return self.image
		
if(__name__ == "__main__"):
		
		if(len(sys.argv) > 1):
		
			if(sys.argv[1] == "routing"):
			
				pass
				
			elif(sys.argv[1] == "game"):
			
				server = Server()
				
			elif(sys.argv[1] == "info"):
			
				sys.stdout.buffer.write("Just read the README file.")
				
			else:
			
				raise Exception("Unknown command line argument(s)")
				
		else:
		
			server = Server()