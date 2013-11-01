local Server = {name = "", port = 0}
local OnlineApi = {ServerList = {}}

function OnlineApi:new()
	print("This is a singleton class! You cannot make a new OnlineAPI instance.")
end

--[[
	Registers an AHuman with the API. Will check that the server has the same AHuman.
	Requires: An a pointer to an AHuman object
	Returns: The pointer to the api's object.
]]--

function OnlineApi:registerAHuman(AHuman)
	
end

--[[
	Registers an HDFirearm with the API. Will check that the server has the same HDFirearm.
	Requires: An a pointer to an HDFirearm object
	Returns: The pointer to the api's object.
]]--

function OnlineApi:registerHDFirearm(HDFirearm)

end

function OnlineApi:registerActor(actor)
	
end

function OnlineApi:forceupdate()
	
end

function OnlineApi:startserver(name, port)
	o = setmetatable({}, {__index = Server})
	o.name = name
	o.port = port
	self.ServerList[name] = o
	return o
end

function OnlineApi:closeserver(name)
	
end

function Server:updated(callback)
	callback()
end

function Server:close() 
	
end

setmetatable(OnlineApi, {
	
	__metatable = function() print("This is a locked metatable.") end
	
	__newindex = function() print("You may not change this table.") end
	
}
)

_G.OnlineApi = OnlineApi