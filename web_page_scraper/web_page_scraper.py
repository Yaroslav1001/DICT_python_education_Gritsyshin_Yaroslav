import json
from io import StringIO

# json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
# print(json.dumps("\"foo\bar"))
# print(json.dumps('\u1234'))
# print(json.dumps('\\'))
# print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))

io = StringIO('[https://api.quotable.io/quotes/-CzNrWMGIg8V]')
json.load(io)
