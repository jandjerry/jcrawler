import urllib2
""" http://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python """

class Bot():

    """ Constructor """
    def __init__(self, url, depth):
        self.url = url
        self.depth = depth;

    """ This will be the function recursive and multi-threaded 
        Will be passed a filter array contains regex filters for url and content
    """
    def crawl(self, filters=[]):
        print("Crawling....")

    """ Download the url content """
    def download(self, url): 
        content = urllib2.urlopen(url).read()
        print(content)
        
    """ Validate current url and content by filters TODO"""
    def validate(self, filters=[]):
        return true 


