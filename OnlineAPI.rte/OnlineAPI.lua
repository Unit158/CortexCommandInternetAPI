NetworkingAPI = {}

local Singleton = {};

--[[
	
	Requires: No arguments
	Returns: Errors, as this is just to help people use the Singletons.
]]--

function NetworkingAPI:new()
	print("This is a singleton class! You cannot make a new NetworkingAPI instance, use getinstance() instead.")
end

--[[
	Registers an SceneObject with the API. Will check that the server has the same SceneObject.
	Requires: A pointer to an SceneObject object
	Returns: The pointer to the API's object.
]]--

function NetworkingAPI:registerSceneObject(SceneObject)

end

--[[
	Registers AHuman with the API. Will check that the server has the same AHuman.
	Requires: A pointer to AHuman object
	Returns: The pointer to the API's object.
]]--

function NetworkingAPI:registerMovableObject(MovableObject)

end

--[[
	Registers AHuman with the API. Will check that the server has the same AHuman.
	Requires: A pointer to AHuman object
	Returns: The pointer to the API's object.
]]--

function NetworkingAPI:registerMOSprite(MOSprite)

end

--[[
	Registers AHuman with the API. Will check that the server has the same AHuman.
	Requires: A pointer to AHuman object
	Returns: The pointer to the API's object.
]]--

function NetworkingAPI:registerMOSParticle(MOSParticle)

end

--[[
	Registers AHuman with the API. Will check that the server has the same AHuman.
	Requires: A pointer to AHuman object
	Returns: The pointer to the API's object.
]]--

function NetworkingAPI:registerMOSRotating(MOSRotating)

end

--[[
	Registers AHuman with the API. Will check that the server has the same AHuman.
	Requires: A pointer to AHuman object
	Returns: The pointer to the API's object.
]]--

function NetworkingAPI:registerAttachable(Attachable)

end

--[[
	Registers AHuman with the API. Will check that the server has the same AHuman.
	Requires: A pointer to AHuman object
	Returns: The pointer to the API's object.
]]--

function NetworkingAPI:registerHeldDevice(HeldDevice)

end

--[[
	Registers AHuman with the API. Will check that the server has the same AHuman.
	Requires: A pointer to AHuman object
	Returns: The pointer to the API's object.
]]--

function NetworkingAPI:registerHDFirearm(HDFirearm)

end

--[[
	Registers AHuman with the API. Will check that the server has the same AHuman.
	Requires: A pointer to AHuman object
	Returns: The pointer to the API's object.
]]--

function NetworkingAPI:registerThrownDevice(ThrownDevice)

end

--[[
	Registers AHuman with the API. Will check that the server has the same AHuman.
	Requires: A pointer to AHuman object
	Returns: The pointer to the API's object.
]]--

function NetworkingAPI:registerTDExplosive(TDExplosive)

end

--[[
	Registers AHuman with the API. Will check that the server has the same AHuman.
	Requires: A pointer to AHuman object
	Returns: The pointer to the API's object.
]]--

function NetworkingAPI:registerAEmitter(AEmitter)

end

--[[
	Registers AHuman with the API. Will check that the server has the same AHuman.
	Requires: A pointer to AHuman object
	Returns: The pointer to the API's object.
]]--

function NetworkingAPI:registerMagazine(Magazine)

end

--[[
	Registers AHuman with the API. Will check that the server has the same AHuman.
	Requires: A pointer to AHuman object
	Returns: The pointer to the API's object.
]]--

function NetworkingAPI:registerActor(Actor)
	
end

--[[
	Registers AHuman with the API. Will check that the server has the same AHuman.
	Requires: A pointer to AHuman object
	Returns: The pointer to the API's object.
]]--

function NetworkingAPI:registerAHuman(AHuman)

end

--[[
	Registers AHuman with the API. Will check that the server has the same AHuman.
	Requires: A pointer to AHuman object
	Returns: The pointer to the API's object.
]]--

function NetworkingAPI:registerACrab(ACrab)

end

--[[
	Registers AHuman with the API. Will check that the server has the same AHuman.
	Requires: A pointer to AHuman object
	Returns: The pointer to the API's object.
]]--

function NetworkingAPI:registerADoor(ADoor)

end

--[[
	Registers AHuman with the API. Will check that the server has the same AHuman.
	Requires: A pointer to AHuman object
	Returns: The pointer to the API's object.
]]--

function NetworkingAPI:registerACraft(ACraft)

end

--[[
	Registers AHuman with the API. Will check that the server has the same AHuman.
	Requires: A pointer to AHuman object
	Returns: The pointer to the API's object.
]]--

function NetworkingAPI:registerADropship(ADropship)

end

--[[
	Registers AHuman with the API. Will check that the server has the same AHuman.
	Requires: A pointer to AHuman object
	Returns: The pointer to the API's object.
]]--

function NetworkingAPI:registerARocket(ARocket)

end

--[[
	Forces the API  to update. It is quite an expensive operation.
	Requires: Nothing
	Returns: Nothing
]]--

function NetworkingAPI:forceupdate()
	
end

--[[
	Gets the instance of the Networking API.
	Requires: A pointer to AHuman object
	Returns: The pointer to the API's object.
]]--

function NetworkingAPI:startserver() -- Requires python! It will be included with the release, so feel happy :)
	print("Starting server, please wait...")
	os.execute("python Server.py")
	print("Server started")
end

--[[
	Gets the instance of the Networking API.
	Requires: A pointer to AHuman object
	Returns: The pointer to the API's object.
]]--

function NetworkingAPI:getinstance()
	return Singleton
end

--[[
    Sends a chat message to the server.
    Requires: 
]]--

function NetworkingAPI:sendmessage(msg, channel)
	reply = "Failed"
	
	if (reply == "Failed") then
		print("There was no reply from the server. Pinging the server.")
	end
	return reply
end

function NetworkingAPI:

if(not socket) then
assert(socket = require("socket"), "LuaSocket is not installed. Nice job.")
end
assert(os.execute("./python testinstall.py"), "Python is not installed. Check http://python.org/ for downloads")


setmetatable(NetworkingAPI, {
	
	__metatable = function() print("This is a locked metatable.") end
	
	__newindex = function() print("You may not extend this table.") end
	
}

Singleton = NetworkingAPI