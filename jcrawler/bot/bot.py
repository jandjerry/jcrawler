import content
from parser import Parser
import urllib2

""" http://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python """

class Bot(object):

    """ Constructor """
    def __init__(self, url, depth=None):
        self.url = url
        self.depth = depth
        self.discovered_urls = []
        self.downloaded_content = None


    """ This will be the function recursive and multi-threaded 
        Will be passed a filter array contains regex filters for url and content
    """
    def run(self, url_filters=[], content_filters=[]):
        c = self.download(self.url)
        if isinstance(c, content.Content): 
            Parser.parse(c)
        
            if self.depth > 0 or self.depth == None :
                for link in c.alinks :
                    crawler = Bot(link)
                    crawler.run()

    """ Download the url content and return content object """
    def download(self, url):
        c = content.Content()
        c.url = self.url

        #TODO check for caced version by hash before download it
        #TODO check the time also. Is cached version expired or not 

        try: 
            html = urllib2.urlopen(self.url).read()
            c.html = html
            print("----> [URL]Downloaded " + url)
        except ValueError as ve: 
            #Skip or TODO log 
            print("----> [URL]Skipped " + url)
            return None

        return c


    """ Validate current url  by filters TODO"""
    def url_validate(self, filters=[]):
        return true 



    """ Validate current content by filters TODO """
    def content_validate(self, filters=[]):
        return true


