#==== Modulws ====
from sys import stdout
import requests
import os
from time import sleep
import pyfiglet 
import webbrowser
import phonenumbers
from phonenumbers import geocoder, timezone, carrier 
#====== Banner ======
os.system("clear")
ban = pyfiglet.figlet_format("Tracker", font = "slant")
print("\033[1;33m",ban)
print("\033[1;33m[ + ] \033[0;37mBY : Mohamed Gafar ")                         
#==================
print("\033[1;33m=" * 50)
print ("\t\033[1;33mDeveloper : \033[0;37mM.G_64\n\t\033[1;33mTelegram  : \033[0;37mpythoner_1\n\t\033[1;33mInstagram : \033[0;37mmohamed_gafar5433")
print("\033[1;33m=" * 50)
#===INPUT ===
try :
	while True :
	    

	    list = input ("\033[1;33m[ + ] \033[0;37mEnter 'List' To Show OPtions : ").strip().capitalize()
	    if list == "List" :
        



		                 		           
                         print ("""                                                                                  \033[1;33mCommand                     
\033[1;33m------------                    ------------------------
\033[1;33m[ + ] Help                      Help You To Learn Use Tool
\033[1;33m[ + ] List                      Show This List
\033[1;33m[ + ] Exit                      Exit From Tool
\033[1;33m[ + ] Dev                       Connect With Me
\033[1;33m[ + ] Track                     Start Tracking 
\033[1;33m[ + ] Clear                     Clear Screen 
 """)
 #==========Commands ===========  
                         cmd = input ("\033[1;33m[ + ] \033[0;37mEnter Command : ").strip().capitalize()
                         if cmd == "Help" :
                         	print ("\033[1;33m=" * 55)
                         	print ("\033[1;33m[ + ]\033[0;37m Hello, This Tool To Track IP and Phone Numbers \n\033[1;33m[ + ]\033[0;37m This V.1 From Tool I Will Develop IT More, Enjoy ")
                         	
                         	print ("\033[1;33m=" * 55)
                         	
                         elif cmd == "Exit" :
                         	print ("\033[1;33m[ + ] \033[0;37mGood Bay :) ")
                         	break 
                         elif cmd == "Clear" :
                         	os.system("clear")
                         elif cmd == "List" :
                         	                         print ("""                                                                              \033[1;33mCommand                     
\033[1;33m------------                    ------------------------
\033[1;33m[ + ] Help                      Help You To Learn Use Tool
\033[1;33m[ + ] List                      Show This List
\033[1;33m[ + ] Exit                      Exit From Tool
\033[1;33m[ + ] Dev                       Connect With Me
\033[1;33m[ + ] Track                     Start Tracking 
\033[1;33m[ + ] Clear                     Clear Screen 
 """)
                         	
                	
                         	
                         	
                         elif cmd == "Dev" or cmd == "Develper" :
                         	webbrowser.open("http://t.me/pythoner_1")
                         
                         	
                         	
                         elif cmd == "Track" :
                         	print ("")
                         
                         	track = input("""
\033[1;33m[ + ] \033[0;37mWhat Do You Want Track ?

\033[1;33m[ 1 ] \033[0;37mIP 

\033[1;33m[ 2 ] \033[0;37mPhone Numbers

\033[1;33m::::⟩ \033[0;37m""")
#===========Track IP ============
                         	if track == "IP" or track == "1" or track == "ip" :
                         		ip = requests.get("https://api.ipify.org").text
                         		print(f"\033[1;33m[ + ]\033[0;37m Your IP : {ip}")
                         		print("")
                         		ip = input("\033[1;33m[ + ]\033[0;37m Enter IP To Track IT : ")
                         		load = f"""\033[1;33m[ + ] \033[0;37mLoading....."""
                         		for char in load :
                         			stdout.write(char)
                         			stdout.flush()
                         			sleep(0.001/0.02)
                         		sleep(2)
                         		print ("")
                         		print ("")
                         		
                         		ip_address = ip
                         		response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
                         		print ("\033[1;33m[ + ] Country   : ", "\033[0;37m" ,response.get("country_name"))
                         		print ("\033[1;33m[ + ] City      : ", "\033[0;37m" ,response.get("city"))
                         		print ("\033[1;33m[ + ] Time Zone : ", "\033[0;37m" ,response.get("timezone"))
                         		print ("\033[1;33m[ + ] IP Version: ", "\033[0;37m", response.get("version"))
                         		print ("\033[1;33m[ + ] Currency  : ", "\033[0;37m", response.get("currency_name"))
                         		print ("\033[1;33m[ + ] Cou Code  :", "\033[0;37m", response.get("country_calling_code"))
                         		print ("\033[1;33m[ + ] Languages : ","\033[0;37m", response.get("languages"))
                         		print ("\033[1;33m[ + ] Latitude  : ", "\033[0;37m", response.get("latitude"))
                         		print ("\033[1;33m[ + ] Longitude : ", "\033[0;37m", response.get("longitude"))
                         		net = requests.get(f"http://ip-api.com/json/{ip_address}").json()
                         		print ("\033[1;33m[ + ] Type ISP  : ", "\033[0;37m", (net['isp']))
                        	                                                   

                         		chose = input ("\033[1;33m[ + ]\033[0;37m Do You Want Track Any IP [Y /N] ?  ").strip().capitalize()
                         		if chose == "Y" :
                         			continue
                         		elif chose == "N" :
                         			print ("\033[1;33m[ + ] \033[0;37mGood Bay :)")
                         			break
                         		else :
                         			print("\033[1;31mEror :(")
#=========Phone Numbers=========
                         	elif track == "2" :
                               	   num = input ("\033[1;33m[ + ] \033[0;37mEnter Phone Number And Country Code : ").strip()
                               	   phone = phonenumbers.parse(num, None)
                               	   aod = f"""\033[1;33m[ + ] \033[0;37mLoading....."""
                               	   for char in aod :
                               	   	stdout.write(char)
                               	   	stdout.flush()
                               	   	sleep(0.001/0.02)
                               	   sleep(2)
                               	   print ("")
                               	   print ("")
                               	   print ("\033[1;33m[ + ]\033[0;37m", phone)
                               	   country = geocoder.description_for_number(phone, "en")
                               	   print ("\033[1;33m[ + ] \033[0;37mCountry : " ,country)
                               	   zone = timezone.time_zones_for_number(phone)
                               	   print("\033[1;33m[ + ] \033[0;37mTime Zone :" ,zone)
                               	   num_kind = carrier.name_for_number(phone, "en")
                               	   print("\033[1;33m[ + ] \033[0;37mCompany :", num_kind)
                               	   chose2 = input ("\033[1;33m[ + ]\033[0;37m Do You Want Track Any Number [Y /N] ?  ").strip().capitalize()
                               	   if chose2 == "Y" :
                               	   	continue
                               	   elif chose2 == "N" :
                               	   	print ("\033[1;33m[ + ]\033[0;37m Good Bay :) ")
                               	   	break
                               	   else :
                               	   	print ("\033[1;31mErorr :(")
                               	   	break 
                    
                 
                         else :
                                            print("\033[1;31mErorr :(")              	                 	                 	                 	                 	                 	   
                                            
                                
                     
                       
                       
                       
                      
	
except :
     print ("\033[1;31mErorr :(")
