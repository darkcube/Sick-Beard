# Author: Timothy Lusk <timothy.lusk@gmail.com>
#
# This file is part of Sick Beard.
#
# Sick Beard is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Sick Beard is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Sick Beard.  If not, see <http://www.gnu.org/licenses/>.

import cherrypy
import sickbeard

from sickbeard import logger, db
from api_objects import *

try:
    import json
except ImportError:
    from lib import simplejson as json

encoder = json.JSONEncoder()

def jsonify_tool_callback(*args, **kwargs):
    response = cherrypy.response
    response.headers['Content-Type'] = 'application/json'
    response.body = encoder.iterencode(response.body)

cherrypy.tools.jsonify = cherrypy.Tool('before_finalize', jsonify_tool_callback, priority=30)

class API_Services(object):

    @cherrypy.tools.jsonify()
    @cherrypy.expose
    def showlist(self):
        
        myDB = db.DBConnection()
        sqlResults = myDB.select("SELECT * FROM tv_shows ORDER BY show_name DESC")
        
        showList = []
        
        for curShow in sqlResults:
            
            newShow = API_TVShow()
            newShow.loadFromDB(curShow)
            
            showList.append(newShow.__dict__)
        
        return showList
    
    @cherrypy.tools.jsonify()
    @cherrypy.expose
    def show_episodes(self, showid=None, season=None):
        
        if not showid:
            return
        
        myDB = db.DBConnection()
        sqlResults = myDB.select(
            "SELECT * FROM tv_episodes WHERE showid = ? ORDER BY season*1000+episode DESC",
            [showid]
        )
        
        episodeList = []
        
        for curEpisode in sqlResults:
            
            newEpisode = API_TVEpisode()
            newEpisode.loadFromDB(curEpisode)
            
            episodeList.append(newEpisode.__dict__)
        
        return episodeList