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
	
	:param str prof_name:
	   Profile name.
	:param Profile prof:
	   Profile instance.
	"""
	
	def __init__(self, prof_name, prof):
	
		self.__prof_name = prof_name
		self.__prof = prof
		self.__comp_stub_reg = ComponentStubRegistry(self.__prof)
		
	def component(self, comp_name):
	
		"""
		Component with the specified name.
		
		:param str comp_name:
		   Specified component name.
		:rtype:
		   ComponentStub
		:return:
		   The component stub with the specified name.
		"""
		
		return self.__comp_stub_reg.get(comp_name)
		
	def insert_plan(self, comp_name):
	
		"""
		Prepare an insert plan for specified component.
		
		:param str comp_name:
		   Specified component name.
		:rtype:
		   execution.Plan
		:return:
		   Prepared insert plan.
		"""
		
		return None
		
	def delete_plan(self, comp_name):
	
		"""
		Prepare a delete plan all specified component.
		
		:param str comp_name:
		   Specified component name.
		:rtype:
		   execution.Plan
		:return:
		   Prepared delete plan.
		"""
		
		return None
		
	def update_plan(self, *comp_name):
	
		"""
		Prepare an update plan for all specified component.
		
		:param str comp_name:
		   Specified component name.
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
		
class ComponentStubRegistry:

	"""
	Registry of :class:`ComponentStub`.
	
	:param Profile prof:
	   Involved profile.
	"""
	
	def __init__(self, prof):
	
		self.__prof = prof
		self.__cache = {}
		
	def get(self, comp_name):
	
		"""
		Get the specified component.
		
		:param str comp_name:
		   Specified component name.
		:rtype:
		   ComponentStub
		:return:
		   Specified component stub.
		"""
		
		try:
			return self.__cache[comp_name]
		except KeyError:
			comp = self.__prof.component(comp_name)
			comp_stub = ComponentStub(self, comp_name, comp, self.__prof)
			self.__cache[comp_name] = comp_stub
			return comp_stub
			
class ComponentStub:

	"""
	Stub of a :class:`Component`.
	
	:param ComponentStubRegistry comp_stub_reg:
	   Component stub registry.
	:param str comp_name:
	   Component name.
	:param Component comp:
	   Component instance.
	:param Profile prof:
	   Owner profile.
	"""
	
	def __init__(self, comp_stub_reg, comp_name, comp, prof):
	
		self.__comp_stub_reg = comp_stub_reg
		self.__comp_name = comp_name
		self.__comp = comp
		self.__prof = prof
		
	def dependencies(self):
	
		"""
		Yield :class:`ComponentStub` of dependencies of this component.
		"""
		
		for dep_name in self.__prof.dependencies(self.__comp_name):
			yield self.__comp_stub_reg.get(dep_name)

