""" Parse html from content object to get necessary information """
class Parser():

    @staticmethod
    def parse(content):
        Parser.find_alinks(content)

    @staticmethod
    def find_alinks(content):
        #TODO
        content.alinks.append('hix');
