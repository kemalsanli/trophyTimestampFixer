#KEMAL SANLI 08.02.2021
import sqlite3, os, sys, subprocess

def clearConsole():
    if sys.platform == "win32":
        stream = os.system('cls')
    else:
        stream = os.popen('clear')
        output = stream.read()
        print(output)

def fixer(path):
    clearConsole()
    try:
        sqliteConnection = sqlite3.connect(path)
        cursor = sqliteConnection.cursor()
        totalRow=0
        print("Updating... \n")

        sqlite_update_query = """UPDATE tbl_trophy_title_entry SET time_last_update=time_last_update_uc where time_last_update=='0001-01-01T00:00:00.00Z'"""
        cursor.execute(sqlite_update_query)
        print("First Querry OK {} row affected.".format(cursor.rowcount))
        totalRow=cursor.rowcount
        sqlite_update_query = """UPDATE tbl_trophy_title SET time_last_update=time_last_update_uc, time_last_unlocked=time_last_update_uc WHERE time_last_update == '0001-01-01T00:00:00.00Z' or time_last_unlocked == '0001-01-01T00:00:00.00Z'"""
        cursor.execute(sqlite_update_query)
        print("Second Querry OK {} row affected.".format(cursor.rowcount))
        totalRow=totalRow+cursor.rowcount
        sqlite_update_query = """UPDATE tbl_trophy_flag SET time_unlocked=time_unlocked_uc where time_unlocked=='0001-01-01T00:00:00.00Z'"""
        cursor.execute(sqlite_update_query)
        print("Third Querry OK {} row affected.\n".format(cursor.rowcount))
        totalRow=totalRow+cursor.rowcount
        sqliteConnection.commit()
        print("{} columns updated successfully \n".format(totalRow))
        sqliteConnection.commit()
        cursor.close()
        totalRow=0
        

    except sqlite3.Error as error:
        print("Failed to update sqlite table \n", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("Done \n")

fixer('trophy_local.db')