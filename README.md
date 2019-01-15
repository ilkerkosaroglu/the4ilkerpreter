# THE-4 ilkerpreter
Interpreter designed to work through THE-4 commands.

You can:
-----
* Print the filesystem : *fs*
* list current directory items: *ls*
* check if your commands (cd, mkdir, rmdir, rm, cp, exec) work properly

All you have to do is to put ilkerpreter.py into the folder you have your the4.py . 
run it by typing "python ilkerpreter.py" in your terminal.
-----
Type 'help' to see available commands.
-----
For this tester to work, your check_commands() needs to return either of these:  
- ("ERROR",Command,WD)  
- ("SUCCESS",FS,WD)  
the interpreter doesn't actually need you to return FS. only proper WD is sufficient.
(it assumes you are changing the FS itself. It may not be correct regarding the4 regulations.)

try typing 'fs'!

Changes:  
14 Jan 2019  
Added error handling, KeyboardInterrupt and regular checks to take care of sudden crashing.
