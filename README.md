# Cryptomator
A simple program for encrypt files in sha256. The procedure is simple, you can list or encrypt every file start from a /root (instance name) directory and the cryptomator navigates and search every file in every directory linked to /root (/root is included in the navigation and file checking.
<br>
# Virtual Environment
You can use a virtualenv for possible upgrade of the program. If I want to use some specific external APIs, you can set your virtualenv downloading them in the virtual environment to rest external from your operating system.
<br>
If you want use it, you need to go inside this current directory and digits as follow:<br><br>
<code> virtualenv virtualenv </code><br><br>
<code>source virtualenv/bin/activate</code>
<br>
# Requirements
You need the last version of Python 3.x, if you want to install it:<br><br>
<b>GNU/Linux Distribution:</b><br><br>
<code>sudo apt install python3</code><br><br>
<b>MacOS Versions:</b><br><br>
<code>sudo brew install python3</code><br>
# Usage
Going inside the src directory using cd, than digit in the Terminal:<br><br>
<code>python3 core.py (root-directory) (-e for encrypt and -l for list only)</code><br>

# License
Program made by kode-git. <a href="https://github.com/kode-git/cryptomator/blob/main/LICENSE"> Apache License 2.0 </a>
