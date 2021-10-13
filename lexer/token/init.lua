local EOF_VALUE = -1

local function t(chars, token)
  return {
    value = chars,
    token = token,
  }
end

-- The lexer returns tokens [0-255] if it is an unknown character, otherwise one
-- of these for known things.
local TOKEN = {
  EOF = t(EOF_VALUE, -1),
  -- keywords 
  FUNCTION = t("def", -2),
  EXTERN = t("extern", -3),

  -- if its not a keyword, then we calculate the value after capturing the token
  -- primary
  IDENTIFIER = t(nil, -4),
  NUMBER = t(nil, -5)
}

return TOKEN 
