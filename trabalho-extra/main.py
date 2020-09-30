import os

'''
chave1:elemento1
chave2:elemento2
chave2:elemento3
chave4:elemento4
'''

class FileDict(dict):
    """
    File based dict sub-class
    filepath [str]: path to the core file of the dict
    """
    #defines the separator for all FileDict objects
    SEP = ":" 
    def __init__(self,filepath,**kwargs):
        """Constructor method"""
        #defines the variables
        try:
            self.filepath = filepath
            self.dict = {}
    
            file = open(self.filepath, 'r')
            
            file_text = file.read()
            lines = file_text.split("\n")
            
            #the doc may have a empty line, this would generate an error
            try:
                lines.remove("")
            except ValueError:
                pass
            
            for line in lines:
                try:
                    key, value = line.split(self.SEP)
                    self.dict[key] = value
                except ValueError:
                    pass
            file.close()
             
        except FileNotFoundError:
            file = open(self.filepath, "w")
            file.close()
            #print("File not found")
            pass
        
        
    def __setitem__(self, key, value):
        """Creates a new item in the dict"""
        self.dict[key] = value
    
        file = open(self.filepath, 'a')
        dict_element = str("\n" + key + ":" + value)
        file.write(dict_element)
        
        file.close()
        
    def pop(self,key):
        """Removes an item by the key"""
        
        try:
            self.dict.pop(key)
        
            file = open(self.filepath, 'w+')
            
            file.close()
            
        except KeyError:
            print("KeyError")
    
    def __del__(self):
        """Delete the dict and the file"""
        
        #os.remove(self.filepath)
        #del self
        
        

#TESTES

file_dict = FileDict("dicio.txt") # -->(1)
print(file_dict.dict)
file_dict["chave5"] = "elemento5" # -->(2)
print(file_dict.dict)
file_dict.pop('chave1') # -->(3)
print(file_dict.dict)
file_dict = FileDict("dicioo.txt")

'''
(1) Cria o dicionário
(2) Adiciona 'chave5:elemento5' ao documento e ao dicionário
(3) Remove o 'chave1:elemento1' do documento e do dicionário

'''