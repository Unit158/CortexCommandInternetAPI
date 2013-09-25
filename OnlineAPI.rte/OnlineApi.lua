OnlineApi = {}

local Singleton = {};

function OnlineApi:new()
	print("This is a singleton class! You cannot make a new OnlineAPI instance, use getinstance() instead.")
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

function OnlineApi:registerActor(actor)
	
end

function OnlineApi:forceupdate()
	
end



function OnlineApi:getinstance()
	return Singleton
end

setmetatable(OnlineApi, {
	
	__metatable = function() print("This is a locked metatable.") end
	
	__newindex = function() print("You may not extend this table.") end
	
}

Singleton = OnlineApi