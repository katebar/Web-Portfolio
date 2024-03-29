#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import logging
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        try:
            template = JINJA_ENVIRONMENT.get_template('templates/%s' % self.request.path)
            self.response.write(template.render())
        except:
            template = JINJA_ENVIRONMENT.get_template('templates/index.html')
            self.response.write(template.render())

class ContactHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
        self.response.write(template.render())
    def post(self):
        username = self.request.get('username')
        logging.info(username)
        password = self.request.get('password')
        logging.info(password)

        actual_u = "Colleen"
        actual_p = "pass"

        if username == actual_u and password == actual_p:
            template = JINJA_ENVIRONMENT.get_template('templates/about.html')
            self.response.write(template.render())
        else:
            template = JINJA_ENVIRONMENT.get_template('templates/work.html')
            self.response.write(template.render())
                    

# class IndexHandler(webapp2.RequestHandler):
#     def get(self):
#     	template = JINJA_ENVIRONMENT.get_template('templates/index.html')
#     	self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/contact.html',ContactHandler),
    ('/.*', MainHandler),
], debug=True)
