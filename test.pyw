#coding:utf-8

from tkinter import *
import os


#==============GLOBAL===============




#=============MAIN=============
app = Tk()

# Not allowed file to look at
exept = ['bc.pyw','af.png','db.png','dlt.png','Menu.txt','bc.pyw','test.pyw']

# List everything in the parent floder, except the not allowed file list
fold = [x for x in os.listdir('.') if x not in exept]

# Listbox for displaying folder and file
access = Listbox(app, activestyle='none',selectforeground='white',highlightthickness=0,\
					selectmode=SINGLE, height=25,exportselection =0,selectbackground='light grey')

#=============DISPLAY=============
access.grid()

# foldDic contain all the files associated 
foldDic = {}


#=============FILL LISTBOX============
for x in fold:
	# Create in foldDic the root of folder path associated with the folder/file name
	foldDic[x] = str(os.getcwd()) + "\\" + x
	x = '▲ ' + x
	# Print folder / file on listbox
	access.insert(0,x)



#============= DATA PARSING ================
# Used for read in ListBox - Return only folder/file name
def filter(string):
	badChars =['▲', '▼', ' ']
	
	# Every character in bad list
	for char in badChars:
		# While any bad character in ListBox string
		# Reset parsing every time because of 
		# decreasing len(string)

		while char in string:
			i = 0
			# Go into each char of Listbox string
			while i < len(string):
				# If we found it
				if string[i] == char:
					if i != 0:
						# Cut from 0 to bad index then from bad index +1 to end
						string = string[:i] + string[i+1:]
						# break make while i < len(string) restart
						break
					if i == 0:
						# Cut from 0+1 to the end of string
						string = string[i+1:]
						# break make while i < len(string) restart
						break
				i += 1
	return string

# If we click on listbox
def select_access(event):

	# Where do we have clicked ? ListBox index
	currentSelection = access.curselection()
	# What is displayed at this index ?
	selected = access.get(currentSelection)
	# Get file/folder name whithout undesired char
	fileSelected = filter(selected)
	# Our new line for ListBox
	text = ""
	

	def close_fold(foldPath):


		# Get from the selected listBox element to the end
		# of the listBox element
		accessTab = access.get(currentSelection,last=END)
		
		# For every content in clicked folder
		for file in os.listdir(foldPath):
			# List all the displayed files on listBox
			for i, name in enumerate(accessTab):
				# If the displayed files match the content folder
				if filter(name) == filter(file):
					

					# If foldPath content is a Folder Dictionnary key
					if file in foldDic.keys() :
						# Recall function for searching file in it
						close_fold(foldDic[file])

						# Delete from the ListBox the parsed folder
						newElementPos = currentSelection[0] + 1

					# If foldPath content is a file
					else:
						newElementPos = currentSelection[0] + i 
					
					access.delete(newElementPos)
				


	# If closed folder selected -> show content
	if '▲' in selected:
		
		# Spacing for folder content
		# basicLen is the size of path from 
		# executable root to the file we clicked on
		basicLen = len(os.getcwd().split('\\'))+1
		# pathLen is the size of the path of the clicked folder/file
		pathLen = len(foldDic[fileSelected].split('\\'))
		# 1 path folder size of difference = 1 tabulation
		i = 0
		while pathLen - i > basicLen :
			text += '    '
			i += 1

		# Replace close arrow by open arrow
		# on selected folder
		text += '▼ ' + filter(selected)
		# Delete old clicked folder
		access.delete(currentSelection)
		# Update displayed folder
		access.insert(currentSelection,text)
		
		# For every content of the folder		
		for element in os.listdir(foldDic[fileSelected]):
			# Reset text value for coming folder/file name
			text = '' 
			i = 0
			# Re-tabulate file/folder display name
			while 1 + pathLen - i > basicLen :
				text += '    '
				i += 1

			# Set the new position in listBox
			# One below the last content
			newElementPos = currentSelection[0] + 1 

			# If it's not a file
			if '.' not in element:
				# Add it to the folder dictionnary
				foldDic[element] = foldDic[fileSelected] + '\\' + element
				# Check if it's a folder
				if os.path.isdir(foldDic[element]):
					# Add the folder closed symbol
					text +=	'▲ ' + element

			# If it's a file
			else:
				# Add just the file name
				text += element

			#Put it into listBox
			access.insert(newElementPos,text)




	# If open folder selected -> hide content
	elif '▼' in selected:
		
		# Spacing for folder content
		# basicLen is the size of path from 
		# executable root to the file we clicked on
		basicLen = len(os.getcwd().split('\\'))+1
		# pathLen is the size of the path of the clicked folder/file
		pathLen = len(foldDic[fileSelected].split('\\'))
		# 1 path folder size of difference = 1 tabulation
		i = 0
		
		while pathLen - i > basicLen :
			text += '    '
			i += 1
		
		text += '▲ ' + filter(selected)
		access.delete(currentSelection)
		access.insert(currentSelection,text)

		close_fold(foldDic[fileSelected])

# When clicking on Listbox
access.bind("<<ListboxSelect>>", select_access)

app.mainloop()