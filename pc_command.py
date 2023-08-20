from subprocess import call

#Clase para ejecutar comandos en la PC
#De momento esta en duro funcional para Windows hohoh
class PcCommand():
    def __init__(self):
        pass
    
    def open_chrome(self, website):
        website = "" if website is None else website
        call("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe " + website)
        
    def open_operagx(self, website):
        website = "" if website is None else website
        call("C:/Users/FernandoSanfielReyes/AppData/Local/Programs/Opera GX/launcher.exe " + website)