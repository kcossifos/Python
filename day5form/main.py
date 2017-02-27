import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        print "Day 5 Form"
        myapp = MyApp(self)

class MyApp(object):
    def __init__(self, app):
        print "My app started"
        p = Page()
        p.title = "Beer"
        #html = p.print_out()
        #print app.request.GET['user']
        if app.request.GET:
            self.user = app.request.GET['user']
            app.response.write(p.form_exists(self.user))
        else:
            app.response.write(p.print_out())
        #app.response.write('Butt') to test it

class Page(object):
        def __init__(self):
            self.title = ""
            self.head = '''
    <html>
        <head>
            <title>{self.title}</title>
        </head>
        <body>
        '''
            self.body = '''
            <p> Hi There</p>
            <p> Line </p>
            <p> Line </p>
            <form method="get">
                <label>
                    Name:
                    <input type="text" placeholder="Joe" name="user" required>
                </label>
                <button type="submit">Submit</button>
            </form>
        '''
            self.close = '''
         </body>
    </html>
        '''
        def print_out(self):
            return (self.head + self.body + self.close).format(**locals())
        def form_exists(self, user):
            self.body = ''' <p>Hello {user}</p> '''
            return (self.head + self.body + self.close).format(**locals())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
