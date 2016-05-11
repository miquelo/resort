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

class Endpoint:

	"""
	GlassFish domain management.
	
	:param str host:
	   Endpoint host.
	:param int port:
	   Endpoint port.
	"""
	
	def __init__(self, host, port):
	
		self.__host = host
		self.__port = port
		
	def application(self, name, context_root, module_path):
	
		"""
		Domain application.
		
		:param str name:
		   Application name.
		:param str context_root:
		   Appliaction context root. May be ``None``.
		:param str module_path:
		   Module file path relative to base directory.
		:rtype:
		   Application
		:return:
		   Domain application.
		"""
		
		return Application(self, name, context_root, module_path)
		
class Application:

	"""
	Domain application. Implements :class:`Component`.
	
	:param Endpoint endpoint:
	   Domain endpoint.
	:param str name:
	   Application name.
	:param str context_root:
	   Appliaction context root. May be ``None``.
	:param str module_path:
	   Module file path relative to base directory.
	"""
	
	def __init__(self, endpoint, name, context_root, module_path):
	
		self.__endpoint = endpoint
		self.__name = name
		self.__context_root = context_root
		self.__module_path = module_path

