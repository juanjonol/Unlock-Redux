# Unlock Redux

https://github.com/juanjonol/Unlock-Redux

Based on Unlock (https://github.com/jridgewell/unlock).

## Description

Unlock allows the system to unlock and mount Core Storage (HFS+) or APFS encrypted volumes during boot. In other words, this allows you to log in as a user whose home directory is on an encrypted secondary disk, partition or volume without any problems.

## Usage

- Python 3 must be installed in /usr/local/bin/python3.
- Download this repository as a ZIP.
- In Terminal, move to the folder with this files using the “cd” command.
- Type the next command:
	`sudo install.py`
- Use this command to add disks:
	`sudo /Library/PrivilegedHelperTools/com.juanjonol.unlock.py add`

## Uninstall

Simply run `sudo install.py -u`.

## Differences with Unlock

- Unlock is a Objective-C project. I think this is better suited as a Python script.
- Unlock standard installation consists of downloading binaries from Internet using curl, [something that I don’t recommend.][1]
- Unlock requires Internet access for its standard installation.
- Unlock doesn’t have a non-interactive mode, useful for automation.
- Unlock doesn't support APFS.
- Unlock doesn't check that the password is correct before saving it.
- [Unlock-Redux doesn't use the macOS Keychain to save the passwords][3].

## Support

If you have a problem, create an [issue][2]. Pull request are welcome.

[1]:	http://curlpipesh.tumblr.com
[2]:	https://github.com/juanjonol/Unlock-Redux/issues
[3]:	https://github.com/juanjonol/Unlock-Redux/issues/8