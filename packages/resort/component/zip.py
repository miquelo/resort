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

import io
import os

class File:

	def __init__(self, zip_file):
	
		self.__file = zip_file
		
	def collect(self, source_paths):
	
		return Collect(self.__file, source_paths)
		
	def extract(self, target_path):
	
		return Extract(self.__file, target_path)
		
class Collect:

	"""
	Resource set. Implements :class:`Component`.
	
	:param str source_path:
	   Path relative to base directory.
	:param str target_path:
	   Path relaltive to profile working directory.
	:param dict props:
	   Resource properties. Property with name ``context`` is reserved.
	"""
	
	def __init__(self, source_path, target_path, props):
	
		if os.path.isabs(source_path):
			msg = "Source path '{}' is absolute"
			raise Exception(msg.format(source_path))
		self.__source_path = source_path
		
		if os.path.isabs(target_path):
			msg = "Target path '{}' is absolute"
			raise Exception(msg.format(target_path))
		self.__target_path = target_path
		
		self.__props = props
		
	def __repr__(self):
	
		return "{}.{}({}, {}, {})".format(
			self.__module__,
			type(self).__name__,
			repr(self.__source_path),
			repr(self.__target_path),
			repr(self.__props)
		)
			
	def available(self, context):
	
		"""
		Return ``None``.
		
		:param resort.engine.execution.Context context:
		   Current execution context.
		"""
		
		return None
		
	def insert(self, context):
	
		"""
		Resolve resoures.
		
		:param resort.engine.execution.Context context:
		   Current execution context.
		"""
		
		in_path = os.path.join(context.base_dir(), self.__source_path)
		out_path = os.path.join(context.profile_dir(), self.__target_path)
		self.__resolve(context, in_path, out_path)
		
	def delete(self, context):
	
		"""
		Does nothing.
		
		:param resort.engine.execution.Context context:
		   Current execution context.
		"""
		
		pass

