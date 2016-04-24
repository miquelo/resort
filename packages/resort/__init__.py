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

def setup(
	work_dir=".resort",
	profiles=None
):

	"""
	Configures a project to be managed by *resort*.
	
	:param str work_dir:
	   Path of directory were profiles will be created.
	:param dict profiles:
	   Dictionary containing profile type and instance entries.
	"""
	
	prof_mgr = engine.ProfileManager(os.getcwd(), work_dir, profiles)

