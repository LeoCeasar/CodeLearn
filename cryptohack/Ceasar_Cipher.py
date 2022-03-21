import string


def encoder(plaintext, step):
	c = ""
	for ch in plaintext:
		if ch.isalpha():
			s = (ord(ch) + step)
			if ch.isupper():
				if s>ord('Z'):
					s-=26
				elif s<ord('A'):
					s+=26
			else:
				if s > ord('z'):
					s -= 26
				elif s<ord('a'):
					s+=26
			c += chr(s)
		else:
			c += ch
	return c

def decoder(ciphertext, step):
	return encoder(ciphertext, step)

print("Input Number 1\n1:Encoder\n2:Decoder")
kind = int(input("Input:"))
step = int(input("Input Shift Step:"))
if kind == 1:
	text = input("plaintext:")
	print(encoder(text, -step))
elif kind == 2:
	text = input("ciphertext:")
	print(decoder(text, step))

