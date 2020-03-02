import pickle
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox as mb
TITLE_FONT=('Times New Roman', 24)
BUTTON_FONT = ('Times New Roman', 24)
class Screen(tk.Frame):
    current=0
    def __init__(self):
        tk.Frame.__init__(self)
    def switch_frame():
        screens[Screen.current].tkraise()
       
"""-------------------------------------------------------------------------------------------------------------------------------------"""
class MainMenu(Screen):
    
    
    def __init__(self):
        
        Screen.__init__(self)
        self.lbl_title = tk.Label(self, text="Game Library", font=TITLE_FONT )
        self.lbl_title.grid(row="0", column = "1", sticky = "news")
        #Buttons
        self.btn_add = tk.Button(self, text="Add" , font=BUTTON_FONT, command=self.go_add)
        self.btn_add.grid(row="1", column="1")
        self.btn_edit= tk.Button(self, text="Edit" , font=BUTTON_FONT, command=self.go_edit)
        self.btn_edit.grid(row="2", column="1")
        self.btn_search = tk.Button(self, text="Search" , font=BUTTON_FONT, command=self.go_print)
        self.btn_search.grid(row="3", column="1")
        self.btn_remove = tk.Button(self, text="Remove" , font=BUTTON_FONT, command=self.go_remove)
        self.btn_remove.grid(row="4", column="1") 
        self.btn_search = tk.Button(self, text="Save" , font=BUTTON_FONT, command=self.go_save)
        self.btn_search.grid(row="5", column="1")
        
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        
        self.grid_rowconfigure(0, weight = 3)
        self.grid_rowconfigure(1, weight = 1)
        self.grid_rowconfigure(2, weight = 1)
        self.grid_rowconfigure(3, weight = 1)
        self.grid_rowconfigure(4, weight = 1)
        self.grid_rowconfigure(5, weight = 3)
    def go_add(self):
        Screen.current= 4
        screens[Screen.current].clear()
        screens[Screen.current].edit_key = len(library_database.keys())+1
        Screen.switch_frame()    
    def go_edit(self):
        pop_up = tk.Tk()
        pop_up.title( "Edit")
        frm_edit_list = EditChooser(pop_up)
        
        frm_edit_list.grid(row=0, column=0, sticky="news")
        frm_edit_list.tkraise()
    def go_save(self):   
        Screen.current= 1
        Screen.switch_frame()
    def go_remove(self):   
        Screen.current= 3
        Screen.switch_frame()    
    def go_info(self):   
        Screen.current= 4
        Screen.switch_frame()    
    
    def go_print(self):   
        Screen.current= 6
        Screen.switch_frame()        
"""-------------------------------------------------------------------------------------------------------------------------------------"""
class Saved(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_success = tk.Label(self, text = "File Saved.", font=TITLE_FONT).grid(row="0", column="1")
        
        self.btn_ok = tk.Button(self, text="Ok", font=BUTTON_FONT, command=self.go_menu)
        self.btn_ok.grid(row="1", column="1")
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)   
        
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 3)
        self.grid_rowconfigure(2, weight = 1)
    def go_menu(self):   
        Screen.current= 0
        Screen.switch_frame() 
"""-------------------------------------------------------------------------------------------------------------------------------------"""
class EditChooser(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master=parent)
        self.parent = parent
        self.lbl_instructions = tk.Label(self, text = "Which title to Edit?", font=TITLE_FONT).grid(row="0", column="1", columnspan="2")
        
        self.options = ["Select a title"]
        
        for key in library_database.keys():
            self.options.append(library_database[key][1])
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(self.options[0])
        self.menu_title = tk.OptionMenu(self, self.tkvar, *self.options)
        self.menu_title.grid(row="2", column="1", columnspan="2", sticky="news")
        
        self.btn_cancel = tk.Button(self, text="Cancel", font=BUTTON_FONT, command=self.cancel)
        self.btn_cancel.grid(row="4", column="1")
        self.btn_ok = tk.Button(self, text="Edit", font=BUTTON_FONT, command=self.go_info)
        self.btn_ok.grid(row="4", column="2")     
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        self.grid_columnconfigure(3, weight = 1)
        self.grid_columnconfigure(4, weight = 1)
        
        self.grid_rowconfigure(0, weight = 6)
        self.grid_rowconfigure(1, weight = 6)
        self.grid_rowconfigure(2, weight = 1)
        self.grid_rowconfigure(3, weight = 6)
        self.grid_rowconfigure(4, weight = 6)
    def cancel(self):   
        self.parent.destroy()   
    def go_info(self):   
        if self.tkvar.get() == self.options[0]:
            pass
        else:
            for i in range(len(self.options)):
                if self.tkvar.get() == self.options[i]:
                    screens[4].edit_key = i
                    break;
            Screen.current= 4
            screens[Screen.current].update()

            Screen.switch_frame()
            self.parent.destroy()        

