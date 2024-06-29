from Crypto.Hash import SHA256
from Crypto.Publickey import RSA
from Crypto import Random

semente = Random.new().read
chaves = RSA.generate(1024,semente)
publica = chaves.publickey()
texto1 = 'estudo java'
texto2 = 'estudo Python'
hash1 = SHA256.new(texto1.encode('utf-8')).digest()
assinatura = chaves.sign(hash1)
print('Hash 1: '+ repr(hash1))
print('Assinatura Digital: '+repr(assinatura))

hash2 = SHA256.new(texto2.encode('utf-8')).digest()
print('Hash 2: '+ repr(hash2))

hash3 = SHA256.new(texto2.encode('utf-8')).digest()
print('Hash 3: '+repr(hash3))
if(publica.verify(hash2,assinatura)):
    print('Texto verdadeiro: '+ texto1)
elif(publica.verify(hash3,assinatura)):
    print('Texto verdadeiro: '+texto2)