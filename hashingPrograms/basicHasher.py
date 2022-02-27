# Define my hashing function
def hashIt( arg1 ):
	# [insert hash function logic here]
	# Does NOT have to be cryptographic standard
    result = 0
    for char in arg1:
        result = result + ord(char)
    print("Argument passed: ",arg1,"Hash result:",result)
    return result

# Declare an empty dictionary
myHashTable = {}
testUser = "MrWilson"
testPassword = "8MonsterPizza8"
myHashTable[ hashIt(testPassword) ] = testUser

# If user 'MrWilson' logs in, their password hash will need to match the username
# We've successfully prevented the need to store plaintext passwords