class DH_Endpoint(object):
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None

    def generate_partial_key(self):
        partial_key = self.public_key1 ** self.private_key
        partial_key = partial_key % self.public_key2
        return partial_key

    def generate_full_key(self, partial_key_r):
        full_key = partial_key_r ** self.private_key
        full_key = full_key % self.public_key2
        self.full_key = full_key
        return full_key

    def encrypt_message(self, message):
        encrypted_message = ""
        key = self.full_key
        for c in message:
            encrypted_message += chr(ord(c) + key)
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        decrypted_message = ""
        key = self.full_key
        for c in encrypted_message:
            decrypted_message += chr(ord(c) - key)
        return decrypted_message


message = "This is a very secret message!!!"
s_public = 25626781
s_private = 211200
m_public = 24858934
m_private = 250299
Sadat = DH_Endpoint(s_public, m_public, s_private)
Michael = DH_Endpoint(s_public, m_public, m_private)

s_partial=Sadat.generate_partial_key()
print(s_partial) #147
m_partial=Michael.generate_partial_key()
print(m_partial)#66
s_full=Sadat.generate_full_key(m_partial)
Sadat.full_key=s_full

m_full=Michael.generate_full_key(s_partial)
Michael.full_key=m_full

m_encrypted=Michael.encrypt_message(message)
print(m_encrypted)

message = Sadat.decrypt_message(m_encrypted)
print(message) #'This is a very secret message!!!'