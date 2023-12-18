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

import os
import socket
from merkletree import MerkleTree
from cryptography.fernet import Fernet 

KEY = "6tMKbjdPA1q1iic_9gvoYUb6LvlgliL0oBJyvTZbu3U="

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostbyname(socket.gethostname())
    port = 8000
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}\n")
        file_path = client_socket.recv(1024).decode()
        if not os.path.exists(file_path):
            client_socket.sendall("File Not Found!".encode())
            client_socket.close()
            continue
        file_content, file_extension = MerkleTree.getContent(file_path)
        hash_value = MerkleTree(file_path).buildTree()
        data = f"{hash_value}\n{file_extension}\n{file_content}"
        fnet = Fernet(KEY)
        MerkleTree.storeRaw(fnet.encrypt(data.encode()).decode(),"server_raw.txt")
        MerkleTree.validate(data)
        print("Sending Data...\n")
        client_socket.sendall(fnet.encrypt(data.encode()))
        
        acknowledgment = client_socket.recv(1024).decode()
        print(f"Received from client: {acknowledgment}\n")

        client_socket.close()

if __name__ == "__main__":
    server()