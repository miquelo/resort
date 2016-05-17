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

from setuptools import setup, find_packages

setup(
	name="resort",
	version="0.1.1",
	
	author="RESORT Team",
	author_email="miquel.ferran.gonzalez@gmail.com",
	
	packages=find_packages("packages"),
	package_dir={
		"": "packages"
	},
	install_requires={
		"colorama>=0.3.3"
	},
	test_suite="testsuite.resort",
	
	url="http://pypi.python.org/pypi/resort_0.1.1/",
	
	license="LICENSE.txt",
	description="Component manager for software projects.",
	long_description="Read documentation at http://miquelo.github.io/resort/."
)

