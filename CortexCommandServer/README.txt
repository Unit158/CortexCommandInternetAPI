This server will re-configure stuff if you delete anything, just saying.

If you want to run this server on any other operating system than a windows-compatible
one, you must set up luasocket and lua your self! I am tired of trying to compile stuff.

About plugins:

Put .cfg files in the plugin folder.

Here is the base for the files:

FileName=example_plugin.plg
PluginName=Example Plugin
NoSandbox=false
Lua=false

The kind of files that the server will read are .cfg, .log, .py and .plg.

The .plg file is like a package. Python files are just scripts, log files are logs -
however, they can be used as saving files in sandbox mode. Cfg files are exactly what
they say they are.

You may also load new libraries if you want :P.

The other scripting language is quite simple really.

