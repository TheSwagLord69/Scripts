#!/usr/bin/env python
'''
DISCLAIMER:
Use at Your Own Risk
Author holds no responsibility for the accuracy/reliablity of the results.
Any reliance you place on such information is therefore strictly at your own risk.
In no event will the author be liable for any loss or damage including without limitation, indirect or consequential loss or damage, or any loss or damage whatsoever arising from loss of data or profits arising out of, or in connection with, the use of this script.
This information is being given to you gratuitously and there is no agreement or understanding between you and the author regarding your use or modification of this script.

AUTHOR:
Hentai Salesman 69

PREREQUISITES:
pdf_parser.py (by Didier Stevens)[https://github.com/DidierStevens/DidierStevensSuite]

DESCRIPTION:
This Script parses all literal names in the PDF document specified.
Uses and expects pdf_parser.py (by Didier Stevens) in the same directory

USAGE:
python pdf-keywords [example_pdf_filename.pdf]

USEFUL INFORMATION:
What is a literal name / name object?

Name object is an atomic symbol uniquely defined by a seqeuence of characters.
Uniquely defined means that any two name objects made up of the same sequence of characters are identically the same object.
Atomic means that a name has no internal structure; although it is defined by a sequence of characters, those characters are not "elements" of the name
A slash character (/) introduces a name. The slash is not part of the name itself, but a prefix indicating that the following sequence of characters constitutes a name.
There can be no whitespace characters between the slash and the first character in the name.
The name my include any regular characters, but not delimiter or whitespace characters.
Uppercase and lowercase letters are considered distinct. e.g. /A and /a are different

Examples of valid literal names:
/Names1
/ASomewhatLongerName
/A;Name_with-Various***Characters?
/1.2
/$$
/@pattern
/.notdef

Beginning with PDF 1.2, any character except null (character code 0) may be included in a name,
by writing its 2-digit hexadecimal code, preceded by the number sign character (#);
This syntax is required in order to represent any of the delimiter or whitespace characters or the number sign itself;
it is recommended but not required for characters whose codes are outside the range 33 (!) to 126 (~).
E.g. The name /A#20B has four characters (/, A, space, B), not six.

Examples:
Literal Name:               Result:
/Adobe#20Green              Adobe Green
/PANTONE#205757#20CV        PANTONE 5757 CV
/paired#28#29parentheses    paired()parentheses
/The_Key_of_F#23_Minor      The_Key_of_F#_Minor
/A#42                       AB

Reference: https://www.adobe.com/content/dam/acom/en/devnet/pdf/pdfs/pdf_reference_archives/PDFReference.pdf
'''


import sys
import subprocess
import re
from collections import Counter
import os

def check_arguments():
    if (len(sys.argv) == 1) or (str(sys.argv[1]) == "-h") or (str(sys.argv[1]) == "--help"):
        print("USAGE:")
        print("python pdf-keywords.py [example_pdf_filename.pdf]")
        print("\nExample:\npython pdf-keywords.py ligma.pdf")
        print("\npdf-keywords.py Parses all literal names in the PDF document, displays all the lines with keywords found, and sorts by count.")
        quit()
        
def pdfparser():
    #Uses pdf-parser.py to filter away the PDF stream data
    pdffile = sys.argv[1]
    f = open("pdf-parser_out.txt", "w")
    subprocess.call(['python', 'pdf-parser.py', pdffile], stdout=f)
    f.close()
    
    #Read contents of pdf-parser.py
    f = open("pdf-parser_out.txt","r")
    if f.mode == 'r':
        contents =f.read()
    f.close()
    
    #Return contents of pdf-parser.py
    return contents
    
def search_keywords(contents):
    #Use regex to find all the valid literal names
    #Get tags by line without separating multiple tags
    regex = "\/.*[\n]"
    name_objects = re.findall(regex, contents)
    
    #Returns all valid literal names
    return name_objects
    
def sort_occurances(name_objects):
    #Sort and count
    counter = Counter(name_objects)
    print("\nCount ("+str(len(name_objects))+")\nQty:\tName:")
    for i in counter.most_common():
        print(str(i[1]) + "\t" + str(i[0]).replace('\n',''))
        
def remove_file(file):
    os.remove(file)
    
def main():
    check_arguments()
    contents = pdfparser()
    name_objects = search_keywords(contents)
    sort_occurances(name_objects)
    remove_file("pdf-parser_out.txt")

if __name__ == "__main__":
    main()
