from passlib.context import CryptContext

class CryptService:
    def __init__(self):
        self.crypt = CryptContext(schemes=['sha256_crypt'])
    
    def encrypt(self, password)->str:
        return self.crypt.hash(password)
    
    def verify(self, password, hashed_password)->bool:
        return self.crypt.verify(password, hashed_password)

if __name__ =='__main__':
    service = CryptService()
    hash = service.encrypt('password')
    print(hash)
    result = service.verify(password='password', hashed_password=hash)
    if result == True:
        print('Password is correct')
    else:
        print('Password is incorrect')