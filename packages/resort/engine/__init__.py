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

import configparser
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
			self.__work_dir = work_dir
		else:
			self.__work_dir = os.path.join(self.__base_dir, work_dir)
			
		self.__profiles = profiles or {}
		
	def __profile_stub(self, prof_name, prof_type, prof_dir):
	
		try:
			prof = self.__profiles[prof_type]
			return ProfileStub(self.__base_dir, prof_name, prof, prof_dir)
		except KeyError:
			msg = "Profile of type '{}' does not exist"
			raise Exception(msg.format(prof_type))
			
	def __profile_dir(self, prof_name):
	
		return os.path.join(self.__work_dir, prof_name)
		
	def __profile_ini_path(self, prof_dir):
	
		return os.path.join(prof_dir, "profile.ini")
		
	def load(self, prof_name):
	
		"""
		Load the profile with the given name.
		
		:param str prof_name:
		   Profile name.
		:rtype:
		   ProfileStub
		:return:
		   An stub to loaded profile.
		"""
		
		prof_dir = self.__profile_dir(prof_name)
		prof_ini_path = self.__profile_ini_path(prof_dir)
		if not os.path.exists(prof_ini_path):
			msg = "Profile '{}' does not exist"
			raise Exception(msg.format(prof_name))
			
		# Load profile
		prof_ini_file = open(prof_ini_path, "r")
		prof_ini = configparser.ConfigParser()
		prof_ini.read_file(prof_ini_file)
		prof_ini_file.close()
		
		# Prepare profile
		prof_type = prof_ini["profile"]["type"]
		prof_stub = self.__profile_stub(prof_name, prof_type, prof_dir)
		prof_stub.prepare(prof_ini["properties"])
		
		return prof_stub
		
	def store(self, prof_name, prof_type):
	
		"""
		Store a profile with the given name and type.
		
		:param str prof_name:
		   Profile name.
		:param str prof_type:
		   Profile type.
		"""
		
		prof_dir = self.__profile_dir(prof_name)
		prof_stub = self.__profile_stub(prof_name, prof_type, prof_dir)
		if not os.path.exists(prof_dir):
			os.makedirs(prof_dir)
		prof_ini_path = self.__profile_ini_path(prof_dir)
		
		# Load previous properties
		if os.path.exists(prof_ini_path):
			prof_ini_file = open(prof_ini_path, "r")
			prof_ini = configparser.ConfigParser()
			prof_ini.read_file(prof_ini_file)
			prof_ini_file.close()
			prev_props = prof_ini["properties"]
		else:
			prev_props = {}
			
		# Prepare and store profile
		prof_ini = configparser.ConfigParser()
		prof_ini["profile"] = {}
		prof_ini["profile"]["type"] = prof_type
		prof_ini["properties"] = prof_stub.prepare(prev_props)
		prof_ini_file = open(prof_ini_path, "w")
		prof_ini.write(prof_ini_file)
		prof_ini_file.close()
		
class ProfileStub:

	"""
	Stub of a :class:`Profile`.
	
	:param str prof_name:
	   Profile name.
	:param Profile prof:
	   Profile instance.
	:param str prof_dir:
	   Profile working directory.
	"""
	
	def __init__(self, base_dir, prof_name, prof, prof_dir):
	
		self.__base_dir = base_dir
		self.__prof_name = prof_name
		self.__prof = prof
		self.__prof_dir = prof_dir
		self.__comp_stub_reg = ComponentStubRegistry(self.__prof)
		
	def context(self):
	
		"""
		Create an exectution context.
		
		:rtype:
		   execution.Context
		:return:
		   The created execution context.
		"""
		
		return execution.Context(self.__base_dir, self.__prof_dir)
		
	def prepare(self, props):
	
		"""
		Prepare stubbed profile and return its properties.
		
		:param dict props:
		   Dictionary with previous properties.
		:rtype:
		   dict
		:return:
		   Properties dictionary.
		"""
		
		return self.__prof.prepare(props)
		
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
		Prepare a delete plan for specified component.
		
		:param str comp_name:
		   Specified component name.
		:rtype:
		   execution.Plan
		:return:
		   Prepared delete plan.
		"""
		
		return None
		
	def update_plan(self, comp_name):
	
		"""
		Prepare an update plan for specified component.
		
		:param str comp_name:
		   Specified component name.
		:rtype:
		   execution.Plan
		:return:
		   Prepared update plan.
		"""
		
		return None
		
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
			comp_stub = ComponentStub(self, comp_name, self.__prof)
			self.__cache[comp_name] = comp_stub
			return comp_stub
			
class ComponentStub:

	"""
	Stub of a :class:`Component`.
	
	:param ComponentStubRegistry comp_stub_reg:
	   Component stub registry.
	:param str comp_name:
	   Component name.
	:param Profile prof:
	   Owner profile.
	"""
	
	def __init__(self, comp_stub_reg, comp_name, prof):
	
		self.__comp_stub_reg = comp_stub_reg
		self.__comp_name = comp_name
		self.__comp_inst = None
		self.__comp = self.__comp_empty
		self.__prof = prof
		
	def __comp_empty(self):
	
		self.__comp_inst = self.__prof.component(self.__comp_name)
		if self.__comp_inst is None:
			self.__comp_inst = ComponentEmpty()
		self.__comp = self.__comp_filled
		return self.__comp_inst
		
	def __comp_filled(self):
	
		return self.__comp_inst
		
	def name(self):
	
		"""
		Return component name.
		
		:rtype:
		   str
		:return:
		   Component name.
		"""
		
		return self.__comp_name
		
	def type_name(self):
	
		"""
		Fully qualified name of component class.
		
		:rtype:
		   str
		"""
		
		return "{}.{}".format(
			self.__comp_inst.__module__,
			self.__comp_inst.__class__.__name__
		)
		
	def dependencies(self):
	
		"""
		Yield :class:`ComponentStub` of dependencies of this component.
		"""
		
		try:
			for dep_name in self.__prof.dependencies(self.__comp_name):
				yield self.__comp_stub_reg.get(dep_name)
		except TypeError:
			yield from ()
			
	def available(self, context):
	
		"""
		Check stubbed component is available.
		
		:param execution.Context context:
		   Execution context.
		:rtype:
		   bool
		:return:
		   Stubbed component availability.
		"""
		
		return self.__comp().available(context)
		
	def insert(self, context):
	
		"""
		Insert stubbed component.
		
		:param execution.Context context:
		   Execution context.
		"""
		
		self.__comp().insert(context)
		
	def delete(self, context):
	
		"""
		Delete stubbed component.
		
		:param execution.Context context:
		   Execution context.
		"""
		
		self.__comp().delete(context)
		
class ComponentEmpty:

	"""
	Empty :class:`Component` implementation.
	"""
	
	def available(self, context):
	
		"""
		Return ``None``.
		"""
		
		return None
		
	def insert(self, context):
	
		"""
		Does nothing.
		"""
		
		pass
		
	def delete(self, context):
	
		"""
		Does nothing.
		"""
		
		pass

