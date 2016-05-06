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

import resort.engine
import resort.engine.execution

import argparse
import colorama
import io
import os
import sys

#
# Entry point
#
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
	
	# Initialize colorama
	colorama.init()
	
	# Program name
	prog_name = sys.argv[0]
	
	# Profile manager
	prof_mgr = engine.ProfileManager(os.getcwd(), work_dir, profiles)
	
	# Retrieve arguments
	parser = argparse.ArgumentParser(
		prog=prog_name
	)
	parser.add_argument(
		"profile",
		metavar="profile",
		type=str,
		nargs=1,
		help="Profile name"
	)
	parser.add_argument(
		"command",
		metavar="command",
		type=argparse_command,
		nargs=1,
		help="Command name"
	)
	parser.add_argument(
		"arguments",
		metavar="args",
		nargs=argparse.REMAINDER,
		help="Command arguments"
	)
	args = parser.parse_args(sys.argv[1:])
	
	# Execute command
	cmd_name, cmd_fn = args.command[0]
	cmd_prog_name = "{} profile {}".format(prog_name, cmd_name)
	prof_name = args.profile[0]
	prog_args = args.arguments
	cmd_fn(cmd_prog_name, prof_mgr, prof_name, prog_args)
	
#
# Argument parser for command
#
def argparse_command(value):

	try:
		cmd_prefix = "command_"
		return (value, globals()["{}{}".format(cmd_prefix, value)])
	except:
		msg = io.StringIO()
		msg.write("unrecognized command '")
		msg.write(value)
		msg.write("'\n\nAvailable commands:\n")
		cmds = [
			(g_name[len(cmd_prefix):], globals()[g_name])
			for g_name in sorted(globals())
			if g_name.startswith(cmd_prefix)
		]
		desc_pos = 0
		for cmd_name, cmd in cmds:
			desc_pos = max(desc_pos, len(cmd_name))
		for cmd_name, cmd in cmds:
			msg.write(cmd_name.ljust(desc_pos))
			msg.write("  ")
			msg.write(cmd.__doc__.strip())
			msg.write("\n")
		msg.seek(0)
		raise argparse.ArgumentTypeError(msg.read())

#		
# Component status printer
#
def print_component_status(out, context, comp_stub, last, depth, indent,
		show_type, tree_depth):

	for indent_last in indent:
		if indent_last:
			out.write(" ")
		else:
			out.write("\u2502")
		out.write("   ")
	if last:
		out.write("\u2514")
	else:
		out.write("\u251c")
	out.write("\u2500 ")
	
	avail = comp_stub.available().get(context)
	if avail is True:
		out.write(colorama.Style.BRIGHT)
	elif avail is False:
		out.write(colorama.Style.DIM)
	out.write(comp_stub.name())
	if show_type:
		out.write(" (")
		out.write(comp_stub.type_name())
		out.write(")")
	out.write(colorama.Style.RESET_ALL)
	out.write("\n")
	
	deps = list(comp_stub.dependencies())
	new_depth = depth + 1
	new_indent = []
	new_indent.extend(indent)
	new_indent.append(last)
	for i, dep_stub in enumerate(deps):
		last = i == len(deps) - 1
		if tree_depth is None or depth <= tree_depth:
			print_component_status(out, context, dep_stub, last, new_depth,
					new_indent, show_type, tree_depth)
		
#
# Command init
#
def command_init(prog_name, prof_mgr, prof_name, prog_args):

	"""
	Initialize a profile.
	"""
	
	# Retrieve arguments
	parser = argparse.ArgumentParser(
		prog=prog_name
	)
	parser.add_argument(
		"type",
		metavar="type",
		type=str,
		nargs=1,
		help="profile type"
	)
	args = parser.parse_args(prog_args)
	
	# Profile store
	prof_type = args.type[0]
	prof_mgr.store(prof_name, prof_type)
	
#
# Command status
#
def command_status(prog_name, prof_mgr, prof_name, prog_args):

	"""
	Show status of component tree.
	"""
	
	# Retrieve arguments
	parser = argparse.ArgumentParser(
		prog=prog_name
	)
	parser.add_argument(
		"-t",
		"--type",
		required=False,
		action="store_true",
		default=False,
		dest="show_type",
		help="show component qualified class name"
	)
	parser.add_argument(
		"-d",
		"--depth",
		metavar="tree_depth",
		required=False,
		type=int,
		default=None,
		dest="tree_depth",
		help="integer value of dependency tree depth"
	)
	parser.add_argument(
		"components",
		metavar="comps",
		nargs=argparse.REMAINDER,
		help="system components"
	)
	args = parser.parse_args(prog_args)
	
	# Profile load
	prof_stub = prof_mgr.load(prof_name)
	
	# Collect component stubs
	comp_stubs = []
	if len(args.components) == 0:
		comp_stub = prof_stub.component(None)
		comp_stubs.extend(comp_stub.dependencies())
	else:
		for comp_name in args.components:
			comp_stub = prof_stub.component(comp_name)
			comp_stubs.append(comp_stub)
			
	# Print status
	show_type = args.show_type
	tree_depth = args.tree_depth
	context = prof_stub.context()
	out = io.StringIO()
	for i, comp_stub in enumerate(comp_stubs):
		last = i == len(comp_stubs) - 1
		print_component_status(out, context, comp_stub, last, 1, [], show_type,
				tree_depth)
	out.seek(0)
	sys.stdout.write(out.read())
	
#
# Command insert
#
def command_insert(prog_name, prof_mgr, prof_name, prog_args):

	"""
	Insert components.
	"""
	
	# Retrieve arguments
	parser = argparse.ArgumentParser(
		prog=prog_name
	)
	parser.add_argument(
		"components",
		metavar="comps",
		nargs=argparse.REMAINDER,
		help="system components"
	)
	args = parser.parse_args(prog_args)

