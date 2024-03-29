#!/usr/bin/env python
# -*- coding: utf-8 -*-
from shodan import Shodan
import os , sys , time
import progressbar
from tqdm import tqdm
from progressbar import *
import signal
import chrono
from rich.console import Console

Fichier = open("API_KEY.txt", "r")
API = Fichier.read()

os.system('cls' if os.name == 'nt' else 'clear')

api = Shodan(API)
Fichier.close()
class COLOR:
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	FAIL = '\033[91m'
	END = '\033[0m'
	REDS = '\033[91m'
	WHITE = '\033[97m'
	BOLD  = '\033[1m'
	RED   = '\033[91m'
	Black = '\033[90m'
widgets=['Chargement : ',
COLOR.YELLOW          , Percentage()                        , COLOR.END,
COLOR.RED + COLOR.BOLD, Bar(left=' ', marker='━', right=' '), COLOR.END,
COLOR.YELLOW          , Timer()                             , COLOR.END
]
console = Console()



try:
	
	def shosho2():	
		try:
			counter = 1
			
			
			result = api.host(mot) 
			file = open("Shodan_IP/Simple_IP/"+ result["ip_str"], "w")
			os.system('cls' if os.name == 'nt' else 'clear')
			
			print ("[+" + "-" * 78 + "+]")
			print ("[+] \033[1;31mIP: \033[1;m" + (result["ip_str"]))
			print ("[+] \033[1;31mPort: \033[1;m" + str(result.get("port")))
			print ("[+] \033[1;31mOS:\033[1;m" + str(result["os"]))
			print ("[+] \033[1;31mOrganization: \033[1;m" + str(result.get("org")))
			print ("[+] \033[1;31mLocation: \033[1;m" + str(result.get("location")))
			print ("[+] \033[1;31mLayer: \033[1;m" + str(result.get("transport")))
			print ("[+] \033[1;31mDomains: \033[1;m" + str(result.get("domains")))
			print ("[+] \033[1;31mHostnames: \033[1;m" + str(result.get("hostnames")))
			print ("[+] \033[1;31mVulnerabilité: \033[1;m" + str(result["vulns"]))
			print ("[+] \033[1;31mLien:\033[1;m https://www.shodan.io/host/" + (result["ip_str"]))
			#print ("[+] \033[1;31mThe banner information for the service: \033[1;m\n\n" + (result["data"]))
			print ("\n[✓] Result: %s . Search query: %s" % (str(counter), str(mot)))
			data = ("\nIP: " + result["ip_str"]) + ("\nPort: " + str(result.get("port"))) + ("\nOrganisation: " + str(result.get("org"))) + ("\nLocation: " + str(result.get("location"))) + ("\nLayer: " + str(result.get("transport"))) + ("\nDomains: " + str(result.get("domains"))) + ("\nHostnames: " + str(result.get("hostnames"))) + ("\nData\n" + str(result.get("data")))
			file.write(data)
			
			
			
			for i in range(results['total']) :
				time.sleep(0.01)
				pb.update(i)
				pbar.update(i)
				
			print("\nLimit de 1 IP arriver a terme")
			print(COLOR.YELLOW + "\nData = Shodan_IP/Simple_IP/" + COLOR.END)
			widgets[4] = COLOR.YELLOW
			file.close()
			
			
			time.sleep(5)
			os.system('cls' if os.name == 'nt' else 'clear')
			#print ("[+" + "-" * 78 + "+]")
			print (COLOR.RED +"[+--------------------------------------[Menu]--------------------------------------+]"+ COLOR.END)
			choix = input("""
			Voulez-vous faire une nouvelle recherche ? 
			
	    		oui
	    						
	    		non
	    		
	    		Réponse : """)
			
			
			if choix =="oui":
	      			print("")
	      			os.system('cls' if os.name == 'nt' else 'clear')
			elif choix =="non":
	      			print("\n Goodbye")
	      			time.sleep(5)
	      			os.system('cls' if os.name == 'nt' else 'clear')
	      			os._exit(1)
	      			
	      				
			
			else:
	       			print("\n Not Valid Choice Try again")
	       			time.sleep(1)
	       			os.system('cls' if os.name == 'nt' else 'clear')
		except:
			print("""
			L'ip """,mot,""" que vous avez rentrer est invalide
			""") 
			time.sleep(5)
			os.system('cls' if os.name == 'nt' else 'clear')
			
			
		
	def shosho():
		
		counter = 0
		z = True
		a = 0
		
		for result in api.search_cursor(mot) :
			file = open("Shodan_IP/Multi_IP/"+ result["ip_str"], "w")
			os.system('cls' if os.name == 'nt' else 'clear')
			a = a + 1
			
			print ("[+" + "-" * 78 + "+]")
			print ("[+] \033[1;31mIP: \033[1;m" + (result["ip_str"]))
			print ("[+] \033[1;31mPort: \033[1;m" + str(result["port"]))
			print ("[+] \033[1;31mOS:\033[1;m" + str(result["os"]))
			print ("[+] \033[1;31mOrganization: \033[1;m" + str(result["org"]))
			print ("[+] \033[1;31mLocation: \033[1;m" + str(result["location"]))
			print ("[+] \033[1;31mLayer: \033[1;m" + (result["transport"]))
			print ("[+] \033[1;31mLayer: \033[1;m" + (result["transport"]))
			print ("[+] \033[1;31mDomains: \033[1;m" + str(result["domains"]))
			print ("[+] \033[1;31mHostnames: \033[1;m" + str(result["hostnames"]))
			#print ("[+] \033[1;31mVulnerabilité: \033[1;m" + str(result["vuln"]))
			print ("[+] \033[1;31mLien:\033[1;m https://www.shodan.io/host/" + (result["ip_str"]))
			#print ("[+] \033[1;31mThe banner information for the service: \033[1;m\n\n" + (result["data"]))
			print ("\n[✓] Result: %s . Search query: %s" % (str(counter), str(mot)))
			data = ("\nIP: " + result["ip_str"]) + ("\nPort: " + str(result["port"])) + ("\nOrganisation: " + str(result["org"])) + ("\nLocation: " + str(result["location"])) + ("\nLayer: " + result["transport"]) + ("\nDomains: " + str(result["domains"])) + ("\nHostnames: " + str(result["hostnames"])) + ("\nData\n" + result["data"])
			file.write(data)
			counter = counter + 1
			
			
			if counter >= int(limit) + 1 :
				print("\nLimit de "+ (str(limit)) +" arriver a terme")
				widgets[4] = COLOR.YELLOW
				pbar.finish()
				file.close()
				print(COLOR.YELLOW + "\nData = Shodan_IP/Simple_IP/" + COLOR.END)
				
				z = False
				
				
				time.sleep(5)
				os.system('cls' if os.name == 'nt' else 'clear')
				
				print (COLOR.RED +"[+--------------------------------------[Menu]--------------------------------------+]"+COLOR.END)	
				choix = input("""
				Voulez-vous faire une nouvelle recherche ? 
				
		    		oui
		    		
		    		non
		    		
		    		Réponse : """)
				
				
				if choix =="oui":
		      			print("")
		      			os.system('cls' if os.name == 'nt' else 'clear')
		      			return "good"
				elif choix =="non":
		      			print("\n Goodbye")
		      			time.sleep(5)
		      			os.system('cls' if os.name == 'nt' else 'clear')
		      			os._exit(1)
		      			
		      				
				
				else:
		       			print("\n Not Valid Choice Try again")
		       			time.sleep(1)
		       			os.system('cls' if os.name == 'nt' else 'clear')
			if z == True :
				pbar.update(a)
				pb.update(a)
				time.sleep(0.1)	
						
			
			
	
	ans=True
	while ans:
		print (COLOR.GREEN + """
		███████╗██╗  ██╗ ██████╗ ██████╗  █████╗ ███╗   ██╗
		██╔════╝██║  ██║██╔═══██╗██╔══██╗██╔══██╗████╗  ██║
		███████╗███████║██║   ██║██║  ██║███████║██╔██╗ ██║
		╚════██║██╔══██║██║   ██║██║  ██║██╔══██║██║╚██╗██║
		███████║██║  ██║╚██████╔╝██████╔╝██║  ██║██║ ╚████║
		╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝   
	[+]--__--__--__--__--__--__--__--__--__--__--__--__--__--__--__--[+]
		"""+ COLOR.END)
		console.print("""
  [+]-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-[+]	
  [+].................                 -+=--=.                 .................[+]
  [+]................                .+######*.                 ................[+]
  [+]...............                 +########+                  ...............[+]
  [+]..............                 +##########=                  ..............[+]
  [+].............                 -############:                 ..............[+]
  [+].............           -==+++#############*+++==:            .............[+]
  [+]............            .:-+*################*+-:              ............[+]
  [+]............                 .:-=+**##**+=-:                   ............[+]
  [+]...........                  ..-***+:.=+**=.:                  ............[+]
  [+]...........                .=#-#####=:*####=**-                 ...........[+]
  [+]...........               -*##-*#[bold red]#[/bold red]#=  :*#[bold red]#[/bold red]#-*##*:               ...........[+]
  [+]...........              -*###+ :-.     :-.:####*:              ...........[+]
  [+]...........                :=##-           +#*=.                ...........[+]
  [+]...........               .:=+##:         =#*=-:                ...........[+]
  [+]...........              =#######=.     :*######*:             ............[+]
  [+]............            +##########*++*###########:            ............[+]
  [+]............           :##***********************#+            ............[+]
  [+].............          *#+=*********************-##-          .............[+]
  [+].............         -##*+#####################=##*         ..............[+]
  [+]..............       .*###=#####################=###-        ..............[+]
  [+]...............      =####=#####################=###*.      ...............[+]
  [+]................     =####=#####################=####.     ................[+]
  [+].................    .+###=####################*+##*-     .................[+]
  [+]..................     .-=-********************+=-:.    ...................[+]
  [+]...........................====================-...........................[+]
  [+]-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-[+]
		""")
		print (COLOR.GREEN +"""
				Author: 000Tonio
				github.com/000Tonio
		""" + COLOR.END)
		print (COLOR.RED +"""
					v 1.2
		""" + COLOR.END)
		print (COLOR.YELLOW + """
				[!] Legal Disclaimer:
				
		     We aren't responsible for bad use of this tool!
		""" + COLOR.END)
		print ("")
		print("""
					Menu
		      	     [+]-_-_-_-_-_-_-_-_-_-[+]
    				   1.Simple IP
    				   2.Multi IP
    				   3.Exit/Quit
    			     [+]-_-_-_-_-_-_-_-_-_-[+]
    		""")
		ans=input("""
			     What would you like to do? """)
		print("")
		if ans=="1":
      			mot = input("""
      			          Recherche IP : """)
      			results = api.search(mot)
      			
      			print("""
      				   Results found: {}
      			""".format(results['total']))
      			pbar = ProgressBar(widgets=widgets, maxval=results['total']).start()
      			pb = chrono.progress("Shodan_Search", len("1"), api_key = API)
      			time.sleep(1)
      			shosho2()
		elif ans=="2":
      			mot = input("""
      			Recherche (exemple apache ou domain.fr) : """)
      			results = api.search(mot)
      			limit = input("""
      			Limit de recherche (MAX 10 000) : """)
      			print("""
      				   Results found: {}
      			""".format(results['total']))
      			numbers = range(int(limit))
      			pb = chrono.progress("Shodan_Search", len(numbers), api_key = API )
      			pbar = ProgressBar(widgets=widgets, maxval=int(limit)).start()
      			time.sleep(1)
      			shosho()	
		elif ans=="3":
      			print("""
      					Goodbye
      			""")
      			time.sleep(5)	
      			os._exit(1)
		else:
       			print("""
       			\n Not Valid Choice Try again
       			""")
       			time.sleep(1)
       			os.system('cls' if os.name == 'nt' else 'clear')
			

except KeyboardInterrupt:
	os.system('cls' if os.name == 'nt' else 'clear')
	print("\nOups.. Fin du programme")
	sys.exit(1)

