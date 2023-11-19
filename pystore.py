import json
import time

OpenStores = dict()

class Store():
    def __init__(self, name:str):
        FILE_NAME = name+"_pys.json"
        self.FILE_NAME = FILE_NAME
        self.IsOpen = True
         
        if not FILE_NAME in OpenStores:
            OpenStores[FILE_NAME] = self
            
            try: 
                with open(FILE_NAME) as f:
                    self.Cache = json.load(f)
            except FileNotFoundError:
                with open(FILE_NAME, "w+") as f:
                    self.Cache = dict()
                
            if not "Meta" in self.Cache:
                self.Cache["Meta"] = {
                    "TIME_CREATED": time.time(),
                    "LastTimeEdited": time.time(),
                    "LastTimeSaved": -1
                }
                self.Cache["Store"] = dict()
        else:
            return OpenStores[self.FILE_NAME]
    def saveStore(self):
        if self.IsOpen:
            self.Cache["Meta"]["LastTimeSaved"] = time.time()
            with open(self.FILE_NAME, "w") as f:
                json.dump(self.Cache, f)
    def close(self):
        if self.IsOpen:
            self.saveStore()
            self.IsOpen = False
            del OpenStores[self.FILE_NAME]
            del self.Cache
    def setElement(self, key:str, value):
        if self.IsOpen:
            self.Cache["Store"][key] = value
            self.Cache["Meta"]["LastTimeEdited"] = time.time()
    def hasElement(self, key:str):
        return key in self.Cache["Store"]
    def getElement(self, key:str):
        if self.IsOpen:
            return self.Cache["Store"][key]
    def deleteElement(self, key:str):
        if self.IsOpen:
            del self.Cache["Store"][key]
            self.Cache["Meta"]["LastTimeEdited"] = time.time()            
