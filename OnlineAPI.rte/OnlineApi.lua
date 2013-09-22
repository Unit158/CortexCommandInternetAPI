OnlineApi = {}

local Singleton = {};

function OnlineApi:new()
	print("This is a singleton class! You cannot make a new OnlineAPI instance, use getinstance() instead.")
end

function OnlineApi:registeractor(actor)
	
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