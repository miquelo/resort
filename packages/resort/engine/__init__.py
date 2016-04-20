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
Package containing engine classes.

.. class:: Profile

   Specific layout of components.
   
   .. function:: dependencies(comp_name)
   
      Yields dependency component names of the specified component.
      
      :param string comp_name:
         Name of the specified component.
         
   .. function:: definition(comp_name)
   
      Definition of the specified component.
      
      :param string comp_name:
         Name of the specified component.
      :rtype:
         Component
         
.. class:: Component

   Definition of a component.
   
   .. function:: available()
   
      Check this component is available.
      
      Return True if it is available or False otherwise. But it can also return
      None if availability is not known or it is not relevant.
      
      :rtype:
         bool
      :return:
         Component availability.
   
   .. function:: insert(context)
   
      Insert this component.
      
      :param execution.Context context:
         Current execution context.
         
   .. function:: delete(context)
   
      Delete this component.
      
      :param execution.Context context:
         Current execution context.
"""

class ProfileManager:

	"""
	Manager for profiles located in a directory.
	
	:param str base_dir:
	   Directory path of this manager.
	:param str work_dir:
	   Work directory.
	"""
	
	def __init__(self, base_dir):
	
		if not os.path.isabs(base_dir):
			msg = "{} is not absolute".format(base_dir)
			raise Exception(msg)
			
		# XXX Project must have resort directory. It creates unversioned...
		# ... work directory and optionally has extension directory with...
		# ... versioned contents
		
		self.__base_dir = base_dir
		
	def create(self, prof_name, prof_type):
	
		"""
		Create a profile with the given name and provider.
		
		:param string prof_name:
		   Profile name.
		:param string prov_name:
		   Name of profile provider.
		:rtype:
		   ProfileStub
		:return:
		   An stub to created profile.
		"""
		
		pass
		
	def load(self, prof_name):
	
		"""
		Load the profile with the given name.
		
		:param string prof_name:
		   Profile name.
		:rtype:
		   ProfileStub
		:return:
		   An stub to loaded profile.
		"""
		
		pass
		
class ProfileStub:

	"""
	Stub of a :class:`Profile`.
	"""
	
	def __init__(self):
	
		pass
		
	def insert_plan(self, *comp_name):
	
		"""
		Prepare an insert plan for all specified component.
		
		:param list comp_name:
		   Specified component names.
		:rtype:
		   execution.Plan
		:return:
		   Prepared insert plan.
		"""
		
		return None
		
	def delete_plan(self, *comp_name):
	
		"""
		Prepare a delete plan for all specified component.
		
		:param list comp_name:
		   Specified component names.
		:rtype:
		   execution.Plan
		:return:
		   Prepared delete plan.
		"""
		
		return None
		
	def update_plan(self, *comp_name):
	
		"""
		Prepare an update plan for all specified component.
		
		:param list comp_name:
		   Specified component names.
		:rtype:
		   execution.Plan
		:return:
		   Prepared update plan.
		"""
		
		return None
		
	def store(self):
	
		"""
		Store this profile.
		"""
		
		pass

