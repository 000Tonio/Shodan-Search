#!/usr/bin/env python
# -*- coding: utf-8 -*-
from shodan import Shodan
import os , sys , time
import progressbar
from tqdm import tqdm
from progressbar import *
import signal   

os.system('cls' if os.name == 'nt' else 'clear')
api = Shodan('Your_API_KEY')
class COLOR:
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	FAIL = '\033[91m'
	END = '\033[0m'
	REDS = '\033[91m'
	WHITE = '\033[97m'
	BOLD  = '\033[1m'
	RED   = '\033[91m'
widgets=['Chargement : ',
COLOR.YELLOW          , Percentage()                        , COLOR.END,
COLOR.RED + COLOR.BOLD, Bar(left=' ', marker='━', right=' '), COLOR.END,
COLOR.YELLOW          , Timer()                             , COLOR.END
]



try:
	try:
     		raise KeyboardInterrupt
	except KeyboardInterrupt:
     		print("Keyboard interrupt exception caught")
	def shosho2():	
		counter = 1
		
		
		result = api.host(mot) 
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
		print ("[+] \033[1;31mLien:\033[1;m https://www.shodan.io/host/" + (result["ip_str"]))
		#print ("[+] \033[1;31mThe banner information for the service: \033[1;m\n\n" + (result["data"]))
		print ("\n[✓] Result: %s . Search query: %s" % (str(counter), str(mot)))
		data = ("\nIP: " + result["ip_str"]) + ("\nPort: " + str(result.get("port"))) + ("\nOrganisation: " + str(result.get("org"))) + ("\nLocation: " + str(result.get("location"))) + ("\nLayer: " + str(result.get("transport"))) + ("\nDomains: " + str(result.get("domains"))) + ("\nHostnames: " + str(result.get("hostnames"))) + ("\nData\n" + str(result.get("data")))
		
		
		
		
		for i in range(results['total']) :
			time.sleep(0.01)
			pbar.update(i)
			
		print("\nLimit de 1 IP arriver a terme")
		widgets[4] = COLOR.YELLOW
		
		os._exit(1)
			
		
	def shosho():	
		counter = 0
		
		a = 0
		for result in api.search_cursor(mot) :
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
			print ("[+] \033[1;31mLien:\033[1;m https://www.shodan.io/host/" + (result["ip_str"]))
			#print ("[+] \033[1;31mThe banner information for the service: \033[1;m\n\n" + (result["data"]))
			print ("\n[✓] Result: %s . Search query: %s" % (str(counter), str(mot)))
			data = ("\nIP: " + result["ip_str"]) + ("\nPort: " + str(result["port"])) + ("\nOrganisation: " + str(result["org"])) + ("\nLocation: " + str(result["location"])) + ("\nLayer: " + result["transport"]) + ("\nDomains: " + str(result["domains"])) + ("\nHostnames: " + str(result["hostnames"])) + ("\nData\n" + result["data"])
			
			counter = counter + 1
			#progress()
			
			if counter >= int(limit) + 1 :
				print("\nLimit de "+ (str(limit)) +" arriver a terme")
				widgets[4] = COLOR.YELLOW
				pbar.finish()
				os._exit(1)
			
			pbar.update(a)
			time.sleep(0.1)
	
	ans=True
	while ans:
		print (COLOR.GREEN + "███████╗██╗  ██╗ ██████╗ ██████╗  █████╗ ███╗   ██╗")
		print ("██╔════╝██║  ██║██╔═══██╗██╔══██╗██╔══██╗████╗  ██║")
		print ("███████╗███████║██║   ██║██║  ██║███████║██╔██╗ ██║   ")
		print ("╚════██║██╔══██║██║   ██║██║  ██║██╔══██║██║╚██╗██║   ")
		print ("███████║██║  ██║╚██████╔╝██████╔╝██║  ██║██║ ╚████║   ")
		print ("╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝   ")
		print ("")
		print ("Author: 000Tonio")
		print ("github.com/000Tonio" + COLOR.END)
		print (COLOR.YELLOW + "[!] Legal Disclaimer: We aren't responsible for bad use of this tool!" + COLOR.END)
		print ("")
		print("""
    		1.Simple IP
    		2.Multi IP
    		3.Premiere utilisation
    		4.Exit/Quit
    		""")
		ans=input("What would you like to do? ")
		print("")
		if ans=="1":
      			mot = input("\nRecherche IP : ")
      			results = api.search(mot)
      			
      			print('Results found: {}'.format(results['total']))
      			pbar = ProgressBar(widgets=widgets, maxval=100).start()
      			time.sleep(1)
      			shosho2()
		elif ans=="2":
      			mot = input("\nRecherche (exemple apache ou domain.fr) : ")
      			results = api.search(mot)
      			limit = input("Limit de recherche : ")
      			print('Results found: {}'.format(results['total']))
      			numbers = range(int(limit))
      			pbar = ProgressBar(widgets=widgets, maxval=int(limit)).start()
      			time.sleep(1)
      			shosho()
		elif ans=="3":
			os.system('pip install progressbar2' if os.name == 'nt' else 'pip install progressbar')
			os.system('pip install shodan' if os.name == 'nt' else 'pip install Shodan')
			
		elif ans=="4":
      			print("\n Goodbye") 
      			os._exit(1)
		else:
       			print("\n Not Valid Choice Try again")
       			time.sleep(1)
       			os.system('cls' if os.name == 'nt' else 'clear')
			

except KeyboardInterrupt:
	os.system('cls' if os.name == 'nt' else 'clear')
	print("\nOups.. Fin du programme")
	sys.exit(1)
