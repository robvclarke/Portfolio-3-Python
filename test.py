class neo (object):
    health = 25
    strength = 5
    defence = 10
    agility = 1
    score = 2

character = neo()

def test(b):
   b.health = 10

test(character)

print(character.health)
#this is a primitive below

def testprimitive(a):
    a = 6

primitive = 8
testprimitive(primitive)
print(primitive)