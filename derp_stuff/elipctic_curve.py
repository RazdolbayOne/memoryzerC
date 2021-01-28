from fastecdsa import keys, curve,ecdsa
priv_key, pub_key = keys.gen_keypair(curve.P256)
print(priv_key)
print(pub_key)