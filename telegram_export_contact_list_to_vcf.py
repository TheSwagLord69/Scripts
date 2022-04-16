#!/usr/bin/python

# Usage: python telegram_export_contact_list_to_vcf.py [path of contacts.html]
# Export contacts from Telegram Desktop. (Settings > Advanced > Export Telegram Data > Check only "Contacts list") https[:]//www[.]quora[.]com/How-can-I-export-telegram-contacts
# To find contacts.html, Navigate to "Telegram Desktop\DataExport_YYYY_MM_DD\lists"

import sys
import os
import re

contact_list = []
contact_counter = 0

with open(os.path.abspath(sys.argv[1])) as f:
    lines = f.readlines()
    
'''enumerate lines'''
for c, i in enumerate(lines):
    
    '''seach name'''
    regex = '<div class="name bold">'
    if re.search(regex, i):
        contact_name = str(lines[c+1])
        contact_number = str(lines[c+5]).replace(" ", "")
        
        '''strip front "+" and all whitespace'''
        if re.search("[a-z]", contact_number):
            pass
        else:
            contact_list.append({"name":contact_name,"number":contact_number})
            
'''write to a new contacts.vcf'''
f = open("newcontacts.vcf", "w")

for i in contact_list:
    f.write("BEGIN:VCARD\n")
    f.write("VERSION:2.1\n")
    f.write("N:;" + str(i['name']).strip() + ";;;\n")
    f.write("FN:"+ str(i['name']).strip() +"\n")
    f.write("TEL;CELL;PREF:"+ str(i['number']).strip() +"\n")
    f.write("END:VCARD\n")
    
f.close()