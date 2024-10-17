import subprocess
import os

#MSI file installer
def MSI_Installer(MSI_File):
    print("Installing MSI file...")

    msi_path = os.path.join(os.getcwd(), "Temp", MSI_File)
    print(msi_path)

    # Calls msiexec.exe with arguments for silent install and no restart
    subprocess.call([r"msiexec.exe", "/i", msi_path, "/qn", "/norestart"])

    print("Installation complete!")

#Winget package installer
def Winget_Installer(Winget_Package):
    print("Installing application from Winget...")

    # Calls winget to install a program
    subprocess.call([r"winget", "install", "--silent", "--exact", "--id", Winget_Package])

    print("Installation complete")
