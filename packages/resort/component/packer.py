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

class Image:

	"""
	Packer image.
	
	:param str base_dir:
	   Template base directory.
	:param str template_path:
	   Template file path relative to ``base_dir``.
	"""
	
	def __init__(self, base_dir, template_path):
	
		self.__base_dir = base_dir
		self.__template_path = template_path
		
	def available(self, context):
	
		"""
		Always return ``None``.
		"""
		
		return None

