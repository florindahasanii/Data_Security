import argparse
import datetime

#initialising the parser
parser = argparse.ArgumentParser(description="Encode and Decode Morse code With this Command Line Tool ! ",
epilog= "Tip: Add Quotes(" ") for more than one word(eg: -e \"Hello There\")")

# Arguments   
parser.add_argument('-d','--decode',dest="Morse",type=str,help="Decode Morse to Plain text .")
parser.add_argument('-e','--encode',dest="text",type=str,help="Encode plain text into Morse code .")
parser.add_argument('-t ','--time',dest='time',action='store_true',help="Shows the current time,JustForFun! :)")
parser.add_argument('-v','--version',dest='version',action='store_true',help="Show the program version and exit.")
#calling the parser
args = parser.parse_args()


# Translation 
EncD = {'A':".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..",
     "J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-",
     "W":".--","X":"-..-","Y":"-.--","Z":"--.."}

DecD = {".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E",
        "..-.":"F","--.":"G","....":"H","..":"I",".---":"J","-.-":"K",".-..":"L","--":"M",
        "-.":"N","---":"O",".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T","..-":"U","...-":"V",
        ".--":"W","-..-":"X","-.--":"Y","--..":"Z"}

#Encode Function
text = args.text
def Encode(text):
    text = text.upper()
    text = text.split()
    try:
        for i in text:
            for j in i:
                j = EncD[j]
                print(j,end=" ")
    except KeyError:
        print("\n[!] Numbers or Special characters are Not allowed in Morse.")

#Decode Function
code = args.Morse
def Decode(code):
    code = code.split()
    try:
        for i in code:
            i = DecD[i]
            print(i,end=" ")
    except KeyError:
        print("\n[!] Invalid or Special characters Found in Text .")

# Conditions
if args.version:
    print("version -> V1.0/2020")
if args.time:
    now = datetime.datetime.now()
    print(now)        
if args.text :
    Encode(args.text)
    print( "\n")
if args.Morse :
    Decode(args.Morse)
    print( "\n")

# <--------------Coded By Anirudh--------------->
            
