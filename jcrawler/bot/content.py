import hashlib
class Content():
    def __init__(self): 
        self.url = None;
        self.html = None;
        self.alinks = [];
    
    """ Hash url to unique string to be used as a key """
    def hash(self):
        m = hashlib.md5();
        m.update(self.url)
        return m;


    """ Get md5 string from hash - md5 object """
    def hash_string(self):
        return self.hash().hexdigest()
