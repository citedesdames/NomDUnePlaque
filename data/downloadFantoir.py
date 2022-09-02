#!/usr/sfw/bin/python
# -*- coding: utf-8 -*-

import glob, os, re, requests, sys, time, zipfile

"""
downloadFantoir, a script to automatically download Fantoir files for NomDUnePlaque

Copyright (c) 2022 Philippe Gambette

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

# Get the current folder
folder = os.path.abspath(os.path.dirname(sys.argv[0]))

#"""
# Get the list of ZIP files to download
print("Downloading list of files from https://www.collectivites-locales.gouv.fr/competences/la-mise-disposition-gratuite-du-fichier-des-voies-et-des-lieux-dits-fantoir")
response = requests.get("https://www.collectivites-locales.gouv.fr/competences/la-mise-disposition-gratuite-du-fichier-des-voies-et-des-lieux-dits-fantoir")
open(os.path.join(folder,"fantoir.html"), 'wb').write(response.content)
zipList = open("fantoir.html", "r", encoding="utf-8", errors="ignore")

# Download all ZIP files
files = []
for line in zipList:
   res = re.search("<a href=./files/Comp%C3%A9tences/5.%20am%C3%A9nagement%20de%20mon%20espace/1-cadastre/fantoir2022/zip/([^/]+).zip.>fichier .zip</a>", line)
   if res:
      file = res.group(1)
      fileName = file.replace("%20","_").replace("%C3%A9","e")
      print("Downloading file " + fileName + ".zip")
      print("https://www.collectivites-locales.gouv.fr/files/Comp%C3%A9tences/5.%20am%C3%A9nagement%20de%20mon%20espace/1-cadastre/fantoir2022/zip/" + file + ".zip")
      response = requests.get("https://www.collectivites-locales.gouv.fr/files/Comp%C3%A9tences/5.%20am%C3%A9nagement%20de%20mon%20espace/1-cadastre/fantoir2022/zip/" + file + ".zip")
      open(os.path.join(folder, "fantoir-" + fileName + ".zip"), 'wb').write(response.content)
      # Extract the content of the ZIP file
      with zipfile.ZipFile("fantoir-" + fileName + ".zip", 'r') as zip_ref:
         zip_ref.extractall(".")
      newFolder = file.replace("%20"," ").replace("%C3%A9","é")
      # Move all extracted text files to the parent folder
      for f in glob.glob(os.path.join(os.path.join(folder, newFolder),"*.txt")):
         f = os.path.basename(f)
         print(os.path.join(os.path.join(folder, newFolder), f))
         print(os.path.join(folder, f))
         os.replace(os.path.join(os.path.join(folder, newFolder), f), os.path.join(folder, f))
         files.append(f)
      time.sleep(1)
#"""

"""
# Get the list of all text files
outputFile = open("files.js", "w", encoding="utf-8")
outputFile.writelines("let file = [\n")
for file in files:
   outputFile.writelines("'" + file + "',\n")
outputFile.writelines("]")
outputFile.close()
"""

"""
# Store addresses by year
yearFiles = {}
outputFileDe = open("file-DE.js", "w", encoding="utf-8")
for annee in range(1988,2023):
   outputFile = open("file-" + str(annee) + ".js", "w", encoding="utf-8")
   yearFiles[str(annee)] = outputFile
outputFile.writelines("let yearData = [\n")
for txtFile in glob.glob(os.path.join(folder,"*.txt")):
   print("Extracting dates from file " + txtFile)
   inputFile = open(txtFile, "r", encoding="utf-8", errors="ignore")
   for line in inputFile:
      res = re.search("^(..).(...).........(...........................).......................................(....)...", line)
      if res:
         nom = res.group(3)
         res2 = re.search("([ ]*)$", nom)
         if res2:
            nom = nom[0:len(nom)-len(res2.group(1))]
         if (nom[0:2] != "D'") and (nom[0:3] != "DE ") and (nom[0:3] != "DU ") and (nom[0:4] != "DES "):
            annee = res.group(4)
            #print(annee)
            if annee != "1987" and annee != "0000" :
               insee = res.group(1)+res.group(2)
            
               yearFiles[annee].writelines('[' + insee + ',"' + nom + '"],\n')
         else:
            outputFileDe.writelines(nom + '\n')
for file in yearFiles:
   yearFiles[file].writelines(']')
   yearFiles[file].close()
   outputFileDe.close()
"""

   
# Store addresses by INSEE code
for txtFile in glob.glob(os.path.join(folder,"*.txt")):
   print("Extracting dates from file " + txtFile)
   folderName = os.path.basename(txtFile)
   if folderName[0:2] == "97":
     folderName = folderName[0:3]
   else:
     folderName = folderName[0:2]
   if folderName[0:2] == "CA":
     folderName = "973"
   print("Creating folder " + folderName)
   try:
     os.mkdir(folderName)
   except:
     print("Already exists")
   
   inputFile = open(txtFile, "r", encoding="utf-8", errors="ignore")
   currentFile = open(txtFile, "r", encoding="utf-8", errors="ignore")
   previousINSEE = ""
   insee = ""
   for line in inputFile:
      res = re.search("^(..).(...)(....).(...).(...........................).......................................(....)...", line)
      if res:
         nom = res.group(5)
         res2 = re.search("([ ]*)$", nom)
         if res2:
            nom = nom[0:len(nom)-len(res2.group(1))]
         if (nom[0:2] != "D'") and (nom[0:3] != "DE ") and (nom[0:3] != "DU ") and (nom[0:4] != "DES "):
            annee = res.group(6)
            #print(annee)
            if annee != "1987" and annee != "0000" :
               previousINSEE = insee
               insee = res.group(1) + res.group(2)
               if (res.group(1) + res.group(2)) != previousINSEE:
                 # We found a new INSEE code: create new file
                 currentFile.close()
                 currentFile = open(os.path.join(folderName, insee+".json"), "w", encoding="utf-8")
               # write the new street name
               currentFile.writelines(annee + res.group(3) + res.group(4) + nom + '\n')
               #print(nom + ";" + annee)
   currentFile.close()