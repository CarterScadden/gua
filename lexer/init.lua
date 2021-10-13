local TOKEN = require 'lexer.token'

-- create a table reading function, that will convert to json, and functions will just be "function[<address>]"

print "priting tokens..."
for i,v in pairs(TOKEN) do print(i,v) end

local function read_file(path)
    local file = io.open(path, "rb") -- r read mode and b binary mode
    if not file then return nil end
    local content = file:read "*a" -- *a or *all reads the whole file
    file:close()
    return content
end

print "reading test.gua\n-----\n"
local fileContent = read_file("test.gua")
print (fileContent)
print "---"


