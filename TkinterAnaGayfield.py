import tkinter as tk

root = tk.Tk()
root.title("Busy Day?")
root.geometry("500x500")
root.configure(background = "#FFFE73")
# Sets up tk window, creating a title and the dimensions of the window



def addList():
    """ Displays text from entrybox to listbox. """
    entered_text = myEntry.get()
    if entered_text:
        displayList.insert(tk.END, entered_text)
        myEntry.delete(0, tk.END)
        



# Clears the entrybox automatically after adding to display


def deleteList():
    """ Deletes last text in listbox."""
    delete_text = displayList.get(0, tk.END)
    if delete_text:
        displayList.delete(tk.END)




def clearList():
    """ Deletes all text in listbox. """
    clear_text = displayList.get(0, tk.END)
    if clear_text:
        displayList.delete(0, tk.END)

        

frame = tk.Frame(root)
frame.grid(row = 0, column = 0)
frame.configure(background = "#FFFE73")

# Creates a frame to hold to widgets


label = tk.Label(frame, text = "What Are We Doing Today?", font = ('Courier', 14, 'underline'))
label.grid(row = 0, column = 0, padx = 15, pady = 15)
label.configure(background = "#FFB973")

# Top text label

displayList = tk.Listbox(frame)
displayList.grid(row = 1, column = 0, pady = 5, columnspan = 3)

# Box for displaying list

myEntry = tk.Entry(frame)
myEntry.grid(row = 2, column = 0, columnspan = 3)

# Box for entering input

entryButton = tk.Button(frame, text = "Add", font = ('Courier', 9), fg = "#13B040", command = addList)
entryButton.grid(row = 2, column = 1, padx = (0,5))
entryButton.configure(background = "#F9E0FF")

# Button for adding to the list

deleteButton = tk.Button(frame, text = "Delete", font = ('Courier', 9), fg = "#B01335", command = deleteList)
deleteButton.grid(row = 2, column = 2)
deleteButton.configure(background = "#F9E0FF")

# Button for deleting last list item

clearButton = tk.Button(frame, text = "Clear All", font = ('Courier', 9), fg = "#1384B0", command = clearList)
clearButton.grid(row = 2, column = 3, padx = (5,0))
clearButton.configure(background = "#F9E0FF")


# Button for clearing entire list created





















root.mainloop() #Keeps window open


