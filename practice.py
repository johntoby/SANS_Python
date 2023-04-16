user_list = "tolu, toby, toye, timmy"
print(user_list) 

sule_list = "tolu\ntoby\ntoye\ntimmy" 
print(sule_list)

user_list1 = "user list: \n\ttolu\n\ttoby\n\tsule\n\tmonkey" 
print (user_list1)

email = "john@email.com" 
print("'" + email.lstrip() + "'\n'" + email.rstrip() + "'\n'" + email.strip()) 

email = "sulezoo@badoo.com" 
print("jt" + " " + email.lstrip()) 

email = "sulezoo@badoo.com" 
print("jt" + " " + email) 

phrase = "Hello world"
print(phrase[0:8])    

phrase = "a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p"
print(phrase.split('-')) 

phrase = "a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p"
print(phrase.count('-')) 

phrase = "Hello Alex"
print(phrase.replace("Hello", "JT")) 

phrase = "The quick brown fox jumps over the lazy dog" 
print(phrase.upper())   

phrase = "The quick brown fox jumps over the lazy dog" 
print(phrase.lower())  

phrase = "The quick brown fox jumps over the lazy dog" 
print(phrase.title())  

phrase = "The quick brown fox jumps over the lazy dog" 
print(phrase.capitalize())

phrase = "The quick brown fox jumps over the lazy dog" 
print(phrase.swapcase())   

print(10+3*4) 

print((10+3)*4) 

print(5/6)

print(round(655.9876, 2) )   



jt = 15
jt_str = str(jt) 
print("sarah has closed " + jt_str + " cases this week") 

jt = 15
print("sarah has closed " + str(jt) + " cases this week") 

morning_coffee = None
afternoon_coffee = 9

jt_morning_coffee = bool(morning_coffee)
print(jt_morning_coffee) 


fav_linix_distros = ["centOs", "debian", 'ubuntu', "babayaga"]
print(fav_linix_distros) 
print(fav_linix_distros[-1]) 
jt_top_fav_linux_distro = fav_linix_distros[0]
print("Jt's fav linux distro is " + jt_top_fav_linux_distro.upper() + " !") 

print(len(fav_linix_distros))
