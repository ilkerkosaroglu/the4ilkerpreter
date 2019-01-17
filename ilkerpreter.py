from the4 import *

import getpass
import os,time,traceback
import copy
if os.name != 'nt':import readline
aa=os.system('del the4.pyc' if os.name == 'nt' else "rm the4.pyc")

######################
#Using default FS + test file. Change it below.
######################
FS = ["/", "d",\
["home", "D", ["the4", "d", ["the4", "D"], ["the.py", "F"]]],\
["etc", "d"],\
["tmp", "D", ["tmp.sh", "f"], ["del.txt", "F"]],\
["tst.txt","f"]\
]

c1 = ["cd home/the4/",\
"mkdir ../../home/../home///test///",\
"cd .././../home/test",\
"mkdir /home/test/the4", "cd ..//"\
]

c2 = ["cd ./home/", "cd ../etc/../tmp/test"]
#######################

def flush():
    a=os.system('cls' if os.name == 'nt' else 'clear')

def isp3():
    print "try running this in python 2, not 3"

def bye():
    print "cya."
    print ";)"

def ft(FS,WD):
    qd=[]
    ftrt=copy.deepcopy(FS)
    for i in WD.split("/"):
        qd.append(i)
    while qd[1:] and qd[1]:
        for i in ftrt[2:]:
            if i[0]==qd[1]:
                del qd[1]
                ftrt=copy.deepcopy(i)
                break
        else:
            print "WD is faulty? couldn't find the directory..:",WD
            return -1
    return ftrt,0

def prettify(Tree,space=0,prt=True):
    if prt:
        print '\033[93m'+Tree[1].lower()+'\033[0m',"*"," "*space*3,Tree[0]
    if not Tree:return space
    if prt:time.sleep(0.03)
    for node in Tree[2:]:
        prettify(node,space+1,prt)

def rmWhite(arg):
    """Removes extra whitespace"""
    s=""
    flag=0
    for i in arg:
        if i==" " and not flag:
            s+=i
            flag=1
        if i==" " and flag:
            continue
        else:
            s+=i
            flag=0
    return s

def userinp(path):
    if path!="/" and path[-1]=="/":path=path[:-1]
    inp=raw_input('\033[92m'+"%s"%(getpass.getuser())+'\033[0m'+"@interpreter:"+'\033[95m'" %s "%path+'\033[0m' +"$ " )
    inp=inp.strip(" ")
    inp=rmWhite(inp)
    return inp

def hello():
    flush()
    print '\033[5m'+"\nilkerpreter *@15 ocak 2019*\n\n"+'\033[0m'
    # print '\033[96m'+"Press enter to reload the4 whenever you update the4.py .\n"+'\033[0m' #change log: made it automatic
    print '\033[96m'+'\033[7m'+'\033[4m'+"type:"+'\033[0m'+'\033[4m'+"'help'"+'\033[0m'+'\033[96m'+"\n\npress ctrl+c or type 'quit' to quit anytime.\n\n"+'\033[0m'
    # print "Your the4 will be updated automatically when you make a change.\n*commands that you enter will be calculated additively,\n*until you refresh the commands by typing rf*"

def help():
    flush()
    print '\033[1m'+"Hello!"+'\033[0m'+" This environment was created just for you to test your homework. \nCommands like cd, mkdir, cp will try to run by your specifications."
    print "\nBare in mind that check_commands() needs to return \nthe working directory (-,-,WD) for this interpreter to work."
    print "\nIf you see me, don't forget to complain about how badly all this is written.\nThank you!"

    print '\033[4m'+"\n----------&----------"+'\033[0m'
    print "\nAll available commands:"

    print "* ls\n* fs: print the file system (prettified)\n* reload/update: reload the4.py manually (does everytime you enter a command)\n* test c1/c2\n* refresh(rf): empty the command stack\n* +{all commands specified in the4}\n* flush: clear screen\n* exit/quit/ctrl+c\n"

