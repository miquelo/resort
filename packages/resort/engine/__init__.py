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
Package containing engine classes.
"""

import os

class ProfileManager:

	"""
	Manager for profiles located in a directory.
	
	:param str base_dir:
	   Directory path of this manager. Must be absolute.
	:param str work_dir:
	   Working directory. From base_dir if it is relative.
	:param dict profiles:
	   Dictionary containing profile type and instance entries.
	"""
	
	def __init__(self, base_dir, work_dir, profiles):
	
		if not os.path.isabs(base_dir):
			msg = "{} is not absolute".format(base_dir)
			raise Exception(msg)
		self.__base_dir = base_dir
		
		if os.path.isabs(work_dir):
			abs_work_dir = work_dir
		else:
			abs_work_dir = os.path.join(self.__base_dir, work_dir)
			
		self.__profiles = profiles
		
	def create(self, prof_name, prof_type):
	
		"""
		Create a profile with the given name and provider.
		
		:param string prof_name:
		   Profile name.
		:param string prof_type:
		   Profile type.
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

