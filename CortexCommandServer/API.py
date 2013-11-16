import time
import traceback
import socket
import math
import string
import io
import hashlib
import re
import sys
from urllib import request as req
import urllib
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
issystemserver = 0
udp = 0

"""
	Set this to 1 if you want this to be a system server.
"""

def CheckIP(ip):
	octets = re.split("[.]", ip)
	checktcp = socket.socket()
	try:
		response = req.urlopen("http://%s.%s.%s.%s.dnsbl.sorbs.net/"%(octets[3],octets[2],octets[1],octets[0]))
		print(response.read())
		return 0
	except (urllib.error.HTTPError):
		return 0
	except (socket.gaierror, urllib.error.URLError) as e:
		print(e)
		
		return 1
	
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

class ServersClass: #For system servers only!
	
	gameservers = {}
	systemservers = {}
	
	def __init__(self):
		return
	
	def getsystemservers(self):
	
		return systemservers
	
	def getservers(self):
		return
		
class Timer:

	def __init__(self, callback = 0):
		self.starttime = time
		self.runtime = starttime
		if callback is not 0:
			self.callback = callback
	
	def GetStartTime(self):
		return self.starttime
	
	def GetRunningTime(self):
		return runtime
	
	def GetThread(self):
		return self.thread
	
	def ResetTimer(self):
		self = Timer(self.callback)
		
	def PauseTimer(self):
		self.thread
		
	def ResumeTimer(self):
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
		if(isinstance(user, User)):
			pass
		elif(isinstance(user, basestring)):
			pass
	
	def deleteregistereduser(self):
		if(isinstance(user, User)):
			pass
		elif(isinstance(user, basestring)):
			pass
		
	def getloggedinusers(self):
		return
		
	
	def loginuser(self):
		if(isinstance(user, User)):
			pass
		elif(isinstance(user, basestring)):
			pass
	
	def logoutuser(self):
		if(isinstance(user, User)):
			pass
		elif(isinstance(user, basestring)):
			pass
	
	def getbannedusers(self):
		return
		
	
	def banuser(self, usr):
		if(usr.incognito):
			log("Banned ip: " + usr.ip)
		if(isinstance(usr, User)):
			usr = usr.name
			
		log("Banned player: " + usr, "c")
		self.getuserbyname(usr)
		self.bannedusers.append(usr)
	
	def unbanuser(self, user):
		if(isinstance(user, User)):
			pass
		elif(isinstance(user, basestring)):
			pass
			
	def getwhitelist(self):
		return
		
	
	def whitelistuser(self):
		if(isinstance(user, User)):
			pass
		elif(isinstance(user, basestring)):
			pass
	
	def unwhitelistuser(self):
		if(isinstance(user, User)):
			pass
		elif(isinstance(user, basestring)):
			pass

class User:

	def __init__(self, ip, port, id, name):
		self.ip = ip
		self.port = port
		self.id = id
		if name is not None:
			self.name = b"Incognito" + bytes(str(id), "UTF-8")
		else:
			self.name = name
			
	def send(self, datagram):
		udp.sendto(datagram, self.ip)
		
	def kick(self, message):
		self.send("BOOT Kicked: " + message)
		self.disconnect()
		
	def ban(self, message):
		userlist.banuser(self)
		
	def disconnect(self, message = "") :
		if(message != 0 or message != "" or message != None):
			self.send("BOOT " + message)
			userlist.disconnectuser(self)
		else:
			userlist.disconnectuser(self)
			
class Room:

	def __init__(self, maxplayers, map, description = "A room"):
		self.maxplayers = 0
		self.players = []
		self.map = map
		self.desc = ""
	

class Map:

	def __init__(self, image):
		self.image = image # DIBs on the image. I am so drole.
	
		
	def getImage():
		return self.image # Please don't abuse this line. Maps have feelings too.