import curses

def get_param(prompt_string):
     screen.clear()
     screen.border(0)
     screen.addstr(2, 2, prompt_string)
     screen.refresh()
     input = screen.getstr(10, 10, 60)
     return input
	 
	 def execute_cmd(cmd_string):
     system("clear")
     a = system(cmd_string)
     print ""
     if a == 0:
          print "Command executed correctly"
     else:
          print "Command terminated with error"
     raw_input("Press enter")
     print ""
	 

myscreen = curses.initscr()

myscreen.border(0)
myscreen.addstr(12, 25, "Python curses in action")
myscreen.refresh()


x = myscreen.getch()

     if x == ord(‘1'):
	      localsystem = get_param("Is the cluster being created on a local system? yes/no")
		      if localsystem == 'no'
		          hostname = get_param("Enter the host name")
			  else
          groups = get_param("Enter comma-separated groups, eg adm,dialout,cdrom")
          shell = get_param("Enter the shell, eg /bin/bash:")
          curses.endwin()
          execute_cmd("useradd -d " + homedir + " -g 1000 -G " + groups + " -m -s " + shell + " " + username)
     elif x == ord(‘2'):
          curses.endwin()
          execute_cmd("apachectl restart")
     elif x == ord(‘3'):
          curses.endwin()
          execute_cmd("df -h")
		  
		  
curses.endwin()
