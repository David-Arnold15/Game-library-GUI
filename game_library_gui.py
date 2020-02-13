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
        self.lbl_instructions = tk.Label(self, text = "Which title to Edit?", font=TITLE_FONT).grid(row="0", column="0", columnspan="2")
        
        options=["Title1", "Title2", "Title3"]
        tkvar = tk.StringVar(self)
        tkvar.set(options[0])
        self.menu_title = tk.OptionMenu(self, tkvar, *options)
        self.menu_title.grid(row="1", column="0", columnspan="2")
        
        self.btn_cancel = tk.Button(self, text="Cancel", font=BUTTON_FONT)
        self.btn_cancel.grid(self, row="2", column="0")
        self.btn_ok = tk.Button(self, text="Edit", font=BUTTON_FONT)
        self.btn_ok.grid(row="2", column="1")     
        
"""-------------------------------------------------------------------------------------------------------------------------------------"""
class RemoveChooser(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_instructions = tk.Label(self, text = "Which titles to Remove?", font=TITLE_FONT).grid(row="0", column="0", columnspan="2")
        
        options=["Title1", "Title2", "Title3"]
        tkvar = tk.StringVar(self)
        tkvar.set(options[0])
        self.menu_title = tk.OptionMenu(self, tkvar, *options)
        self.menu_title.grid(row="1", column="0", columnspan="2")
        
        self.btn_cancel = tk.Button(self, text="Cancel", font=BUTTON_FONT)
        self.btn_cancel.grid(row="2", column="0")
        self.btn_ok = tk.Button(self, text="Remove", font=BUTTON_FONT)
        self.btn_ok.grid(row="2", column="1")        
"""-------------------------------------------------------------------------------------------------------------------------------------"""
class InfoFrameEntries(tk.Frame):

    def __init__(self,parent):
        tk.Frame.__init__(self, master= parent)    
        #--------------------------------------
        self.lbl_genre = tk.Label(self, text="Genre").grid(row="0", column="0")
        self.ent_genre = tk.Entry(self, text="Genre")
        self.ent_genre.grid(row="0", column="1")
        #---------------------------------------
        self.lbl_title = tk.Label(self, text="Title").grid(row="0", column="2")
        self.ent_title = tk.Entry(self, text="Title")
        self.ent_title.grid(row="0", column="3")
        #---------------------------------------
        self.lbl_dev = tk.Label(self, text="Developer").grid(row="1", column="0")
        self.ent_dev = tk.Entry(self, text="Developer")
        self.ent_dev.grid(row="1", column="1")    
        #---------------------------------------
        self.lbl_pub = tk.Label(self, text="Publisher").grid(row="1", column="2")
        self.ent_pub = tk.Entry(self, text="Publisher")
        self.ent_pub.grid(row="1", column="3") 
        #---------------------------------------
        self.lbl_system = tk.Label(self, text="System").grid(row="2", column="0")
        self.ent_system = tk.Entry(self, text="System")
        self.ent_system.grid(row="2", column="1")   
        #---------------------------------------
        self.lbl_release_date = tk.Label(self, text="Release Date").grid(row="2", column="2")
        self.ent_release_date = tk.Entry(self, text="Release Date")
        self.ent_release_date.grid(row="2", column="3")
        #---------------------------------------
        self.lbl_price = tk.Label(self, text="Price").grid(row="3", column="0")
        self.ent_price = tk.Entry(self, text="Price")
        self.ent_price.grid(row="3", column="1")
        #---------------------------------------
        self.lbl_purchase_date = tk.Label(self, text="Purchase_date").grid(row="3", column="2")
        self.ent_purchase_date = tk.Entry(self, text="Purchase Date")
        self.ent_purchase_date.grid(row="3", column="3")      
        #--------------------------------------
        self.lbl_rating = tk.Label(self, text="Rating").grid(row="4", column="0")
        self.ent_rating = tk.Entry(self, text="Rating")
        self.ent_rating.grid(row="4", column="1")      
        #---------------------------------------
"""-------------------------------------------------------------------------------------------------------------------------------------"""
class InfoFrame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        #-----------------------------------------
        self.info_frame_entries = InfoFrameEntries(self)
        self.info_frame_entries.grid(row="0", column="0" ,columnspan="3", sticky="news")
        var1=None
        chk_beat = tk.Checkbutton(self, text='Beat it?',variable=var1, onvalue=1, offvalue=0,)
        chk_beat.grid(row="1", column="0")        
        #---------------------------------------
        options=["Single or Multiplayer?", "Single", "Multi"]
        tkvar = tk.StringVar(self)
        tkvar.set(options[0])
        self.menu = tk.OptionMenu(self, tkvar, *options)
        self.menu.grid(row="1", column="2", )
        #------------------------------------------
        self.lbl_notes = tk.Label(self, text="Notes: ").grid(row="2", column="0", sticky="w" )
        self.scr_notes = scrolledtext.ScrolledText(self, height="8",width="60",)
        self.scr_notes.grid(row="3", column="0", columnspan="3")
        #------------------------------------------
        self.btn_cancel = tk.Button(self, text="Cancel")
        self.btn_cancel.grid(row="4", column="0")
        self.btn_submit = tk.Button(self, text="Submit")
        self.btn_submit.grid(row="4", column="2")    
        #-------------------------------------------
        self.grid_columnconfigure( 0, weight="1")
        self.grid_columnconfigure( 1, weight="1")
        self.grid_columnconfigure( 2, weight="1")
class MarkedFrame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_notes = tk.Label(self, text="These items are marked for removal ").grid(row="0", column="0", columnspan = "3")
        self.scr_items = scrolledtext.ScrolledText(self, height="8",width="60", )
        self.scr_items.grid(row="1", column="0", columnspan="3")
        #------------------------------------------
        self.btn_cancel = tk.Button(self, text="Cancel")
        self.btn_cancel.grid(row="2", column="0")
        self.btn_submit = tk.Button(self, text="Submit")
        self.btn_submit.grid(row="2", column="2")        
class PrintFrameChecks(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self, master= parent)
        self.

class PrintFrame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        #-----------------------------------------
        self.lbl_search = tk.Label(self, text="Search", font=TITLE_FONT).grid(row='0', column='0', columnspan='3')
        tk.Frame.__init__(self)
        self.lbl_search_by = tk.Label(self, text="Search By").grid(row="1", column="0")
        options=["Info1", "Info2", "Info3"]
        tkvar = tk.StringVar(self)
        tkvar.set(options[0])
        self.menu_search_by = tk.OptionMenu(self, tkvar, *options)
        self.menu_search_by.grid(row="2", column="0", columnspan="2")        
        #------------------------------------------
        self.lbl_search_for = tk.Label(self, text="Search For: ").grid(row="3", column="0")
        self.ent_search_for = tk.Entry(self,)
        self.ent_search_for.grid(row="4", column="0")
        #------------------------------------------
        self.scr_info = scrolledtext.ScrolledText(self, height="8",width="60")
        self.scr_info.grid(row="5", column="0", columnspan='3')
        #------------------------------------------
        self.btn_cancel = tk.Button(self, text="Cancel")
        self.btn_cancel.grid(row="6", column="0")
        self.btn_reset = tk.Button(self, text="Reset")
        self.btn_reset.grid(row="6", column="1")
        self.btn_confirm = tk.Button(self, text="Submit")
        self.btn_confirm.grid(row="6", column="2")

if __name__ == "__main__":
    datafile = open("game_lib.pickle" , "rb")
    library_database = pickle.load(datafile)
    datafile.close()
    maxkey = max(list(library_database.keys()))
    root = tk.Tk()
    root.title("Game Lib")
    #root.geometry("500x500")
    """main_menu = MainMenu()
    main_menu.grid(row="0" , column="0" ,sticky="news")
    
    saved = Saved()
    saved.grid(row="0" , column="0" ,sticky="news")

   
    editchooser = EditChooser()
    editchooser.grid(row="0" ,column="0")
    info_frame= InfoFrame()
    info_frame.grid(row="0", column="0")
    marked_frame = MarkedFrame()
    marked_frame.grid(row="0", column="0", sticky="news")
    removechooser = RemoveChooser()
    removechooser.grid(row="0" ,column="0")
    """
    print_frame = PrintFrame()
    print_frame.grid(row="0" ,column="0")    
    root.mainloop()