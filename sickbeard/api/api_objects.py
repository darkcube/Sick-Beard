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

import datetime

import sickbeard

from sickbeard.common import *

class API_TVShow(object):
    
    def __init__(self):
        
        self.show_id = 0
        self.tvdb_id = 0
        self.name = ""
        self.tvrid = 0
        self.tvrname = ""
        self.network = ""
        self.genre = ""
        self.runtime = 0
        self.quality = int(sickbeard.QUALITY_DEFAULT)
        self.seasonfolders = int(sickbeard.SEASON_FOLDERS_DEFAULT)

        self.status = ""
        self.airs = ""
        self.startyear = 0
        self.paused = 0
        self.air_by_date = 0
        self.absolute_numbering = 0
        
    def loadFromDB(self, databaseObject):
        
        self.show_id = databaseObject["show_id"]
        self.tvdb_id = databaseObject["tvdb_id"]
        self.name = databaseObject["show_name"]
        self.tvrname = databaseObject["tvr_name"]
        self.network = databaseObject["network"]
        self.genre = databaseObject["genre"]
        self.runtime = databaseObject["runtime"]
        self.status = databaseObject["status"]
        self.airs = databaseObject["airs"]
        self.quality = int(databaseObject["quality"])
        self.seasonfolders = int(databaseObject["seasonfolders"])
        self.paused = int(databaseObject["paused"])
        self.tvrid = int(databaseObject["tvr_id"])
        
        self.startyear = databaseObject["startyear"]
        if self.startyear == None:
            self.startyear = 0

        self.air_by_date = databaseObject["air_by_date"]
        if self.air_by_date == None:
            self.air_by_date = 0
            
        self.absolute_numbering = databaseObject["absolute_numbering"]
        if self.absolute_numbering == None:
            self.absolute_numbering = 0
        
class API_TVEpisode(object):
    
    def __init__(self):
        
        self.name = ""
        self.season = 0
        self.episode = 0
        self.absolute_episode = 0
        self.description = ""
        self.airdate = 0
        self.hasnfo = False
        self.hastbn = False
        self.status = UNKNOWN
        self.tvdbid = 0
        
    def loadFromDB(self, databaseObject):
        
        self.name = databaseObject["name"]
        self.season = databaseObject["season"]
        self.episode = databaseObject["episode"]
        self.absolute_episode = int(databaseObject["absolute_episode"])
        self.tvdbid = int(databaseObject["tvdbid"])
        self.airdate = int(databaseObject["airdate"])
        self.status = int(databaseObject["status"])
        
        self.description = databaseObject["description"]
        if self.description == None:
            self.description = ""
