import random 
import os 

def encrypt(msg, key):
    return bytes(a ^ b for a, b in zip(msg, key))

def xor_secure(keys, msg):
    result = msg

    for key in keys:
        result = encrypt(result, key)
    
    return result
key1 = bytearray. fromhex("d11f5c4991188186d7666b6cf1b09231a63c1b5042ee42cae4780e9f519df447f7dc8266d2ad29b4557b1fe9") 
key2 = bytearray. fromhex("3cf2b5be58edc7e3c48bdf3007b3be54abc3f78369f673e8e0cb051302f0903cbe839b043cd56b1eab1393d0") 
key3 = bytearray. fromhex("4141414141414141414141414141414141414141414141414141414141414141414141414141414141414141") 
key4 = bytearray. fromhex("96d65d1a24429926cc44762d86d71ddfbdd774a1da9be1bf152ca5d4bb1afda93dd11a0e9159a17923b5a677") 
enc_msg = bytearray. fromhex("7929c79d9cc1e54faabbf70363ca409dae08975081f1ff880fa6df4bf642ebd07da1735c4b53d1b3bdbd4a72")
enc_msg = xor_secure([key1,key2,key3,key4],enc_msg)
msg = enc_msg.decode()
print(msg)


