from passlib.context import CryptContext


password_context = CryptContext(schemes = ['bcrypt'], deprecated ='auto')


class Hash:
    def bcrypt(password):
        return password_context.hash(password)
    
    def verify_password(plain_password, hash_password):
        return password_context.verify(plain_password, hash_password)