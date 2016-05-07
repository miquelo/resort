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
		Relative path from base directory.
		
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
		Relative path from profile working directory.
		
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
		
class Availability:

	"""
	Component avaiability.
	
	:param Component comp:
	   Target component.
	"""
	
	def __init__(self, comp):
	
		self.__comp = comp
		if self.__comp is None:
			self.__get = self.__get_empty
		else:
			self.__get = self.__get_default
			
	def __get_empty(self, context):
	
		return None
		
	def __get_default(self, context):
	
		return self.__comp.available(context)
		
	def get(self, context):
	
		"""
		Availability value.
		
		:param Context context:
		   Current execution context.
		"""
		
		return self.__get(context)
		
class Plan:

	"""
	Execution plan.
	
	Could be iterated to retrieve :class:`Operation` instances.
	"""
	
	def __init__(self):
	
		self.__list = []
		
	def __iter__(self):
	
		return iter(self.__list)
		
	def insert(self, comp):
	
		"""
		Include an :class:`Insert` operation with the given component to this
		plan.
		
		:param Component comp:
		   Component.
		"""
		
		op = Insert(comp_stub)
		op.include(self.__list)
		
	def delete(self, comp):
	
		"""
		Include a :class:`Delete` operation with the given component to this
		plan.
		
		:param Component comp:
		   Component.
		"""
		
		op = Insert(comp)
		op.include(self.__list)
		
	def merge(self, plan):
	
		"""
		Include each operation of the given plan.
		
		:param Plan plan:
		   Plan to be merged.
		"""
		
		for op in plan:
			op.include(self.__list)
			
class Operation:

	"""
	Component operation.
	
	:param Component comp:
	   Target component.
	"""
	
	def __init__(self, comp):
	
		self.__comp = comp
		if self.__comp is None:
			self.__execute = self.__execute_empty
		else:
			self.__execute = self.__execute_default
			
	def __execute_empty(self, context):
	
		pass
		
	def __execute_default(self, context):
	
		self.execute_it(context)
		
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
	
	:param Component comp:
	   Component to be inserted.
	"""
	
	def __init__(self, comp):
	
		super().__init(comp)
		
	def include(self, op_list):
	
		"""
		Include this operation into given operation list.
		
		:param list op_list:
		   Operation list.
		"""
		
		pass
		
	def execute_it(self, comp, context):
	
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
	
	:param Component comp:
	   Component to be deleted.
	"""
	
	def __init__(self, comp):
	
		super().__init(comp)
		
	def include(self, op_list):
	
		"""
		Include this operation into given operation list.
		
		:param list op_list:
		   Operation list.
		"""
		
		pass
		
	def execute_it(self, comp, context):
	
		"""
		Execute delete operation.
		
		:param Component comp:
		   Target component.
		:param Context context:
		   Current context.
		"""
		
		comp.delete(context)

