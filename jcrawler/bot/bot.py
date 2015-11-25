import content
from parser import Parser
import urllib2

""" http://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python """

class Bot(object):
    processed_links = []

    """ Constructor """
    def __init__(self, url, depth=None):
        #print("-->[Newround]" + url )
        self.url = url
        self.depth = depth
        self.discovered_urls = []
        self.downloaded_content = None


    """ This will be the function recursive and multi-threaded 
        Will be passed a filter array contains regex filters for url and content
    """
    def run(self, url_filters=[], content_filters=[]): 
        c = self.download(self.url, url_filters, content_filters)
        if isinstance(c, content.Content): 
            Parser.parse(c)
            if self.depth > 0 or self.depth == None :
                for link in c.alinks :
                    if link not in Bot.processed_links:
                        crawler = Bot(link)
                        crawler.depth = self.depth

                        if crawler.depth != None and crawler.depth > 0 :
                            crawler.depth = crawler.depth - 1

                        crawler.run()

    """ Download the url content and return content object """
    def download(self, url, url_filters=[], content_filters=[] ):
        if url == None or url == "": 
            return None

        if self.url_validate(url, url_filters) == False :
            return None

        print("----> [URL]Processing " + url)

        #Overall processed links
        Bot.processed_links.append(url)

        c = content.Content()
        c.url = self.url

        #TODO check for caced version by hash before download it
        #TODO check the time also. Is cached version expired or not 

        try: 
            html = urllib2.urlopen(self.url).read()
            c.html = html
            if url in c.alinks :
                c.alinks.remove(url)
            print("----> [URL]Downloaded " + url)
        except ValueError as ve: 
            #Skip or TODO log
            print("----> [URL]Skipped " + url)
            return None
        except : 
            #Skipt or TODO log
            print("----> [URL]Skipped " + url)


        return c


    """ Validate current url  by filters TODO"""
    def url_validate(self, url, filters=[]):
        print(url)
        return False



    """ Validate current content by filters TODO """
    def content_validate(self, url, filters=[]):
        return true


