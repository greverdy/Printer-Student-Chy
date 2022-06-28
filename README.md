
[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](https://ecoris.com)
[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](https://ecoris.com)
[![forthebadge](https://forthebadge.com/images/badges/designed-in-ms-paint.svg)](https://forthebadge.com)

# Printer-Student-Chy

L'exectable "Printer-Student-Chy.exe" vous permettra d'installer l'imprimante située au BREAK du RDC à Ecoris Chambéry.<br>
Code source disponible dans l'archive.<br>
Script compilé à l'aide du module : <a href='https://pypi.org/project/auto-py-to-exe/' target="_blank">AUTO-PY-TO-EXE</a>.

## How To Use
> **Note**
> Vous pouvez simplement télécharger le répertoire et lancer l'excutable.

> **Note**
> Installation avec téléchargement de l'archive.
```bash
# Cloner ce repertoire
$ git clone https://github.com/greverdy/Printer-Student-Chy.git
# Aller dans le repertoire
$ cd Printer-Student-Chy
# Lancer l'application
$ Printer-Student-Chy.exe
# Suppression du dossier
$ cd .. && rmdir /s /q Printer-Student-Chy
```
> **Note**
> Installation avec cmd. [Pilotes MFC-J4540DW à télécharger !](https://www.brother.fr/services-et-supports/mfc-j4540dw/downloads)
```bash
# Création du port de l'imprimante
$ Cscript "C:\Windows\System32\Printing_Admin_Scripts\fr-FR\Prnport.vbs" -a -r 192.168.12.9 -h 192.168.12.9 -o raw -n 9100
# Installation du pilote
$ cscript "C:\Windows\System32\Printing_Admin_Scripts\fr-FR\prndrvr.vbs" -a -m "Brother MFC-J4540DW Printer" -i "<path to folder>\gdi\BRPRI19C.INF"
# Installation de l'imprimante
$ Cscript "C:\Windows\System32\Printing_Admin_Scripts\fr-FR\Prnmngr.vbs" -a -p "Brother MFC-J4540DW Printer" -m "Brother MFC-J4540DW Printer" -r 192.168.12.9
# Configuration : Imprimante par défaut
$ RUNDLL32 PRINTUI.DLL,PrintUIEntry /y /n "Brother MFC-J4540DW Printer"
# Renommage de l'imprimante
$ Cscript "C:\Windows\System32\Printing_Admin_Scripts\fr-FR\prncnfg.vbs" -z "Imprimante RDC Break" -x -p "Brother MFC-J4540DW Printer"
```

## TroubleShooting

- Systèmes d'exploitations supportés : Windows ;
- Merci de vérifier que vous êtes bien sur le réseau : CAMPUS-ECORIS ;
- Merci de vérifier que l'imprimante est bien allumée ;
- [Aide Microsoft](https://support.microsoft.com/fr-fr/windows/installer-une-imprimante-dans-windows-cc0724cf-793e-3542-d1ff-727e4978638b#ID0EBD=Windows_10)
- <a href="mailto:informatique@ecoris.fr?subject=Problème pour se connecter à l'imprimante | Break RDC&body= --- Merci de détailler au mieux votre demande pour que nous puissions vous aider au plus vite ---" target="_blank"> Signaler une erreur / Autres problèmes ➡ mail à : informatique@ecoris.fr </a>
