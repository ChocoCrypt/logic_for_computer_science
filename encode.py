import base64
#aca vamos a poner el metodo de encode

def micode(stringOlista):
	a = ""
	for i in stringOlista:
		a =  a + str(i)
	encoded = base64.b64encode(a)
	print(encoded)
	return(encoded)

def midecode(encoded):
	decoded = base64.b64decode(encoded)
	print(decoded)
	return(decoded)

def hash(h):
	return(h * 3513180409 % 4000000000)

def unhash(n):
    return n * 387420489 % 4000000000


a = hash("buena perro")
print(a)
