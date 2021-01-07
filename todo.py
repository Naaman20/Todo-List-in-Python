import os.path
import sys
from datetime import datetime


def printHelp():

	
	todohelp="""Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""
	sys.stdout.buffer.write(todohelp.encode('utf8'))	
	

def addToList(ti):
	
	
	if os.path.isfile('todo.txt'):					
	    with open("todo.txt",'r') as todoFileOri:
	    	data=todoFileOri.read()
	    with open("todo.txt",'w') as todoFileMod:
	    	todoFileMod.write(ti+'\n'+data)
	else:											
	    with open("todo.txt",'w') as todoFile:
	    	todoFile.write(ti+'\n')
	print('Added todo: "{}"'.format(ti))


def showList():

	
	if os.path.isfile('todo.txt'):
	    with open("todo.txt",'r') as todoFileOri:
	    	data=todoFileOri.readlines()
	    l=len(data)
	    sl=""
	    for line in data:
	    	sl+='[{}] {}'.format(l,line)
	    	l-=1
	    sys.stdout.buffer.write(sl.encode('utf8'))			# Print the Tasks in Reverse Order in UTF-8 Encoding as the default print() generates unexpected results.
	else:
	    print ("There are no pending todos!") 


def delFromList(num):

	
	if os.path.isfile('todo.txt'):
	    with open("todo.txt",'r') as todoFileOri:
	    	data=todoFileOri.readlines()
	    l=len(data)
	    if num>l or num<=0:
	    	print(f"Error: todo #{num} does not exist. Nothing deleted.")
	    else:
	    	with open("todo.txt",'w') as todoFileMod:
	    		for line in data:
	    			if l!=num:
	    				todoFileMod.write(line)
	    			l-=1
	    	print("Deleted todo #{}".format(num))
	else:
	    print("Error: todo #{} does not exist. Nothing deleted.".format(num))


def markDone(num):

	
	if os.path.isfile('todo.txt'):
	    with open("todo.txt",'r') as todoFileOri:
	    	data=todoFileOri.readlines()
	    l=len(data)
	    if num>l or num<=0:
	    	print("Error: todo #{} does not exist.".format(num))
	    else:
	    	with open("todo.txt",'w') as todoFileMod:
	    		if os.path.isfile('done.txt'):						
	    			with open("done.txt",'r') as doneFileOri:
				    	doneData=doneFileOri.read()
			    	with open("done.txt",'w') as doneFileMod:
			    		for line in data:
			    			if l==num:
			    				doneFileMod.write("x "+datetime.today().strftime('%Y-%m-%d')+" "+line)
			    			else:
			    				todoFileMod.write(line)
			    			l-=1
			    		doneFileMod.write(doneData)
		    	else:
		    		with open("done.txt",'w') as doneFileMod:
			    		for line in data:
			    			if l==num:
			    				doneFileMod.write("x "+datetime.today().strftime('%Y-%m-%d')+" "+line)
			    			else:
			    				todoFileMod.write(line)
			    			l-=1

	    	print("Marked todo #{} as done.".format(num))
	else:
	    print("Error: todo #{} does not exist.".format(num))


def generateReport():

	# Function to Generate the Report.
	countTodo=0
	countDone=0
	if os.path.isfile('todo.txt'):
	    with open("todo.txt",'r') as todoFile:
	    	todoData=todoFile.readlines()
	    countTodo=len(todoData)
	if os.path.isfile('done.txt'):
	    with open("done.txt",'r') as doneFile:
	    	doneData=doneFile.readlines()
	    countDone=len(doneData)
	st=datetime.today().strftime('%Y-%m-%d') + " Pending : {} Completed : {}".format(countTodo,countDone)
	sys.stdout.buffer.write(st.encode('utf8'))


def main(): 

	# Main Function
	if len(sys.argv)==1:
		printHelp()
	elif sys.argv[1]=='help':
		printHelp()
	elif sys.argv[1]=='ls':
		showList()
	elif sys.argv[1]=='add':
		if len(sys.argv)>2:
			addToList(sys.argv[2])
		else:
			print("Error: Missing todo string. Nothing added!")
	elif sys.argv[1]=='del':
		if len(sys.argv)>2:
			delFromList(int(sys.argv[2]))
		else:
			print("Error: Missing NUMBER for deleting todo.")
	elif sys.argv[1]=='done':
		if len(sys.argv)>2:
			markDone(int(sys.argv[2]))
		else:
			print("Error: Missing NUMBER for marking todo as done.")
	elif sys.argv[1]=='report':
		generateReport()
	else:
		print('Option Not Available. Please use "./todo help" for Usage Information')

if __name__=="__main__": 
    main()