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

import configparser
import os

#
# Load project.ini
#

package_ini = configparser.ConfigParser()
package_ini.read(os.path.join(
	os.path.dirname(os.path.abspath(__file__)),
	"../../package.ini"
))

#
# General configuration
#

extensions = [
	"sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.ifconfig"
]

templates_path = [
	"_templates"
]
source_suffix = ".rst"
master_doc = "index"

project = "RESORT"
version = package_ini["project"]["version"]
release = package_ini["project"]["version"]

copyright = "2015, {}".format(package_ini["project"]["author"])
author = package_ini["project"]["author"]

language = None
exclude_patterns = []
pygments_style = "sphinx"
todo_include_todos = False
autodoc_member_order = "bysource"

#
# Options for HTML output
#

html_theme = "sphinx_rtd_theme"
html_static_path = [
	"_static"
]
htmlhelp_basename = "RESORTdoc"

#
# Options for LaTeX output
#

latex_elements = {
}
latex_documents = [
	(
		master_doc,
		"RESORT.tex",
		"RESORT Documentation",
		package_ini["project"]["author"],
		"manual"
	)
]

#
# Options for manual page output
#

man_pages = [
	(
		master_doc,
		"resort",
		"RESORT Documentation",
		[
			author
		],
		1
	)
]

#
# Options for Texinfo output
#

texinfo_documents = [
	(
		master_doc,
		"RESORT",
		"RESORT Documentation",
		author,
		"RESORT",
		"Component manager for software projects.",
		"Miscellaneous"
	)
]

#
# Other options
#

intersphinx_mapping = {
	"https://docs.python.org/3/": None
}

