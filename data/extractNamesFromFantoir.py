#!/usr/sfw/bin/python
# -*- coding: utf-8 -*-

import glob, os, re, requests, sys, time, zipfile

"""
extractNamesFromFantoir, a script to automatically extract a list of names from Fantoir files

Copyright (c) 2022-2024 Philippe Gambette

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

"""
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
"""

"""
# Get the list of all text files
outputFile = open("files.js", "w", encoding="utf-8")
outputFile.writelines("let file = [\n")
for file in files:
   outputFile.writelines("'" + file + "',\n")
outputFile.writelines("]")
outputFile.close()
"""

names = {}

searchedNames = [
"MARGUERITE YOURCENAR",
"SIMONE WEIL",
"CHRISTINE DE PIZAN|CHRISTINE DE PISAN|CHRISTINE PISAN",
"REINE MARGUERITE|MARGUERITE DE VALOIS|REINE MARGOT",
"LOUISE MICHEL",
"ZINAIDA HIPPIUS",
"MME DE SCUDERY|MADAME DE SCUDERY|MADELEINE DE SCUDERY",
"MARIE DE FRANCE",
"EMMANUELLE RIVA",
"LOUISE LABE|LOUISE LABBE",
"ANNA DE NOAILLES|COMTESSE DE NOAILLES",
"ELSA TRIOLET",
"MARIE LAURENCIN",
"DESBORDES-VALMORE|DESBORDES VALMORE",
"BARBARA",
"MARIE D’AGOULT",
"DORA MAAR",
"NINA BERBEROVA",
"SAVITRI DEVI",
"ANNA LAETITIA BARBAULD",
"JULIETTE ADAM",
"DELPHINE DE GIRARDIN",
"NATALIA GORBANEVSKAIA",
"ETEL ADNAN",
"ANDREE CHEDID",
"MARIE DE CLEVES",
"MARGUERITE PORETE",
"MARIE DE GOURNAY",
"MARIE SKOBTSOV",
"MARTHE BIBESCO",
"NADEZHDA TEFFI",
"JUDITH GAUTIER",
"LAURE DE SADE",
"AUGUSTA HOLMES",
"HELENE VACARESCO",
"LOUISE BERTIN",
"THIROUX D ARCONVILLE",
"SOPHIE CHERON|ELISABETH CHERON",
"MARIE NOEL",
"BEATRIX BECK",
"LOUISE DE VILMORIN",
"LOUISE COLET",
"DES HOULIERES|DESHOULIERES",
"DELARUE-MARDRUS|DELARUE MARDRUS",
"JACQUELINE PASCAL",
"EUGENIE DE GUERIN",
"JOYCE MANSOUR",
"ALBERTINE SARRAZIN",
"MARY DUCLAUX",
"CATHERINE POZZI",
"TIBORS DE SARENOM",
"LOTTE H. EISNER",
"PERNETTE DU GUILLET",
"MELANIE HAHNEMANN",
"MARIE DE HEREDIA",
"GRETA KNUTSON",
"MARIE DE VENTADOUR",
"L HERITIER DE VILL",
"SAINTPOINT|SAINT POINT|SAINT-POINT",
"CLAIRE GOLL",
"ROSEMONDE GERARD",
"CHARLOTTE DELBO",
"CATHERINE DE VILLEDIEU",
"ANNE DE ROCHECHOUART DE MOR",
"DE SALM|DE THEIS",
"CATHERINE DE PARTHENAY",
"FANNY DE BEAUHARNAIS",
"DE ZUYLEN",
"VALENTINE PENROSE",
"JEANNE LOISEAU",
"GINA PELLON",
"CATHERINE BERNARD",
"NINA DE CALLIAS",
"DUFRENOY",
"JULIA DAUDET",
"BONAPARTE-WYSE|BONAPARTE WYSE",
"KSENIA BOGOUSLAVSKAIA",
"ADRIENNE MONNIER",
"ANJELA DUVAL",
"ALMUCS DE CASTELNOU",
"ARIADNA SCRIABINA",
"PHILADELPHE DE GERDE",
"MALVINA BLANCHECOTTE",
"CLOTILDE DE VAUX",
"AMELIE GEX",
"HELISENNE DE CRENNE",
"CHARLOTTE-ROSE DE CAUMONT|CAUMONT LA FORCE",
"ANDRE CORTHIS",
"RENEE DUNAN",
"SOPHIE D'ARBOUVILLE|SOPHIE D ARBOUVILLE",
"NATALIA MEDVEDEVA",
"LOUISA SIEFERT",
"FORTUNEE BRIQUET",
"FRANCOISE PASCAL",
"LOMBARDA",
"CLAUDE CATHERINE DE CLERMONT",
"SUZANNE BRIET",
"GENEVIEVE LAPORTE",
"AMABLE TASTU",
"MISS.TIC",
"MARIE HUOT",
"MARGUERITE BURNAT-PROVINS",
"ELISA MERCOEUR",
"NIVARIA TEJERA",
"AURORA CORNU",
"ALICE RAHON",
"LAURENCE ICHE",
"ANNE-MARIE ALBIACH",
"CHRISTINE BROOKE-ROSE|CHRISTINE BROOKE ROSE",
"GORMONDA DE MONPESLIER",
"JANE DE LA VAUDERE",
"ANNE-MARIE CAZALIS",
"RAISSA MARITAIN",
"MARTINE BRODA",
"ISEUT DE CAPIO",
"ECKMUHL DE BLOCQUEVILLE",
"CECILE SAUVAGE",
"DANIELLE COLLOBERT",
"GERMAINE BEAUMONT",
"NICOLE ESTIENNE",
"MADELEINE VERNET",
"CLEMENCE ROBERT",
"KATIA GRANOFF",
"MIREILLE HAVET",
"CLOTILDE DE SURVILLE",
"MICHELE CAUSSE",
"FAURE-GOYAU|FAURE GOYAU",
"CLÉMENCE DE BOURGES",
"JULIETTE ROCHE",
"COLETTE PEIGNOT",
"MADELEINE DES ROCHES|MADELEINE DESROCHES",
"LEOCADIE HERSENT|LEOCADIE PENQUER",
"ANDREE BRUNIN",
"JACQUELINE RISSET",
"AGATHE-SOPHIE SASSERNO",
"CATHERINE DES ROCHES|CATHERINE DESROCHES",
"FELICIE D'AYZAC|FELICIE D AYZAC",
"DJAMILA AMRANE-MINNE|DJAMILA AMRANE MINNE",
"DEWE GORODEY",
"HELENE OETTINGEN",
"IDA FAUBERT",
"CELINE ARNAULD",
"JEAN BERTHEROY",
"JEANNE METTE",
"JEANNE DE FLANDREYSY",
"MARCELLE DELPASTRE",
"GEORGETTE DE MONTENAY",
"JOSEPHINE-BLANCHE BOUCHET",
"ANAIS SEGALAS",
"GUILLELMA DE ROSERS",
"RAISSA BLOCH",
"GEORGETTE VALLEJO",
"ROSA BAILLY",
"LYDIA YUDIFOVNA BERDYAEV",
"LOUISE ANASTASIA SERMENT|LOUISE-ANASTASIA SERMENT",
"SUZANNE RENAUD",
"AMELIE MESUREUR",
"JEHANNE D’ORLIAC|JEHANNE D ORLIAC",
"LISE DEHARME",
"HERMINIE DE LA BROUSSE DE VERTEILLAC",
"ANNE DE LA VIGNE",
"ODILE CARADEC",
"HENRIETTE BOURDIC-VIOT",
"HERMANCE LESGUILLON",
"EDMEE DELEBECQUE",
"JEANINE BAUDE",
"JEANNE FLORE",
"JEANNE PERDRIEL-VAISSIERE",
"MELANIE WALDOR",
"GABRIELLE SOUMET",
"PHILOMENE CADORET",
"MARIE-CLAIRE BANCQUART",
"MARIETTA MARTIN",
"LOUISA PAULIN",
"TOLA DORIAN",
"VICTOIRE BABOIS",
"ELISABETH GUIBERT",
"CHARLOTTE DUPLESSIS-MORNAY",
"NICOLETTE HENNIQUE",
"MARIE ATMADJIAN",
"ISEULT GONNE",
"MARYA CHELIGA-LOEWY",
"GILBERTE H. DALLAS",
"LUCILE DE CHATEAUBRIAND",
"HERA MIRTEL",
"MARIE-MARGUERITE BRUN",
"CHARLOTTE SAUMAISE DE CHAZAN",
"SAFIA KETOU",
"SUZON DE TERSON",
"CATHERINE D'AMBOISE",
"SUZANNE VERDIER",
"MICHELE DESBORDES",
"DE BEAUFORT D'HAUT|DE BEAUFORT D HAUT",
"ANNE DE ROHAN",
"MARIE-PAULINE MARTIN|MARIE PAULINE MARTIN",
"ADINE RIOM",
"ALEISSANDRINO BREMOUND",
"MYRIAM WARNER-VIEYRA|MYRIAM WARNER VIEYRA",
"FANNY DENOIX|FANNY DES VERGNES",
"GENEVIEVE IMME",
"NICOLE DE LA CHESNAYE",
"CLAIRE HUCHET-BISHOP",
"LYA BERGER",
"CORA LAPARCERIE",
"YANETTE DELETANG-TARDIF",
"JULIENNE SALVAT",
"LILIANE ATLAN",
"LINA RITTER",
"LUCILE MESSAGEOT",
"ROSE-CELESTE BACHE",
"CLARDELUNA",
"CARMEN BERNOS DE GASZTOLD",
"BLANCHE SAHUQUE",
"MADAME DE LAUVERGNE",
"ELISE MOREAU",
"EMILIE ARNAL",
"MARIE DAUGUET",
"CECILE PERIN",
"HELENE PICARD",
"MARIE-BEATRICE DE BAYE",
"MARIE DE SORMIOU",
"EVA SAARY",
"ANNE OSMONT",
"MICHELLE LEGLISE",
"EVA JOUAN",
"ANNE DE GRAVILLE",
"MARIA POIRE",
"MARIE-MAGDELEINE DE BONAFONS",
]

#"""
# Store addresses by year
yearFiles = {}

