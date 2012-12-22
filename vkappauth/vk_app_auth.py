# -- coding: utf-8 --
import cookielib
import urllib2
import urllib
from urlparse import urlparse
from vk_form_parser import FormParser


class VKAppAuth():
    '''
    Authorizate registred VK application by OAuth and give it access to the users data in given scope. Application
    don't use users password but access token that was only generated for this particular application.
    '''
    def auth_user(self, email, password, client_id, scope, opener):
        '''
        Authorizate user by parsing VK WAP login page with html form and filling needed parameters.
        Returns responce content and redirect url. By success you are redirected to "Receiving access rights" page
        with application authorization form. If redirect url ends with /blank.html an error occured or application
        was already authorized by user. TODO: If error and if success redirect to the same url. Find some allways
        available and small size page to redirect if success.

        See: https://vk.com/developers.php?id=-1_37230422&s=1

        Keyword arguments:
        email    -- Email of VK user gives access to the application (string)
        password -- Password of VK user gives access to the application (string)
        app_id   -- APP_ID of your VK client application (string)
        scope    -- Access rights application needs to obtain. (string/list)
                    See: https://vk.com/developers.php?oid=-17680044&p=Application_Access_Rights

        Returns: -- Content of a page you was redirected after submission of the authorization form
                    and its url. (list [content, url])
        '''
        #Get authorization page content
        response = opener.open(
            "https://oauth.vk.com/oauth/authorize?" + \
            "redirect_uri=https://oauth.vk.com/blank.html&response_type=token&" + \
            "client_id=%s&scope=%s&display=wap" % (client_id, ",".join(scope))
            )
        html = response.read()
        #Find and parse user authorization form
        parser = FormParser()
        parser.feed(html)
        parser.close()

        if not parser.form_parsed or parser.url is None or "pass" not in parser.params or \
        "email" not in parser.params:
                raise RuntimeError("Something wrong with a parser. Unable parse VK authorization form.")
        #Set forms parameters, need to be filled by user
        parser.params["email"] = email
        parser.params["pass"] = password

        if parser.method == "post":
            response = opener.open(parser.url, urllib.urlencode(parser.params))
        else:
            raise NotImplementedError("Method '%s'" % parser.params.method % " for user authorization form \
                submission is currently not supported. Please implement it if there is a need.")
        return response.read(), response.geturl()

    def give_access(self, html, opener):
        '''
        Authorizate application by parsing "Receiving access rights" page with html form and
        filling needed parameters. By success you are redirected to the url contains application
        access token. If redirect url contains query parameter with name "error" an error occur.

        See: https://vk.com/developers.php?id=-1_37230422&s=1

        Keyword arguments:
        html    -- HTML content of the "Receiving access rights" page with application authorization form.
        opener  --

        Return -- Redirect url with access token with /blank.html. (string)
        '''
        #Find and parse application authorization form
        parser = FormParser()
        parser.feed(html)
        parser.close()

        if not parser.form_parsed or parser.url is None:
                raise RuntimeError("Something wrong with a parser. Unable parse VK application authorization form.")

        if parser.method == "post":
            response = opener.open(parser.url, urllib.urlencode(parser.params))
        else:
            raise NotImplementedError("Form method '%s'" % parser.params.method + "for application authorization \
            form submission is currently not supported. Please implement it if there is a need.")

        return response.geturl()

    def auth(self, email, password, app_id, scope):
        '''Durty method.

        See: https://vk.com/developers.php?id=-1_37230422&s=1

        Keyword arguments:
        email    -- Email of VK user gives access to the application (string)
        password -- Password of VK user gives access to the application (string)
        app_id   -- APP_ID of your VK client application (string)
        scope    -- Access rights application needs to obtain. (string/list)
                    See: https://vk.com/developers.php?oid=-17680044&p=Application_Access_Rights

        Return --  Application access parameters (dict{"access_token":"", "user_id":"", "expires_in":""})
        '''

        if not isinstance(scope, list):
            scope = [scope]

        opener = urllib2.build_opener(
            urllib2.HTTPCookieProcessor(cookielib.CookieJar()),
            urllib2.HTTPRedirectHandler())

        #Authorizate user
        html, url = self.auth_user(email, password, app_id, scope, opener)

        #If application was not already once authorized
        if urlparse(url).path != "/blank.html":
            # Need to give access to requested scope
            url = self.give_access(html, opener)

        #If not success
        if urlparse(url).path != "/blank.html":
            raise RuntimeError("Bad responce from oauth server. An error occured by obtaining access_token.")

        def split_key_value(kv_pair):
            '''
            Split string by "=" in pairs

            Keyword arguments:
            kv_pair  -- String

            Return -- list with splitted strings (list)
            '''
            kv = kv_pair.split("=")
            return kv[0], kv[1]

        #Split query parameters to key, value pairs
        answer = dict(split_key_value(kv_pair) for kv_pair in urlparse(url).fragment.split("&"))
        if "access_token" not in answer or "user_id" not in answer or "expires_in" not in answer:
            raise RuntimeError("Missing access token or users id values in answer.")
        return {"access_token": answer["access_token"], "user_id": answer["user_id"], "expires_in": answer["expires_in"]}
