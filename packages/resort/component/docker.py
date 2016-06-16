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
	Docker endpoint.
	"""

	def __init__(self):

		pass

	def build(self, name, version, base_dir):

		"""
		Build an image.

		:param Contextual name:
		   Image name.
		:param Contextual version:
		   Image version.
		:param Contextual base_dir:
		   Base directory containing a ``Dockerfile``.
		:return:
		   Built image.
		:rtype:
		   docker.Image
		"""

		return Image(self, name, version, base_dir)
		
	def create(self, image_name, image_version, name):
	
		"""
		Create a container.
		
		:param Contextual image_name:
		   Image name.
		:param Contextual image_version:
		   Image version.
		:param Contextual name:
		   Container name.
		:return:
		   Created container.
		:rtype:
		   docker.Container
		"""
		
		return Container(self, image_name, image_version, name)
		
class Image:

	"""
	Docker image. Implements :class:`Component`.

	:param docker.Endpoint endpoint:
	   Docker endpoint.
	:param Contextual name:
	   Image name.
	:param Contextual version:
	   Image version.
	:param Contextual base_dir:
	   Base directory containing a ``Dockerfile``.
	"""
	
	def __init__(self, endpoint, name, version, base_dir):
	
		self.__endpoint = endpoint
		self.__name = name
		self.__version = version
		self.__base_dir = base_dir
		
class Container:

	"""
	Docker container. Implements :class:`Component`.

	:param docker.Endpoint endpoint:
	   Docker endpoint.
	:param Contextual image_name:
	   Image name.
	:param Contextual image_version:
	   Image version.
	:param Contextual name:
	   Container name.
	"""
	
	def __init__(self, endpoint, image_name, image_version, name):
	
		self.__endpoint = endpoint
		self.__image_name = image_name
		self.__image_version = image_version
		self.__name = name
		
	def run(self):
	
		"""
		Run a Docker container.
		
		:return:
		   The running container.
		:rtype:
		   docker.ContainerRunning
		"""
		
		return ContainerRunning(self)
		
class ContainerRunning:

	"""
	Docker container is running. Implements :class:`Component`.

	:param docker.Endpoint endpoint:
	   Docker endpoint.
	"""
	
	def __init__(self, endpoint):
	
		self.__endpoint = endpoint

