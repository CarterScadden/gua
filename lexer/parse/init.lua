require "lexer.token"

local function parse(fileContent)
    local tokens = {}
    

    -- getNextToken()
    --  lastChar = ' '
    --
    --  while isSpace(lastChar)
    --      if isEmpty do
    --          lastChar = getNextChar()
    --      else
    --          process()
    --      end
    --
    --  function process()
    --
    --      if isAlpha(lastChar)
    --          where isAlpha is
    --              regex: [a-zA-Z][a-zA-Z0-9_] ie could this be a varaible name?
    --      if is number
    --  end
    --
    -- end

    local chars = '' 
    for char in fileContent do
        if char != ' ' then
            chars += char
        else
            -- process chars
        end
    end
end

return parse
