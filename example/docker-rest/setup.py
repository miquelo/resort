#
# This file is part of RESORT.
#
# RESORT is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# RESORT is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with RESORT.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import resort
import resort.component
import resort.component.docker
import resort.component.maven
import resort.component.vagrant

class LocalProfile:

	def __init__(self):
	
		self.__props = {}
		
	def prepare(self, props):
	
		return self.__props
			
	def dependencies(self, comp_name):
	
		if comp_name is None:
			yield "service"
		if comp_name == "service":
			yield "container-running"
		if comp_name == "container-running":
			yield "container"
		if comp_name == "container":
			yield "machine-running"
			yield "container-image"
		if comp_name == "machine-running":
			yield "machine"
		if comp_name == "machine":
			yield "box"
		if comp_name == "box":
			yield "box-image"
		if comp_name == "box-image":
			yield "box-resources"
		if comp_name == "container-image":
			yield "module"
			
	def component(self, comp_name):
	
		return None
		
resort.setup(
	profiles={
		"local": LocalProfile()
	}
)

