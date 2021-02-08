#KEMAL SANLI 08.02.2021
import sqlite3, os, sys, subprocess
from tkinter import filedialog
from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title('Trophy Timestamp Fixer')
root.geometry("250x100")
root.eval('tk::PlaceWindow . center')
root.resizable(False, False)
root.iconphoto(False, tk.PhotoImage(file='icon.jpg'))



def clearConsole():
    if sys.platform == "win32":
        stream = os.system('cls')
    else:
        stream = os.popen('clear')
        output = stream.read()
        print(output)
clearConsole()

print("        Trophy Timestamp Fixer by kemalsanli")
print("                                                                ")
print("            Please Select a Database File")
print("                    ___________             ")
print("                   '._==_==_=_.'            ")
print("                   .-\:      /-.            ")
print("                  | (|:.     |) |           ")
print("                   '-|:.     |-'            ")
print("                     \::.    /              ")
print("                      '::. .'               ")
print("                        ) (                 ")
print("                      _.' '._               ")
print("                     `\"\"\"\"\"\"\"`              ")
print("                                                                ")
print("                                                                ")
print("                                                                ")
print("                                                                ")
print("                                                                ")
print("                                           github.com/kemalsanli")


def fixer(path):

    try:
        sqliteConnection = sqlite3.connect(path)
        cursor = sqliteConnection.cursor()
        totalRow=0
        print("Updating... \n")

        sqlite_update_query = """UPDATE tbl_trophy_title_entry SET time_last_update=time_last_update_uc where time_last_update=='0001-01-01T00:00:00.00Z'"""
        cursor.execute(sqlite_update_query)
        print("First Query OK {} row affected.".format(cursor.rowcount))
        totalRow=cursor.rowcount
        sqlite_update_query = """UPDATE tbl_trophy_title SET time_last_update=time_last_update_uc, time_last_unlocked=time_last_update_uc WHERE time_last_update == '0001-01-01T00:00:00.00Z' or time_last_unlocked == '0001-01-01T00:00:00.00Z'"""
        cursor.execute(sqlite_update_query)
        print("Second Query OK {} row affected.".format(cursor.rowcount))
        totalRow=totalRow+cursor.rowcount
        sqlite_update_query = """UPDATE tbl_trophy_flag SET time_unlocked=time_unlocked_uc where time_unlocked=='0001-01-01T00:00:00.00Z'"""
        cursor.execute(sqlite_update_query)
        print("Third Query OK {} row affected.\n".format(cursor.rowcount))
        totalRow=totalRow+cursor.rowcount
        sqliteConnection.commit()
        print("{} rows updated successfully \n".format(totalRow))
        sqliteConnection.commit()
        cursor.close()
        totalRow=0


    except sqlite3.Error as error:
        print("Failed to update sqlite table \n", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("Done \n")

def browsefunc():


    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select DB File",filetypes = (("DB File",".db"),("All Files",".*")))
    if os.path.exists(root.filename):
        label1.config(text='{}'.format(os.path.basename(root.filename)))
        b1.config(text="Select Another")
        clearConsole()
        fixer(root.filename)



b1=tk.Button(root,text="Select DB",font=40,command=browsefunc)
spaceLabel = tk.Label(root, text= "                     ")
label1 = tk.Label(root, text= "Please Select a DB File")
spaceLabel.pack()
label1.pack()
b1.pack()



root.mainloop()
clearConsole()
