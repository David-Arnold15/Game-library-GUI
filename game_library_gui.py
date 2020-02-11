import pickle
import tkinter as tk
from tkinter import scrolledtext
TITLE_FONT=('Times New Roman', 24)
BUTTON_FONT = ('Times New Roman', 24)

"""-------------------------------------------------------------------------------------------------------------------------------------"""
class MainMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(text="Game Library", font=TITLE_FONT )
        self.lbl_title.grid(row="0", column = "0", sticky = "news")
        #Buttons
        self.btn_add = tk.Button(text="Add" , font=BUTTON_FONT)
        self.btn_add.grid(row="1", column="0")
        self.btn_edit= tk.Button(text="Edit" , font=BUTTON_FONT)
        self.btn_edit.grid(row="2", column="0")
        self.btn_search = tk.Button(text="Search" , font=BUTTON_FONT)
        self.btn_search.grid(row="3", column="0")
        self.btn_remove = tk.Button(text="Remove" , font=BUTTON_FONT)
        self.btn_remove.grid(row="4", column="0") 
        self.btn_search = tk.Button(text="Save" , font=BUTTON_FONT)
        self.btn_search.grid(row="5", column="0")
"""-------------------------------------------------------------------------------------------------------------------------------------"""
class Saved(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_success = tk.Label(text = "File Saved.", font=TITLE_FONT).grid(row="0", column="0")
        
        self.btn_ok = tk.Button(text="Ok", font=BUTTON_FONT)
        self.btn_ok.grid(row="1", column="0")
"""-------------------------------------------------------------------------------------------------------------------------------------"""
class EditChooser(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_instructions = tk.Label(text = "Which title to Edit?", font=TITLE_FONT).grid(row="0", column="0", columnspan="2")
        
        self.ent_title = tk.Entry()
        self.ent_title.grid(row="1", column="0", columnspan="2")
        
        self.btn_cancel = tk.Button(text="Cancel", font=BUTTON_FONT)
        self.btn_cancel.grid(row="2", column="0")
        self.btn_ok = tk.Button(text="Edit", font=BUTTON_FONT)
        self.btn_ok.grid(row="2", column="1")        
"""-------------------------------------------------------------------------------------------------------------------------------------"""
class RemoveChooser(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self,parent)
        self.lbl_instructions = tk.Label(text = "Which titles to Remove?", font=TITLE_FONT).grid(row="0", column="0", columnspan="2")
        
        self.ent_title = tk.Entry()
        self.ent_title.grid(row="1", column="0", columnspan="2")
        
        self.btn_cancel = tk.Button(text="Cancel", font=BUTTON_FONT)
        self.btn_cancel.grid(row="2", column="0")
        self.btn_ok = tk.Button(text="Remove", font=BUTTON_FONT)
        self.btn_ok.grid(row="2", column="1")        
"""-------------------------------------------------------------------------------------------------------------------------------------"""
class InfoFrameEntries(tk.Frame):

    def __init__(self,master):
        tk.Frame.__init__(self)    
        #--------------------------------------
        self.lbl_genre = tk.Label(text="Genre").grid(row="0", column="0")
        self.ent_genre = tk.Entry(text="Genre")
        self.ent_genre.grid(row="0", column="1")
        #---------------------------------------
        self.lbl_title = tk.Label(text="Title").grid(row="0", column="2")
        self.ent_title = tk.Entry(text="Title")
        self.ent_title.grid(row="0", column="3")
        #---------------------------------------
        self.lbl_dev = tk.Label(text="Developer").grid(row="1", column="0")
        self.ent_dev = tk.Entry(text="Developer")
        self.ent_dev.grid(row="1", column="1")    
        #---------------------------------------
        self.lbl_pub = tk.Label(text="Publisher").grid(row="1", column="2")
        self.ent_pub = tk.Entry(text="Publisher")
        self.ent_pub.grid(row="1", column="3") 
        #---------------------------------------
        self.lbl_system = tk.Label(text="System").grid(row="2", column="0")
        self.ent_system = tk.Entry(text="System")
        self.ent_system.grid(row="2", column="1")   
        #---------------------------------------
        self.lbl_release_date = tk.Label(text="Release Date").grid(row="2", column="2")
        self.ent_release_date = tk.Entry(text="Release Date")
        self.ent_release_date.grid(row="2", column="3")
        #---------------------------------------
        self.lbl_price = tk.Label(text="Price").grid(row="3", column="0")
        self.ent_price = tk.Entry(text="Price")
        self.ent_price.grid(row="3", column="1")
        #---------------------------------------
        self.lbl_purchase_date = tk.Label(text="Purchase_date").grid(row="3", column="2")
        self.ent_purchase_date = tk.Entry(text="Purchase Date")
        self.ent_purchase_date.grid(row="3", column="3")        
class InfoFrame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        #-----------------------------------------
        self.info_frame_entries = InfoFrameEntries(self)
        self.info_frame_entries.grid(row="0", column="0" ,columnspan="4")
        #-----------------------------------------
        self.ent_beat = tk.Entry()
        self.ent_beat.grid(row="1", column="0")
        self.lbl_beat = tk.Label(text="Beat it?")
        self.lbl_beat.grid(row="1", column="1")
        #-----------------------------------------
        self.lbl_players = tk.Label(text="No. of Players")
        self.lbl_players.grid(row="1", column="2")
        self.ent_players = tk.Entry()
        self.ent_players.grid(row="1", column="3")        
        
if __name__ == "__main__":
    datafile = open("game_lib.pickle" , "rb")
    library_database = pickle.load(datafile)
    datafile.close()
    maxkey = max(list(library_database.keys()))
    root = tk.Tk()
    root.title("Game Lib")
    root.geometry("500x500")
    """main_menu = MainMenu()
    main_menu.grid(row="0" , column="0" ,sticky="news")
    
    saved = Saved()
    saved.grid(row="0" , column="0" ,sticky="news")

   
    editchooser = EditChooser()
    editchooser.grid(row="0" ,column="0")
    removechooser = RemoveChooser()
    removechooser.grid(row="0" ,column="0")
    """
    info_frame= InfoFrame()
    info_frame.grid(row="0", column="0")
    root.mainloop()