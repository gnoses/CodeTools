import os
class FileTool:
    def __init__(self):
        pass

    def GetBasename(self, path):
        return os.path.basename(path)
    
    def GetParent(self, path):
        return path.split('/')[-2]