# Looking for specific names
foundNames = {}
outputFoundNames = open("nomsTrouves.csv", "w", encoding="utf-8")

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
         
         #if (nom[0:2] != "D'") and (nom[0:3] != "DE ") and (nom[0:3] != "DU ") and (nom[0:4] != "DES "):
         # Looking for specific names
         for chaineAChercher in searchedNames:
          for nomAChercher in chaineAChercher.split("|"):
           if nomAChercher in nom:
            #print("Trouvé " + nomAChercher + " dans " + nom + " !")
            """
            if nom in names:
               names[nom] += 1
            else:
               names[nom] = 1
            """
            annee = res.group(4)
            #print(annee)
            #if annee != "1987" and annee != "0000" :
            
            # Looking for specific names
            if not(nomAChercher in foundNames):
               foundNames[nomAChercher] = []
            outputFoundNames.writelines(nomAChercher + "\t" + nom + "\t" + res.group(1)+res.group(2) + "\t" + annee + "\n")
            
            if int(annee) > 1999 :
               insee = res.group(1)+res.group(2)
               
               if nom in names:
                  names[nom] += 1
               else:
                  names[nom] = 1

# Looking for specific names
outputFoundNames.close()

# Store names
names = dict(sorted(names.items(), key=lambda item: item[1]))

outputFile = open("names.csv", "w", encoding="utf-8", errors="ignore")
for name in names:
   outputFile.writelines(name + "\t" + str(names[name]) + "\n")
outputFile.close()