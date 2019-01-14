# THE-4 ilkerpreter
Interpreter designed to work through THE-4 commands, merely a TESTER

All you have to do is to put ilkerpreter.py into the folder you have your the4.py . 
run it by typing "python ilkerpreter.py" in your terminal.
Type 'help' to see available commands.

For this tester to work, your check_commands() needs to return either of these:
-("ERROR",,WD)
-("SUCCESS",FS,WD)
the interpreter doesn't need you to return FS. WD is sufficient.
(it assumes you are changing the FS itself. It may not be correct regarding the4 regulations.)

try typing 'fs'!

Changes:
-14 Jan 2019
-Added error handling, KeyboardInterrupt and regular checks to take care of sudden crashing.
