# Rafael Corsi @ insper.edu.br
# /2018
# Disciplina Elementos de Sistemas
#
# Abril/2018

import os
import argparse
import fileinput
import subprocess
<<<<<<< HEAD
=======
import string
>>>>>>> upstream/master

TAB = "    "
END = "\n"

TCL_FILE = "atualizaMemoria.tcl"

<<<<<<< HEAD

=======
>>>>>>> upstream/master
def setMifFile(mif, tclFile):
        for line in fileinput.input(tclFile, inplace = 1):
            if "set MIF" in line:
                print('set MIF "{}"'.format(mif))
            else:
                print(line.rstrip())

<<<<<<< HEAD
=======

>>>>>>> upstream/master
def setJTAG(value, tclFile):
        for line in fileinput.input(tclFile, inplace = 1):
            if "set JTAG" in line:
                print('set JTAG "{}"'.format(value))
            else:
                print(line.rstrip())


def getJtagPort():
    proc = subprocess.Popen("jtagconfig", stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
<<<<<<< HEAD
    h = str(out[2:20])
    h = h[3:15] + '\\' + h[15:19] + '\\' + h[19:-1]
=======
    if os.name is "posix" :
        h = str(out[2:20])
        h = h[3:15] + '\\' + h[15:19] + '\\' + h[19:-1]
    else:
        h = str(out) 
        h = h[5:17]+'\\' + h[17:23]+'\\]'
>>>>>>> upstream/master
    print(h)
    return(h)


def writeROM(mif):
<<<<<<< HEAD
    TCL = os.path.dirname(os.path.abspath(__file__))+"/"+TCL_FILE
=======
    TCL = os.path.join((os.path.dirname(os.path.abspath(__file__))), TCL_FILE)
>>>>>>> upstream/master

    # verifica se o .mif existe
    mif = os.path.abspath(mif)

    if not os.path.isfile(mif):
        print("Arquivo {} não encontrado".format(mif))
        return(1)
<<<<<<< HEAD
=======

    mif = mif.replace('\\', '/')
>>>>>>> upstream/master
    setMifFile(mif, TCL)

    print(mif)
    print(TCL)

    port = getJtagPort()
    setJTAG(port, TCL)

    #os.system("quartus_stp -t "+TCL)
    proc = subprocess.Popen("quartus_stp -t "+TCL, stdout=subprocess.PIPE, shell=True)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--mif" , required=True, help="arquivo de entrada memoria")
    args = vars(ap.parse_args())
    root = os.getcwd()
    writeROM(mif=args["mif"])
