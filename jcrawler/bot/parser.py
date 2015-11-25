from BeautifulSoup import BeautifulSoup

""" Parse html from content object to get necessary information """
class Parser():

    @staticmethod
    def parse(content):
        Parser.find_alinks(content)

    @staticmethod
    def find_alinks(content):
        try: 
            soup = BeautifulSoup(content.html)
            for a in soup.findAll('a'):
                link = a.get('href')
                if link not in content.alinks: 
                    content.alinks.append(link)
        except TypeError:
            #Skipt
            return False
        return True