"""-------------------------------------------------------------------------------------------------------------------------------------"""
class RemoveChooser(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master=parent)
        self.parent=parent
        self.lbl_instructions = tk.Label(self, text = "Which titles to Remove?", font=TITLE_FONT).grid(row="0", column="0", columnspan="2")
        
        options=["Title1", "Title2", "Title3"]
        tkvar = tk.StringVar(self)
        tkvar.set(options[0])
        self.menu_title = tk.OptionMenu(self, tkvar, *options)
        self.menu_title.grid(row="1", column="0", columnspan="2")
        
        self.btn_cancel = tk.Button(self, text="Cancel", font=BUTTON_FONT, command=self.go_menu)
        self.btn_cancel.grid(row="2", column="0")
        self.btn_ok = tk.Button(self, text="Remove", font=BUTTON_FONT,command=self.go_marked )
        self.btn_ok.grid(row="2", column="1") 
    def go_menu(self):   
        Screen.current= 0
        Screen.switch_frame()  
    def go_marked(self):   
        Screen.current= 5
        Screen.switch_frame()    
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

class InfoFrame(Screen):
    def __init__(self,):
        Screen.__init__(self)
        self.edit_key = 0
        
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
        
        self.btn_cancel = tk.Button(self, text="Cancel", command=self.go_menu)
        self.btn_cancel.grid(row="4", column="0")
        
        self.btn_reset = tk.Button(self, text="Reset", command=self.clear)
        self.btn_reset.grid(row="4", column="1")
        
        self.btn_submit = tk.Button(self, text="Submit", command=self.done )
        self.btn_submit.grid(row="4", column="2")    
        
        #-------------------------------------------
        
        self.grid_columnconfigure( 0, weight="1")
        self.grid_columnconfigure( 1, weight="1")
        self.grid_columnconfigure( 2, weight="1")
    def go_menu(self):   
        print("go_menu")
        Screen.current= 0
        Screen.switch_frame()
    def done(self):
        entry = []
        
        #----------------------------------------------------
        
        entry.append(self.info_frame_entries.ent_genre.get())
        entry.append(self.info_frame_entries.ent_title.get())
        entry.append(self.info_frame_entries.ent_dev.get())
        entry.append(self.info_frame_entries.ent_pub.get())
        entry.append(self.info_frame_entries.ent_system.get())
        entry.append(self.info_frame_entries.ent_rating.get())
        entry.append(self.info_frame_entries.ent_release_date.get())
        entry.append("single")
        entry.append(self.info_frame_entries.ent_price.get())
        entry.append("yes")
        entry.append(self.info_frame_entries.ent_purchase_date.get())
        entry.append(self.scr_notes.get(0.0, "end"))
        
        
        #----------------------------------------------------
        
        library_database[self.edit_key] = entry
       
        mb.showinfo(message = "Entry has been added")
        
        Screen.current= 0
        Screen.switch_frame()        
    
    def update(self):
        entry = library_database[self.edit_key]
        self.info_frame_entries.ent_genre.delete(0,"end")
        self.info_frame_entries.ent_genre.insert(0, entry[0])
        
        self.info_frame_entries.ent_title.delete(0,"end")
        self.info_frame_entries.ent_title.insert(0, entry[1])
        
        self.info_frame_entries.ent_dev.delete(0,"end")
        self.info_frame_entries.ent_dev.insert(0, entry[2])
     
        self.info_frame_entries.ent_pub.delete(0,"end")
        self.info_frame_entries.ent_pub.insert(0, entry[3])
        
        self.info_frame_entries.ent_system.delete(0,"end")
        self.info_frame_entries.ent_system.insert(0, entry[4])
         
        self.info_frame_entries.ent_rating.delete(0,"end")
        self.info_frame_entries.ent_rating.insert(0, entry[5])
        
        self.info_frame_entries.ent_release_date.delete(0,"end")
        self.info_frame_entries.ent_release_date.insert(0, entry[6])
        
        self.info_frame_entries.ent_price.delete(0,"end")
        self.info_frame_entries.ent_price.insert(0, entry[8])
        
        self.info_frame_entries.ent_purchase_date.delete(0,"end")
        self.info_frame_entries.ent_purchase_date.insert(0, entry[10])
        
        self.scr_notes.delete(0.0, "end")
        self.scr_notes.insert(0.0, entry[11])
    
    def clear(self):
        self.info_frame_entries.ent_genre.delete(0,"end")
        self.info_frame_entries.ent_title.delete(0,"end")
        self.info_frame_entries.ent_dev.delete(0,"end")
        self.info_frame_entries.ent_pub.delete(0,"end")
        self.info_frame_entries.ent_system.delete(0,"end")
        self.info_frame_entries.ent_rating.delete(0,"end")
        self.info_frame_entries.ent_release_date.delete(0,"end")
        self.info_frame_entries.ent_price.delete(0,"end")
        self.info_frame_entries.ent_purchase_date.delete(0,"end")
        self.scr_notes.delete(0.0, "end")

