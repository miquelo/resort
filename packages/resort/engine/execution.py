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
Engine execution classes.
"""

class Plan:

	"""
	Execution plan.
	"""
	
	def __init__(self):
	
		pass
		
	def execute(self):
	
		"""
		Execute all operations of this plan.
		
		Yields events.
		"""
		
		pass
		
	def merge(self, plan):
	
		"""
		Merge this plan with the given plan.
		
		:param Plan plan:
		   Plan to be merged.
		"""
		
		pass
		
class Context:

	"""
	Execution context.
	
	:param exec_op:
	   Execution operation of type :class:`Insert` or :class:`Delete`.
	"""
	
	def __init__(self, exec_op):
	
		self.__exec_op = exec_op
		
	def next(self, exec_op):
	
		"""
		Initiates a new execution operation.
		
		:param exec_op:
		   Next execution operation of type :class:`Insert` or :class:`Delete`.
		:rtype:
		   Context
		:return:
		   New execution context based on this context.
		"""
		
		return Context(exec_op)
		
class Insert:

	"""
	Insert operation.
	
	:param ComponentStub comp_stub:
	   Stub of component to be inserted.
	"""
	
	def __init__(self, comp_stub):
	
		self.__comp_stub = comp_stub
		
	def execute(self, context):
	
		"""
		Execute insert operation.
		
		:param Context context:
		   Current execution context.
		"""
		
		pass
		
class Delete:

	"""
	Delete operation.
	
	:param ComponentStub comp_stub:
	   Stub of component to be deleted.
	"""
	
	def __init__(self, comp_stub):
	
		self.__comp_stub = comp_stub
		
	def execute(self, context):
	
		"""
		Execute delete operation.
		
		:param Context context:
		   Current execution context.
		"""
		
		pass

