import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        myapp = MyApp(self)

class MyApp(object):
    def __init__(self, app):
        p = Page()
        p.title = "Final"
        if app.request.GET:
            self.name = app.request.GET['name']
            self.one = app.request.GET['one']
            self.two = app.request.GET['two']
            self.three = app.request.GET['three']
            app.response.write(p.form_exist(self.name, self.one, self.two, self.three))
        else:
            app.response.write(p.print_info())

class Page(object):
        def __init__(self):
            self.title = ""
            self.head = '''
    <!DOCTYPE html>
<html>
<head>
    <link href="/stylesheets/main.css" rel="stylesheet" type="text/css">
    <title>Final</title>
</head>
<body>
    <header>
        <div>
            <a href="#">Home</a>
        </div>
        <div>
            <a href="#">Time</a>
        </div>
        <div>
            <a href="#">Location</a>
        </div>
        <div>
            <a href="#">Contact</a>
        </div>
    </header>
        '''
            self.body = '''
    <form method="get">
        <label>Name:<br>
        <input name="name" placeholder="Kelsey" required type=
        "text"></label><br>
        <label>Number 1:<br>
        <input name="one" placeholder="1" required type=
        "number"></label><br>
        <label>Number 2:<br>
        <input name="two" placeholder="2" required
        type="number"></label><br>
        <label>Number 3:<br>
        <input name="three" placeholder="3" required type=
        "number"></label><br>
        <button class="submit">Submit</button>
    </form>
        '''
            self.close = '''
         </body>
    </html>
        '''
        def print_info(self):
            return (self.head + self.body + self.close).format(**locals())
        def form_exist(self, name, one, two, three):
            if one < two < three:
                self.body = '''
                <p id="page"><img src="stylesheets/ban.gif" alt="ban"/><br><br> Hey there, {name}! The lowest number you enter was {one}, which was your first number.
                Your second number was {two}, and your third number was {three}</p>'''
                return (self.head + self.body + self.close).format(**locals())
            elif three < one < two:
                self.body = '''
                <p id="page"><img src="stylesheets/ban.gif" alt="ban"/><br><br> Hey there, {name}! The lowest number you enter was {three}, which was your third number.
                The first number you enter was {one}, and the second number you entered was {two} </p>'''
                return (self.head + self.body + self.close).format(**locals())
            elif two < three < one:
                self.body = '''
                <p id="page"><img src="stylesheets/ban.gif" alt="ban"/><br><br> Hey there, {name}! The lowest number you enter was {two}, which was your second number.
                The first number you enter was {one}, and the third number you entered was {three} </p>'''
                return (self.head + self.body + self.close).format(**locals())
            else:
                self.body = '''
                <p id="page"><img src="stylesheets/ban.gif" alt="ban"/><br><br> Hey there, {name}! Your numbers {one}, {two}, and {three} are the same</p>'''
                return (self.head + self.body + self.close).format(**locals())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
