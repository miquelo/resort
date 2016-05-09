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

"""
Component execution classes.
"""

class Context:

	"""
	Execution context.
	
	:param str prof_dir:
	   Profile directory.
	"""
	
	def __init__(self, base_dir, prof_dir):
	
		self.__base_dir = base_dir
		self.__prof_dir = prof_dir
		
	def base_path(self, path):
	
		"""
		Absolute path from base directory.
		
		:path str path:
		   Relative path.
		:rtype:
		   str
		:return:
		   Absolute path from base directory of the given path.
		"""
		
		if os.path.isabs(path):
			raise Exception("Path '{}' is absolute".format(path))
		return os.path.join(self.__base_dir, path)
		
	def profile_path(self, path):
	
		"""
		Absolute path from profile working directory.
		
		:path str path:
		   Relative path.
		:rtype:
		   str
		:return:
		   Absolute path from profile working directory of the given path.
		"""
		
		if os.path.isabs(path):
			raise Exception("Path '{}' is absolute".format(path))
		return os.path.join(self.__prof_dir, path)
		
class Operation:

	"""
	Component operation.
	
	:param str name:
	   Target component name.
	:param Component comp:
	   Target component. May be ``None``.
	"""
	
	def __init__(self, name, comp):
	
		self.__name = name
		self.__comp = comp
		if self.__comp is None:
			self.__execute = self.__execute_empty
		else:
			self.__execute = self.__execute_default
			
	def __eq__(self, other):
	
		return type(self) == type(other) and self.__name == other.__name
		
	def __ne__(self, other):
	
		return type(self) != type(other) or self.__name != other.__name
		
		
	def __repr__(self):
	
		return "{}.{}({}, {})".format(
			self.__module__,
			type(self).__name__,
			repr(self.__name),
			repr(self.__comp)
		)
		
	def __execute_empty(self, context):
	
		pass
		
	def __execute_default(self, context):
	
		self.execute_impl(self.__comp, context)
		
	def name(self):
	
		"""
		Component name.
		
		:rtype:
		   str
		"""
		
		return self.__name
		
	def execute(self, context):
	
		"""
		Execute operation.
		
		:param Context context:
		   Current execution context.
		"""
		
		self.__execute(context)
		
class Insert(Operation):

	"""
	Insert operation.
	
	:param str name:
	   Component name.
	:param Component comp:
	   Component to be inserted.
	"""
	
	def __init__(self, name, comp):
	
		super().__init__(name, comp)
		
	def execute_impl(self, comp, context):
	
		"""
		Execute insert operation.
		
		:param Component comp:
		   Target component.
		:param Context context:
		   Current context.
		"""
		
		comp.insert(context)
		
class Delete(Operation):

	"""
	Delete operation.
	
	:param str name:
	   Component name.
	:param Component comp:
	   Component to be deleted.
	"""
	
	def __init__(self, name, comp):
	
		super().__init__(name, comp)
		
	def execute_impl(self, comp, context):
	
		"""
		Execute delete operation.
		
		:param Component comp:
		   Target component.
		:param Context context:
		   Current context.
		"""
		
		comp.delete(context)

