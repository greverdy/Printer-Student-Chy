##############################╩╬╦
# ╔══════════════════════════╗
# ║   Printer Student - V.1  ║
# ║    V.1 in Python 3.10    ║
# ║        -24/06/22-        ║
# ╠══════════════════════════╣
# ║       •By G.REVERDY      ║
# ║          •ECORIS         ║
# ╚══════════════════════════╝
##############################

##############################
#   ╔════════════╗
#   ║   IMPORT   ║
#   ╚════════════╝

    # Module permettant la gestion de l'OS
import os
import shutil

    # Module permettant d'afficher du texte graphique amélioré (pour les titres par exemple) dans le terminal
from pyfiglet import Figlet

    # Module permettant l'intégration de temps de pause
import time

    # Module 7zip
import zipfile

##############################

##############################
#   ╔═════════════════════╗
#   ║   VARIABLES FIXES   ║
#   ╚═════════════════════╝


##############################

##############################
#   ╔═════════════════╗
#   ║   DEFINITIONS   ║
#   ╚═════════════════╝

    # Génère des blank
def wipe(n):
    print('\n' * n)

def isAdmin():
    try:
        with open("C:/Windows/WindowsUpdate.log", 'w'):
            print("")
        os.system("del C:\\Windows\\WindowsUpdate.log")
        print(Figlet(font='big').renderText(' ADMIN OK'))
        time.sleep(3)
        wipe(20)
        os.system('cls' if os.name == 'nt' else 'clear')
    except PermissionError:
        print(Figlet(font='big').renderText(' NOT ADMIN'))
        try:
            os.system(f"exit")
        except:
            exit()


########################################################
print("")
########################################################
#   ╔═══════════╗
#   ║   CODES   ║
#   ╚═══════════╝

isAdmin()


print("\n • Télchargement des pilotes de l'imprimante MFC-J4540DW")

if os.system('curl -s "https://download.brother.com/welcome/dlf105297/Y20B_C1-hostm-A1.EXE" --output %userprofile%\\Desktop\\Pilotes-MFCJ4540DW.7z') == 0:
    #os.system("%userprofile%\\Desktop\\Pilotes-MFCJ4540DW.exe")
    with zipfile.ZipFile(os.environ['USERPROFILE']+'\\Desktop\\Pilotes-MFCJ4540DW.7z', 'r') as zip_ref:
        zip_ref.extractall(os.environ['USERPROFILE']+"\\Desktop\\Pilotes-MFCJ4540DW")
    zip_ref.close()
    print("\n • Pilotes de l'imprimante MFC-J4540DW téléchargés")
else:
    print("\n • Impossible de télécharger le pilote pour l'imprimante MFC-J4540DW")
    print("\n\n • Merci de télécharger les pilotes en recherchant : MFC-J4540DW pilotes")

wipe(5)

if os.system('Cscript "C:\\Windows\\System32\\Printing_Admin_Scripts\\fr-FR\\Prnport.vbs" -a -r 192.168.12.9 -h 192.168.12.9 -o raw -n 9100') == 0:
    print("\n • Port 192.168.12.9:9100 créé !")
else:
    print("\n • Port 192.168.12.9:9100 non créé !")
    print("\n • Une erreur est survenue !")

wipe(5)

if os.system('cscript "C:\\Windows\\System32\\Printing_Admin_Scripts\\fr-FR\\prndrvr.vbs" -a -m "Brother MFC-J4540DW Printer" -i "C:\\Users\\Administrateur\\Desktop\\Pilotes-MFCJ4540DW\\gdi\\BRPRI19C.INF"') == 0:
    print("\n • Pilote Brother MFC-J4540DW Printer ajouté !")
else:
    print("\n • Le pilote Brother MFC-J4540DW Printer n'a pas été installé !")
    print("\n • Une erreur est survenue !")

wipe(5)

if os.system('Cscript "C:\\Windows\\System32\\Printing_Admin_Scripts\\fr-FR\\Prnmngr.vbs" -a -p "Brother MFC-J4540DW Printer" -m "Brother MFC-J4540DW Printer" -r 192.168.12.9') == 0:
    print("\n • Imprimante Brother MFC-J4540DW Printer installée !")
else:
    print("\n • L'imprimante Brother MFC-J4540DW Printer n'a pas pu être installée !")
    print("\n • Une erreur est survenue !")
    os.system('echo Erreur d\'installation de l\'imprimante Brother MFC-J4540DW, merci de contacter le service informatique à l\'adresse suivante : informatique@ecoris.fr')
    exit()

wipe(5)

if os.system('Cscript "C:\\Windows\\System32\\Printing_Admin_Scripts\\fr-FR\\prncnfg.vbs" -z "Imprimante RDC Break" -x -p "Brother MFC-J4540DW Printer"') == 0:
    print("\n • Imprimante Brother MFC-J4540DW Printer renommé en Imprimante RDC Break !")
    wipe(5)

    if os.system('powershell.exe "Set-PrintConfiguration -PrinterName \'Imprimante RDC Break\' -Color $False"') == 0:
        print("\n • Échelle de gris sélectionnée !")
    else:
        print("\n • Impossible de sélectionner \"Échelle de gris\"")
        print("\n • Une erreur est survenue !")
        
    wipe(5)

    if os.system('RUNDLL32 PRINTUI.DLL,PrintUIEntry /y /n "Imprimante RDC Break"') == 0:
        print("\n • Imprimante Brother MFC-J4540DW Printer : sélectionnée par défaut !")
    else:
        print("\n • L'imprimante Brother MFC-J4540DW Printer n'a pas pu être mis par défaut !")
        print("\n • Une erreur est survenue !")
else:
    print("\n • Impossible de renommer l'imprimante MFC-J4540DW en Imprimante RDC Break")
    print("\n • Une erreur est survenue !")
    wipe(5)

    if os.system('powershell.exe "Set-PrintConfiguration -PrinterName \'Brother MFC-J4540DW Printer\' -Color $False"') == 0:
        print("\n • Échelle de gris sélectionnée !")
    else:
        print("\n • Impossible de sélectionner \"Échelle de gris\"")
        print("\n • Une erreur est survenue !")
        
    wipe(5)

    if os.system('RUNDLL32 PRINTUI.DLL,PrintUIEntry /y /n "Brother MFC-J4540DW Printer"') == 0:
        print("\n • Imprimante Brother MFC-J4540DW Printer : sélectionnée par défaut !")
    else:
        print("\n • L'imprimante Brother MFC-J4540DW Printer n'a pas pu être mis par défaut !")
        print("\n • Une erreur est survenue !")

wipe(5)

if os.system('del %userprofile%\\Desktop\\Pilotes-MFCJ4540DW.7z') == 0 :
    print("\n • L'archive contenant les pilotes a été supprimés !")
else:
    if Path(os.environ['USERPROFILE']+'\\Desktop\\Pilotes-MFCJ4540DW.7z').is_file():
        print("\n • Impossible de supprimer l'archive contenant les pilotes")
        print("\n • Une erreur est survenue !")
    else:
        print("\n • L'archive contenant les pilotes a été supprimés !")

wipe(5)

if os.system('rmdir /S /Q %userprofile%\\Desktop\\Pilotes-MFCJ4540DW') == 0 :
    print("\n • Le dossier contenant les pilotes a été supprimé !")
else:
    print("\n • Impossible de supprimer le dossier contenant les pilotes")
    print("\n • Une erreur est survenue !")

time.sleep(5)
