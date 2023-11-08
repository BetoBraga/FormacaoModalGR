
# Execute: 
# pip install hashlib (ou pip3 install hashlib)

import hashlib

def criptoSha256(senha, chaveSecreta):
    toEncrypt = senha + chaveSecreta
    sha256 = hashlib.sha256()
    sha256.update(toEncrypt.encode('utf-8'))
    encrypted = sha256.hexdigest()
    return encrypted

def criptoSha512(senha, chaveSecreta):
    toEncrypt = senha + chaveSecreta
    sha512 = hashlib.sha512()
    sha512.update(toEncrypt.encode('utf-8'))
    encrypted = sha512.hexdigest()
    return encrypted

def criptoMd5(senha, chaveSecreta):
    toEncrypt = senha + chaveSecreta
    md5 = hashlib.md5()
    md5.update(toEncrypt.encode('utf-8'))
    encrypted = md5.hexdigest()
    return encrypted

#Chave secreta
chave_secreta = "#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista"

#Senhas
senha1 = "senha1"
senha2 = "senha2"
senha3 = "senha3"

encryptedPassword1 = criptoSha256(senha1, chave_secreta)
encryptedPassword2 = criptoSha512(senha2, chave_secreta)
encryptedPassword3 = criptoMd5(senha3, chave_secreta)
print("Senha 1 criptografada (SHA-256):", encryptedPassword1)
print("Senha 2 criptografada (SHA-512):", encryptedPassword2)
print("Senha 3 criptografada (MD5):", encryptedPassword3)
