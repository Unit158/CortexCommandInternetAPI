"""
Copyright (c) 2013 Unit158 All Rights Reserved.

THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

These notices are subject to change from the author at any time without notification.
These notices may be waived with the author's written premission.

Try and follow these guidelines (old licence if you paid attention):

"Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), the rights
to use, copy, modify, merge, publish and/or distribute the Software, and to 
permit persons to whom the Software is furnished to do so, subject to the following 
conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software."

Honestly guys, I don't care if you make money from ads, but I don't want you selling my software or mods of my software. Yes this includes plugins. I had to change to All Rights Reserved because I didn't get a lawyer to read over the old licence.

You can e-mail me to work out a commercial licence if you want to sell mods.

E-mail to: chickenman158@gmail.com

Alright, lame crap out of the way, let's get to the code!
"""

import API, GameServer, SystemServer, Client
		
if(__name__ == "__main__"):
		
		if(len(sys.argv) > 1):
		
			if(sys.argv[1] == "system"):
			
				server = SystemServer()
				
			elif(sys.argv[1] == "game"):
			
				server = GameServer()
				
			elif(sys.argv[1] == "client"):
				raise Exception("Unimplemented")
				
			elif(sys.argv[1] == "clientgame"):
				raise Exception("Unimplemented")
				
			elif(sys.argv[1] == "info"):
			
				sys.stdout.buffer.write("Just read the README file.")
				
			else:
			
				raise Exception("Unknown command line argument(s)")
				
		else:
		
			server = GameServer()