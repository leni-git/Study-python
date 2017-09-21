# -*- coding: utf-8 -*-

import hmac, binascii
import Crypto
import Crypto.Random
from Crypto.Cipher import AES


def gen_sha256_hashed_key_salt(key):

	# Hash 중 SHA256 방식을 사용할 경우 이용할 수 있는 코드 이 경우 import hashlib을 상단에 추가해 줘야 한다.
	# salt1 = hashlib.sha256(key).digest()
	# print "salt1 len : ", str(len(salt1))
	# return hashlib.sha256(salt1+key).digest()

	# HMAC 을 사용하는 코드.
	# SHA256을 사용하는 HMAC을 생성하고 싶은 경우 hmac.new(key, message, hashlib.sha256)과 같이 코드를 작성하면 된다.
	salt1 = hmac.new(key).digest()
	return salt1


#iv 값을 랜덤으로 받아오는 코드.
def gen_random_iv():
	return Crypto.Random.OSRNG.posix.new().read(AES.block_size)


#암호화 한 문장을 해독하는 코드.
def AES256Decrypt(key, iv, cipher):
	encryptor = AES.new(gen_sha256_hashed_key_salt(key), AES.MODE_CBC, IV=iv)
	plain = encryptor.decrypt(cipher)
	plain = plain[0:-ord(plain[-1])]

	return plain


def AES256Encrypt(key, plain):

	length = AES.block_size - (len(plain) % AES.block_size)
	plain += chr(length)*length
	iv = gen_random_iv()
	encryptor = AES.new(gen_sha256_hashed_key_salt(key), AES.MODE_CBC, IV=iv)
	return {'cipher': encryptor.encrypt(plain), 'iv': iv}
	

key = 'password123qwe'
encrypted = AES256Encrypt(key, 'Let me tell you the huge secret! The king has a donkey ear')
decrypted = AES256Decrypt(key, encrypted['iv'], encrypted['cipher'])

print decrypted
