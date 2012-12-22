# -- coding: utf-8 --
from HTMLParser import HTMLParser


class FormParser(HTMLParser):
    '''
    Find and parse form. Get only appropriated form parameters and names, like hidden,
    text and password, url where to send filled form and method.
    '''
    def __init__(self):
        HTMLParser.__init__(self)
        #Form url
        self.url = None
        #Form params needs to be filled
        self.params = {}
        #Parser processing form right now, mean it is between <form></form> tags.
        self.in_form = False
        #Form already parsed
        self.form_parsed = False
        #Form method
        self.method = "GET"

    def handle_starttag(self, tag, attrs):
        '''
        Implement HTMLParser.handle_starttag
        Get form parameters need to be filled for successfull user authorization,
        url where to send and method.
        '''
        tag = tag.lower()

        if tag == "form":
            if self.form_parsed:
                raise RuntimeError("Second form on page.")
            if self.in_form:
                raise RuntimeError("Already in form.")
            self.in_form = True

        if not self.in_form:
            #No form found
            return
        #Get for attributes
        attrs = dict((name.lower(), value) for name, value in attrs)

        if tag == "form":
            #Save form url
            self.url = attrs["action"]
            #Get form method, for processing http request
            if "method" in attrs:
                self.method = attrs["method"]
        #Get only proper params
        elif tag == "input" and "type" in attrs and "name" in attrs:
            if attrs["type"] in ["hidden", "text", "password"]:
                self.params[attrs["name"]] = attrs["value"] if "value" in attrs else ""

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == "form":
            if not self.in_form:
                raise RuntimeError("Unexpected end of <form>.")
            self.in_form = False
            self.form_parsed = True
