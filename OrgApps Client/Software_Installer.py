import subprocess
import os

def MSI_Installer(MSI_File):

    print("Installing MSI file...")

    msi_path = os.path.join(os.getcwd(), "Temp", MSI_File)
    print(msi_path)

    # Call msiexec.exe with arguments for silent install and no restart
    subprocess.call([r"msiexec.exe", "/i", msi_path, "/qn", "/norestart"])

    print("installation complete!")
