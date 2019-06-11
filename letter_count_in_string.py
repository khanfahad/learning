import pprint
message = "A quick brown fox jumps over the lazy dog"
count = {}
for character in message.upper():
    count.setdefault(character, 0)
    count[character] += 2

pprint.pprint(count)