class MarkedFrame(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_notes = tk.Label(self, text="These items are marked for removal ").grid(row="0", column="0", columnspan = "3")
        self.scr_items = scrolledtext.ScrolledText(self, height="8",width="60", )
        self.scr_items.grid(row="1", column="0", columnspan="3")
        #------------------------------------------
        
        self.btn_cancel = tk.Button(self, text="Cancel", command=self.go_menu)
        self.btn_cancel.grid(row="2", column="0")
        self.btn_submit = tk.Button(self, text="Submit", command=self.go_menu)
        self.btn_submit.grid(row="2", column="2")   
    def go_menu(self):   
        Screen.current= 0
        Screen.switch_frame()
        
class PrintFrameChecks(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, master=parent)
        var1 = None
        self.chk_genre = tk.Checkbutton(self, text='Genre',variable=var1, onvalue=1, offvalue=0,)
        self.chk_genre.grid(row = 0, column=0, sticky="news")
        
        self.chk_title = tk.Checkbutton(self, text='Title',variable=var1, onvalue=1, offvalue=0,)
        self.chk_title.grid(row = 0, column=1, sticky="news")
        
        self.chk_dev = tk.Checkbutton(self, text='Developer',variable=var1, onvalue=1, offvalue=0,)
        self.chk_dev.grid(row = 0, column=2, sticky="news")
        
        self.chk_pub = tk.Checkbutton(self, text='Publisher',variable=var1, onvalue=1, offvalue=0,)
        self.chk_pub.grid(row = 1, column=0, sticky="news")

        self.chk_system = tk.Checkbutton(self, text='System',variable=var1, onvalue=1, offvalue=0,)
        self.chk_system.grid(row = 1 , column = 1, sticky="news")
        
        self.chk_rating = tk.Checkbutton(self, text='Rating',variable=var1, onvalue=1, offvalue=0,)
        self.chk_rating.grid(row = 1, column=2, sticky="news")
        
        self.chk_release = tk.Checkbutton(self, text='Release date',variable=var1, onvalue=1, offvalue=0,)
        self.chk_release.grid(row = 2, column=0, sticky="news")
        
        self.chk_players = tk.Checkbutton(self, text='single/multi',variable=var1, onvalue=1, offvalue=0,)
        self.chk_players.grid(row = 2, column=1, sticky="news")
        
        self.chk_price = tk.Checkbutton(self, text='price',variable=var1, onvalue=1, offvalue=0,)
        self.chk_price.grid(row = 2, column=2, sticky="news")
        
        self.chk_beat = tk.Checkbutton(self, text='Beat it',variable=var1, onvalue=1, offvalue=0,)
        self.chk_beat.grid(row = 3, column=0, sticky="news")
        
        self.chk_purchase_date = tk.Checkbutton(self, text='Purchase Date',variable=var1, onvalue=1, offvalue=0,)
        self.chk_purchase_date.grid(row = 3, column=1, sticky="news")
class PrintFrame(Screen):
    def __init__(self):
        Screen.__init__(self)
        
           
        
        #-----------------------------------------
        
        self.lbl_search = tk.Label(self, text="Search", font=TITLE_FONT).grid(row='0', column='0', columnspan='3')
        tk.Frame.__init__(self)
        self.lbl_search_by = tk.Label(self, text="Search By").grid(row="1", column="0")
        options=["Info1", "Info2", "Info3"]
        tkvar = tk.StringVar(self)
        tkvar.set(options[0])
        self.menu_search_by = tk.OptionMenu(self, tkvar, *options)
        self.menu_search_by.grid(row="2", column="0", )        
        
        #------------------------------------------
        
        self.lbl_search_for = tk.Label(self, text="Search For: ").grid(row="3", column="0")
        self.ent_search_for = tk.Entry(self,)
        self.ent_search_for.grid(row="4", column="0")
        
        #------------------------------------------
        
        self.scr_info = scrolledtext.ScrolledText(self, height="8",width="60")
        self.scr_info.grid(row="5", column="0", columnspan='3')
        
        #------------------------------------------
        
        self.btn_cancel = tk.Button(self, text="Cancel",command=self.go_menu)
        self.btn_cancel.grid(row="6", column="0")
        self.btn_reset = tk.Button(self, text="Reset", )
        self.btn_reset.grid(row="6", column="1")
        self.btn_confirm = tk.Button(self, text="Submit")
        self.btn_confirm.grid(row="6", column="2")
    
        self.frm_print_frame_checks = PrintFrameChecks(self)
        self.frm_print_frame_checks.grid(row=2, column=1, rowspan=3, columnspan=3 ,sticky="news")
    def go_menu(self):   
        print("go_menu")
        Screen.current= 0
        Screen.switch_frame()      

if __name__ == "__main__":
    datafile = open("game_lib.pickle" , "rb")
    library_database = pickle.load(datafile)
    datafile.close()
    maxkey = max(list(library_database.keys()))
    root = tk.Tk()
    root.title("Game Lib")
    
    root.grid_columnconfigure(0, weight="1")
    root.grid_rowconfigure(0, weight="1")
    root.geometry("500x500")
    screens = [MainMenu(), None, None,None,InfoFrame(),MarkedFrame(),
               PrintFrame(),]    
    for i in range(len(screens)):
        try:
            screens[i].grid(row="0", column="0", sticky="news")
        except:
            None
    screens[0].tkraise()
    root.mainloop()