def interactive():
    global FS

    initFS=copy.deepcopy(FS)
    lastFS=copy.deepcopy(FS)
    queueue=[]
    path="/"
    hello()

    while True:
      try:
        inp=userinp(path)

        if True:
            import the4
            reload(the4)
            from the4 import *
            a=os.system('del the4.pyc' if os.name == 'nt' else "rm the4.pyc")

        if not inp:continue
        inp=inp.split("&&")

        if inp[0]=="help":
            help()
            continue

        if inp[0]=="update" or inp[0]=="reload":
            import the4
            reload(the4)
            from the4 import *
            a=os.system('del the4.pyc' if os.name == 'nt' else "rm the4.pyc")
            print '\033[3m'"\nthe4 reloaded successfully!"'\033[0m'
            continue

        elif inp[0]=="exit" or inp[0]=="quit" or inp[0]=="bye":
            bye()
            break

        ########################
        elif inp[0]=="autotest":
            pass # test cases go here (not implemented)
        ########################

        elif inp[0]=="pfs" or inp[0]=="fs":
            print "\nFilesystem:"
            prettify(lastFS)
            print
            continue

        elif inp[0]=="refresh" or inp[0]=="rf":
            queueue=[]
            path="/"
            FS=copy.deepcopy(initFS)
            lastFS=copy.deepcopy(FS)

            print "refreshed! type 'flush' to clear your screen"
            continue

        elif inp[0].startswith("test"):
            if inp[0]=="test":
                print "Type 'test c1' or 'test c2' to test the examples in pdf"
            else:
                try:
                    print check_commands(FS,eval(inp[0].split()[1]))
                except: print "something went wrong.. try again?"
            continue

        elif inp[0]=="flush":
            flush()
            continue

        elif inp[0]=="ls":
             ff=check_commands(FS,queueue)
             if not ff:
                 print "ls can't work. You need to return the (-,-,WD)"
             else:
                 try:
                     if type(ff[2])!=str :
                         print '\033[93m'+'\033[7m'+"!!! WD is probably a list. It must be a string.!!!"+'\033[0m'
                         raise
                     ff=ff[2]
                     rft=ft(FS,ff)
                     if path!="/": print ". ",".. ",
                     if rft!=-1:
                         for i in rft[0][2:]:
                             print i[0]," ",
                     print
                     lastFS=copy.deepcopy(FS)
                     FS=copy.deepcopy(initFS)
                     continue
                 except:
                     print "ls couldn't work. You need to return the (-,-,WD)"
                     FS=copy.deepcopy(initFS)
                     lastFS=copy.deepcopy(FS)
                     continue

        else:
            while inp:
                queueue.append(inp[0])
                del inp[0]
            final=check_commands(FS,queueue)
            bl = lastFS==FS
            lastFS = copy.deepcopy(FS)
            FS = copy.deepcopy(initFS)
            assert type(final[2])==str,'\033[93m'+'\033[7m'+"!!! WD is probably a list. It must be a string.!!!"+'\033[0m'
            if not final:
                print "Maybe you haven't implemented that thing yet? Function returned 'None'"
                blwd = None
                final = ["error"]
            else:
                blwd = final[2]==path
                path = final[2]

            print final

            if final[0].lower()=="error":
                print "***"
                print '\033[93m'+"FS , WD not changed after last command?:"+'\033[0m','\033[93m'+str(bl)+'\033[0m' if bl else '\033[91m'+str(bl)+'\033[0m',",",
                print '\033[93m'+str(blwd)+'\033[0m' if blwd else '\033[91m'+str(blwd)+'\033[0m'

                queueue.pop()
                print "It seems like check_commands() returned an error. \nContinuing from last command. \nType rf or refresh to start from the beginning."
      except KeyboardInterrupt as ki:
          print
          bye()
          exit()
      except Exception as e:
          print '\033[93m'+'\033[7m'+str(e)+'\033[0m'
          traceback.print_exc()
          time.sleep(1)
          print "continuing.."
          queueue=[]
          path="/"
          FS=copy.deepcopy(initFS)
          lastFS=copy.deepcopy(FS)
interactive()
