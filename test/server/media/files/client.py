# 22AIE203 Data Structures and Algorithms 2
# End Semester Project - File Transfer and Validation using Merkle Tree

# Batch - B

# Members : 
# Vishal S - CB.EN.U4AIE22157
# Mounish CH - CB.EN.U4AIE22133

"""
File Format: 

<Hash Value> 
<File Format> 
<Data> 
"""

import sys
import socket
from merkletree import MerkleTree
from cryptography.fernet import Fernet 

KEY = "6tMKbjdPA1q1iic_9gvoYUb6LvlgliL0oBJyvTZbu3U="

def client(filename):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '192.168.56.1'
    port = 8000
    client_socket.connect((host, port))
    print(f"Connected to {host}:{port}\n")
    client_socket.sendall(filename.encode())
    data = client_socket.recv(10000000).decode()
    print("Data Received\nValidating the Data...\n")
    if data == "File Not Found!":
        print("File doesn't exists\n")
        sys.exit()
    MerkleTree.storeRaw(data,"client_raw.txt")
    fnet = Fernet(KEY)
    data = fnet.decrypt(data).decode()
    status = MerkleTree.validate(data, "client_recv")
    message = "File received Successfully" if status else "File Validation Failed"
    
    print("\n" + message + "\n")
    
    acknowledgment = "Received and Validated" if status else "Validation Failed"
    client_socket.sendall(acknowledgment.encode())
    
    client_socket.close()

if __name__ == "__main__":
    filename = input("Enter File Name : ")
    client(filename)