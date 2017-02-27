import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        myapp = MyApp(self)

class MyApp(object):
    def __init__(self, app):
        p = Page()
        p.title = "Contact Information"
        if app.request.GET:
            self.data = {
                "first": app.request.GET['first'],
                "last": app.request.GET['last'],
                "email": app.request.GET['email'],
                "phone": app.request.GET['phone'],
                "comment": app.request.GET['comment'],
                "val": app.request.GET['val']
            }

            app.response.write(p.form(self.data))
        else:
            app.response.write(p.print_all())

class Page(object):
        def __init__(self):
            self.title = ""
            self.head = '''
    <!DOCTYPE html>
<html>
<head>
    <link href="/stylesheets/main.css" rel="stylesheet" type="text/css">
    <link href='https://fonts.googleapis.com/css?family=Abel' rel='stylesheet'
    type='text/css'>
    <link href=
    'http://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css'
    rel='stylesheet prefetch'>
    <title>Contact Information</title>
</head>
<body>
    <header>
        <div class="left">
            <a href="#"><img alt="logo" src="stylesheets/rest.jpg"></a>
        </div>
        <div class="right">
            <a href="#">Home</a>
        </div>
        <div class="right">
            <a href="#">Menu</a>
        </div>
        <div class="right">
            <a href="#">Location</a>
        </div>
        <div class="right">
            <a href="#">Contact Us</a>
        </div>
    </header>
        '''
            self.body = '''
    <section>
        <h1>Contact Form</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas
        eget mi sed neque posuere imperdiet efficitur a sapien. In varius diam
        id elit pellentesque ultrices. Nullam id ultrices tortor. Suspendisse
        potenti. Duis consectetur orci quis pretium maximus. Phasellus non
        sollicitudin lectus, sit amet blandit velit. Praesent nisi urna,
        sagittis at elementum ac, blandit non nisl. Quisque aliquet lobortis
        libero. Fusce massa sem, lobortis eu erat a, fermentum interdum purus.
        Donec gravida, nibh eu pretium consectetur, mauris tellus semper magna,
        auctor aliquam mi eros in nibh. Aenean auctor ante hendrerit,
        consectetur eros et, condimentum mauris.</p>
        <p>Quisque quis nisi imperdiet, hendrerit nulla quis, varius mauris.
        Etiam pulvinar diam vitae enim convallis molestie nec ut lectus. Fusce
        vestibulum viverra arcu. Aliquam id dolor nec est porta auctor. In
        rutrum mattis erat condimentum venenatis. Ut vitae felis ornare dui
        viverra pulvinar sagittis eget enim. Cum sociis natoque penatibus et
        magnis dis parturient montes, nascetur ridiculus mus. Phasellus a
        malesuada augue.</p>
    </section>
    <form method="get">
        <label>First name:<br>
        <input name="first" placeholder="Kelsey" required="" type=
        "text"></label><br>
        <label>Last name:<br>
        <input name="last" placeholder="Smith" required="" type=
        "text"></label><br>
        <label>Email address:<br>
        <input name="email" placeholder="Kelseysmith@yahoo.com" required=""
        type="text"></label><br>
        <label>Phone number:<br>
        <input name="phone" placeholder="000-000-0000" required="" type=
        "text"></label><br>
        <label>Best time to contact:<br>
        <select name="val">
            <option value="Morning">
                Morning
            </option>
            <option value="Afternoon">
                Afternoon
            </option>
            <option value="Evening">
                Evening
            </option>
            <option value="Night">
                Night
            </option>
        </select></label><br>
        <label>Comments:<br>
        <input id="message" name="comment" required="" type="text"></label><br>
        <button class="submit"><i class="fa fa-envelope"></i>Submit</button>
    </form>
        '''
            self.close = '''
         </body>
    </html>
        '''
        def print_all(self):
            return (self.head + self.body + self.close).format(**locals())
        def form(self, data):
            self.body = '''
            <p id="newpage"><img src="stylesheets/images.jpg" alt="thanks"/><br><br>{data[first]} {data[last]} your comment "{data[comment]}" has been left, we will be contacting you either by
            {data[email]} or {data[phone]} sometime in the {data[val]}. Have a great day!</p>  '''
            return (self.head + self.body + self.close).format(**locals())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
