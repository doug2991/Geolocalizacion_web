import webapp2
from google.appengine.ext.webapp import template


class inicio(webapp2.RequestHandler):
	def get(self):
		#self.response.write(template.render("login.html",""))
		self.response.write(template.render("map.html",""))

app = webapp2.WSGIApplication([("/",inicio)],debug = True)