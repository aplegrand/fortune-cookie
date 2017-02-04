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
import random

def getRandomFortune():
    #list of fortunes
    fortunes = [
    "Man who run in front of car get tired. Man who run behind car get exhausted.",
    "Man who stand on toilet is high on pot.",
    "Man who want pretty nurse must be patient.",
    "Woman who put man in doghouse will find him in cathouse."
    ]
    #randomly select a fortune
    i = random.randrange(0, len(fortunes))
    return fortunes[i]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = "<strong>" + getRandomFortune() +"</strong>"
        fort_sentence = "Your fortune: "
        fort_paragraph = "<p>" + fort_sentence + fortune + "</p>"

        lucky_number = random.randint(1,100)
        num_print = 'Your lucky number is: <strong>' + str(lucky_number) + "</strong>"
        num_paragraph = "<p>" + num_print + "</p>"

        another = '''<a href="."><button>Another cookie please!</button></a>'''

        content = header + fort_paragraph + num_paragraph + another
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
