#!/usr/bin/env python3
"""
Installation of Unlock.
"""

import sys
import os
import pathlib
import shutil

script_name = "com.juanjonol.unlock.py"
plist_name = "com.juanjonol.unlock.plist"
script_folder = "/Library/PrivilegedHelperTools/"
plist_folder = "/Library/LaunchDaemons/"

# TODO: Add uninstaller

def main(argv=None):

	if os.getuid() != 0:
		raise PermissionError("This program must be executed as root.")

	# Generates /Library/PrivilegedHelperTools, owned by root
	script_folder_path = pathlib.Path(script_folder)
	if not script_folder_path.is_dir():
		script_folder_path.mkdir()
	os.chown(script_folder, 0, 0)

	folder_path = pathlib.Path(argv[0]).parent

	# Copies the script to /Library/PrivilegedHelperTools, being only writable by root.
	script_current_path = pathlib.Path(str(folder_path) + "/" + script_name)
	script_new = shutil.copy(str(script_current_path), script_folder)
	os.chown(script_new, 0, 0)
	os.chmod(script_new, 0o755)

	# Copies the LaunchDaemon plist to /Library/LaunchDaemon, being only writable by root.
	plist_current_path = pathlib.Path(str(folder_path) + "/" + plist_name)
	plist_new = shutil.copy(str(plist_current_path), plist_folder)
	os.chown(plist_new, 0, 0)
	os.chmod(plist_new, 0o644)

	print("Installation finished.")
	print("To add a disk, use the following command:", script_folder+script_name, "add")

if __name__ == '__main__':
	sys.exit(main(sys.argv))