import customtkinter
from PIL import Image
from Software_Installer import MSI_Installer, Winget_Installer

# Temp Array for testing
Installable_Apps = ["Audacity", "Steam", "Xbox", "Word", "Teams", "Excel", "Outlook", "Powerpoint", "Edge", "Chrome", "Visual studio code", "Proton Mail", "Proton Callender", "Proton Drive", "Proton VPN"]

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Window Setings
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("green")
        self.title("OrgApps")
        self.iconbitmap('C:/Users/Flux/Documents/GitHub/OrgApps/OrgApps Client/OrgApps_Logo.ico')
        self.minsize(1000, 500)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(2, weight=1)

        # Frame's
        self.Left_Bar = Left_Bar(master=self)
        self.Left_Bar.grid(row=0, column=0, sticky="nsw")

        self.Padding = customtkinter.CTkLabel(self, text="  ")
        self.Padding.grid(row=0, column=1, pady=3)

        self.Apps_List = All_Apps_List(master=self)
        self.Apps_List.grid(row=0, column=2, sticky="nesw")


# Left Bar
class Left_Bar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Left Bar widgets
        self.Categories_Label = customtkinter.CTkLabel(self, text="Categories")
        self.Categories_Label.grid(row=0, column=0, pady=5, padx=20)

        self.All_Apps_Buttion = customtkinter.CTkButton(self, text="All Apps", command=lambda: All_Apps_Event())
        self.All_Apps_Buttion.grid(row=1, column=0, pady=5, padx=5)

        self.Apps_Buttion = customtkinter.CTkButton(self, text="Apps", command=lambda: Apps_Event())
        self.Apps_Buttion.grid(row=2, column=0, pady=5, padx=5)

        self.Tools_Buttion = customtkinter.CTkButton(self, text="Tools", command=lambda: Tools_Event())
        self.Tools_Buttion.grid(row=3, column=0, pady=5, padx=5)

        self.Fonts_Buttion = customtkinter.CTkButton(self, text="Fonts", command=lambda: Fonts_Event())
        self.Fonts_Buttion.grid(row=4, column=0, pady=5, padx=5)

        self.Verson_Number = customtkinter.CTkLabel(self, text="OrgApps: V0.1")
        self.Verson_Number.grid(row=10, sticky="s")
        self.grid_rowconfigure(10, weight=1)


# App Frame
class App_Frame(customtkinter.CTkFrame):
    def __init__(self, master, App_Label, **kwargs):
        super().__init__(master, **kwargs)

        self.App_Label = App_Label

        self.App_Icon = customtkinter.CTkImage(Image.open("C:/Users/Flux/Documents/GitHub/OrgApps/OrgApps Client/OrgApps_Logo.ico"), size=(60, 60))
        self.Icon_lable = customtkinter.CTkLabel(self, image=self.App_Icon, text="")
        self.Icon_lable.grid(row=0, column=0, pady=10)

        self.label = customtkinter.CTkLabel(self, text=self.App_Label)
        self.label.grid(row=1, column=0, padx=20)


        self.App_Buttion = customtkinter.CTkButton(self, text="Install")
        self.App_Buttion.grid(row=2, column=0, padx=20, pady=5)


# All Apps List
class All_Apps_List(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Apps List widgets
        self.label = customtkinter.CTkLabel(self, text="All Apps")
        self.label.grid(row=0, column=0, padx=20)

# Apps List
class Apps_List(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Apps List widgets
        self.label = customtkinter.CTkLabel(self, text="Apps")
        self.label.grid(row=0, column=0, padx=20)

        row_count = 1
        col_count = 0


        for x in Installable_Apps:
            self.App_Frame = App_Frame(master=self, App_Label=x, fg_color=("#eaeaea", "#232323"))
            self.App_Frame.grid(row=row_count, column=col_count, pady=5, padx=5)

            col_count += 1
            if col_count >= 4:  # Adjust the number of columns as needed
                col_count = 0
                row_count += 1


# Tools List
class Tools_List(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Tool List widgets
        self.label = customtkinter.CTkLabel(self, text="Tools")
        self.label.grid(row=0, column=0, padx=20)

# Fonts List
class Fonts_List(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Tool List widgets
        self.label = customtkinter.CTkLabel(self, text="Fonts")
        self.label.grid(row=0, column=0, padx=20)

        MSI_File = ""
        self.Sasson_Buttion = customtkinter.CTkButton(self, text="Test Font", command=lambda: MSI_Installer(MSI_File))
        self.Sasson_Buttion.grid(row=4, column=0, pady=5, padx=5)

# Events

def All_Apps_Event():
    app.Apps_List.destroy()
    app.Apps_List = All_Apps_List(master=app)
    app.Apps_List.grid(row=0, column=2, sticky="nesw")

def Apps_Event():
    app.Apps_List.destroy()
    app.Apps_List = Apps_List(master=app)
    app.Apps_List.grid(row=0, column=2, sticky="nesw")

def Tools_Event():
    app.Apps_List.destroy()
    app.Apps_List = Tools_List(master=app)
    app.Apps_List.grid(row=0, column=2, sticky="nesw")

def Fonts_Event():
    app.Apps_List.destroy()
    app.Apps_List = Fonts_List(master=app)
    app.Apps_List.grid(row=0, column=2, sticky="nesw")


app = App()
app.mainloop()