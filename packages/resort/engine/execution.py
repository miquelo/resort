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

.. class:: Operation

   Execution operation.
   
   .. function:: execute(context)
   
   Execute this operation.
   
   :param execution.Context context:
      Current execution context.
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
		"""
		
		pass
		
class Insert:

	"""
	Insert operation. Implements :class:`Operation`.
	"""
	
	def __init__(self):
	
		pass
		
	def execute(self, context):
	
		"""
		Execute insert operation.
		
		:param Context context:
		   Current execution context.
		"""
		
		pass
		
class Delete:

	"""
	Delete operation. Implements :class:`Operation`.
	"""
	
	def __init__(self):
	
		pass
		
	def execute(self, context):
	
		"""
		Execute delete operation.
		
		:param Context context:
		   Current execution context.
		"""
		
		pass

