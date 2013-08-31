local OnlineApi = {}

Singleton = {};

function OnlineApi.getinstance()
	if not Singleton then
		setmetatable(OnlineApi, {__metatable = function() print("This is a locked metatable") end}
		Singleton = OnlineApi
	end
	return Singleton
end

function OnlineApi:new()
	print("This is a singleton class! You cannot make a new OnlineAPI instance, use getinstance() instead.")
end