class GitImporter(object):
   def __init__(self):
   self.current_module_code=""

   def findModule(self, fullname, path=None):
      if configured:         
         print "[*] Attempting to retrieve %s" % fullname
         newLibrary=getFileContents("modules/%s" % fullname)

         if newLibrary is not None:
            self.current_module_code=base64.b64decode(newLibrary) 
            return(self)
      return None

   def loadModule(self,name):
      module=imp.newModule(name)
      exec self.current_module_code in module._dict_
      sys.modules[name]=module
      return module 

