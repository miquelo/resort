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
import subprocess

class BoxFile:

	"""
	Vagrant box from file.
	
	:param str name:
	   Box name.
	:param str image_dir:
	   Box image directory.
	"""
	
	def __init__(self, name, image_dir):
	
		self.__name = name
		self.__image_dir = image_dir
		self.__available = None
		
	def __box_list(self):
	
		args = [
			"vagrant",
			"--machine-readable",
			"box",
			"list"
		]
		proc = subprocess.Popen(args, stdout=subprocess.PIPE)
		result_entry = {}
		for line in proc.stdout.readlines():
			if len(line) > 0:
				line_split = line.decode("UTF-8").rsplit(",")
				key = line_split[2]
				value = line_split[3].strip()
				if key == "box-name":
					if len(result_entry) > 0:
						yield result_entry
						result_entry = {}
					result_entry["name"] = value
				elif key == "box-provider":
					result_entry["provider"] = value
				elif key == "box-version":
					result_entry["version"] = value
		if len(result_entry) > 0:
			yield result_entry
		proc.wait()
		
	def __path(self):
	
		for fname in os.listdir(self.__image_dir):
			if fname.endswith(".box"):
				return os.path.join(self.__image_dir, fname)
		raise Exception("Box image not found at {}".format(self.__image_dir))
		
	def available(self, context):
	
		"""
		Box is available for this user.
		"""
		
		if self.__available is None:
			avail = False
			for box in self.__box_list():
				if box["name"] == self.__name and box["version"] == "0":
					avail = True
					break
			self.__available = avail
		return self.__available
		
	def insert(self, context):
	
		"""
		Add Vagrant box to this user.
		"""
		
		args = [
			"vagrant",
			"box",
			"add",
			"--name", self.__name,
			self.__path()
		]
		subprocess.call(args)
		
	def delete(self, context):
	
		"""
		Delete Vagrant box from this user.
		"""
		
		args = [
			"vagrant",
			"box",
			"remove",
			self.__name
		]
		subprocess.call(args)

