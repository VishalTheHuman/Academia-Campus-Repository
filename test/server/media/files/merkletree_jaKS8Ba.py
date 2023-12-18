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

from hashlib import sha256
import sys

CHUNK_SIZE = 128 # Letter Chunks

class MerkleTree:
    def __init__(self,file):
        self.file = file

    def buildTree(self):
        chunks = self.makeChunks(self.file)
        leaves = [self.generateHash(chunk) for chunk in chunks]
        while len(leaves) > 1:
            new_leaves = []
            for i in range(1,len(leaves),2):
                combined = leaves[i]+ leaves[i-1]
                new_leaves.append(self.generateHash(combined))
            leaves = new_leaves + [leaves[-1]] if len(leaves)%2!=0 else new_leaves
        return leaves[-1]

    def generateHash(self,string):
        return sha256(string.encode('utf-8')).hexdigest()
    
    @staticmethod
    def verifyHashes(h1,h2):
        return h1==h2
    
    @staticmethod
    def saveFile(data,name, extension):
        with open(f"{name}.{extension}","w") as f:
            f.write(data)
            f.close()
        return f"{name}.{extension}"
        
    @staticmethod
    def validate(data, filename="server_send"):
        data = data.split("\n")
        hash_value, file_format = data[:2]
        data = "\n".join(data[2:])
        received_file = MerkleTree.saveFile(data,filename,file_format)
        print("Received Hash Value in the File: ",hash_value,"\n","Hash Value Obtained from the Data:", MerkleTree(received_file).buildTree(),sep="\n")
        return MerkleTree.verifyHashes(hash_value.strip(), MerkleTree(received_file).buildTree())
    
    @staticmethod
    def getContent(file):
        try:
            with open(file,"r") as f:
                data = f.read()
                f.close()
            return data, file.split(".")[-1] # Returns the Data, and File Extension 
        except Exception:
            sys.exit()
    
    @staticmethod
    def storeRaw(data,filename):
        with open(filename,"w") as f:
            f.write(data)
            f.close()

    def makeChunks(self,file):
        global CHUNK_SIZE
        chunks = []
        try:
            with open(file,"r") as f:
                while True:
                    chunk = f.read(CHUNK_SIZE)
                    if len(chunk) == 0:
                        return chunks
                    chunks.append(chunk)
            return chunks
        except Exception:
            sys.exit()

if __name__=="__main__":
    print(MerkleTree("sample.txt").buildTree())