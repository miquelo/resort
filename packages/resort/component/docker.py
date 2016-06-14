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

	def build(self, name):

		"""
		Build an image.

		:param Contextual name:
		   Image name.
		:rtype:
		   Image
		"""

		return Image(self, name)

class Image:

	"""
	Docker image. Implements :class:`Component`.

	:param docker.Endpoint endpoint:
	   Docker endpoint.
	:param Contextual name:
	   Image name.
	"""

	def __init__(self, endpoint, name):

		self.__endpoint = endpoint
		self.__name = name
