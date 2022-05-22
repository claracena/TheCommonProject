import dbconn
import tkinter
import customtkinter

with dbconn.Database() as db:
    categories = db.select_all_categories()

customtkinter.set_appearance_mode('System')  # Modes: system (default), light, dark
customtkinter.set_default_color_theme('dark-blue')  # Themes: blue (default), dark-blue, green

root_tk = customtkinter.CTk()  # create CTk window like you do with the Tk window
root_tk.geometry('640x480')
root_tk.title('The Common Project')
root_tk.resizable(False, False)
root_tk.iconbitmap('assets/images/project-icon.ico')

frame_title = customtkinter.CTkFrame(master=root_tk,
                               width=10000,
                               height=100,
                               corner_radius=10)

frame_root_menu = customtkinter.CTkFrame(master=root_tk,
                               width=10000,
                               height=10000,
                               corner_radius=10)

frame_projects_menu = customtkinter.CTkFrame(master=root_tk,
                               width=10000,
                               height=10000,
                               corner_radius=10)
                               
frame_title.pack(padx=20, pady=20)
frame_root_menu.pack(padx=20, pady=20)
frame_projects_menu.pack(padx=20, pady=20)

def show_cats():
    frame_root_menu.pack()
    frame_projects_menu.pack_forget()
    my_subtitle.config(text='Please select a category')

def show_projects():
    frame_projects_menu.pack()
    frame_root_menu.pack_forget()
    for widget in frame_projects_menu.winfo_children():
        widget.destroy()
    my_subtitle.config(text='Now choose a project from this category')

def button_launch_module(mod_name):
    try:
        exec(open('modules/' + mod_name).read())
    except:
        print('There has been an error')

def button_select_cat(cat_id):
    with dbconn.Database() as db:
        modules = db.select_all_modules_from_cateory(cat_id)
        # print(modules)
        show_projects()

        i = 0
        final_pos = 0
        for n in modules:
            name = 'button_' + str(i)
            name = customtkinter.CTkButton(frame_projects_menu, text=n[2], command=lambda j = n[6]:button_launch_module(j))
            final_pos = (i / 7) + 0.1
            name.place(relx=0.5, rely=final_pos, anchor=tkinter.N)
            i += 1

        button_back = customtkinter.CTkButton(frame_projects_menu, text='Back', command=button_back_func)
        button_back.place(relx=0.5, rely=final_pos + 0.2, anchor=tkinter.N)

        button_exit = customtkinter.CTkButton(frame_projects_menu, text='Exit', command=button_exit_func)
        button_exit.place(relx=0.5, rely=final_pos + 0.4, anchor=tkinter.N)

def button_exit_func():
    root_tk.destroy()

def button_back_func():
    show_cats()

my_title = customtkinter.CTkLabel(frame_title, text='Welcome to The Common Project', text_font=(None, 15))
my_title.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

my_subtitle = customtkinter.CTkLabel(frame_title, text='')
my_subtitle.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

show_cats()

i = 0
final_pos = 0
for n in categories:
    name = 'button_' + str(i)
    name = customtkinter.CTkButton(frame_root_menu, text=n[1], command=lambda j = i:button_select_cat(j))
    final_pos = (i / 7) + 0.1
    name.place(relx=0.5, rely=final_pos, anchor=tkinter.N)
    i += 1

button_exit = customtkinter.CTkButton(frame_root_menu, text='Exit', command=button_exit_func)
button_exit.place(relx=0.5, rely=final_pos + 0.2, anchor=tkinter.N)

root_tk.mainloop()
