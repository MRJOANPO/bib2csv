import pandas as pd
import pandas as pd
from pybtex.database import parse_file

def bib2csv(pBibFile, pExport):
    totalData = []
    bib_data = parse_file(pBibFile, "bibtex")
    for latexKey in bib_data.entries:
        
        # Data for current Entry
        currentData = bib_data.entries[str(latexKey)]

        # Collect Autor or Editors
        peopleInvolved = currentData.persons
        authorsText = ""
        if "author" in peopleInvolved:

            for author in peopleInvolved["author"]:
                authorsText += str(author)
                authorsText += "; "

        if "editor" in peopleInvolved:

            for author in peopleInvolved["editor"]:
                authorsText += str(author)
                authorsText += "; "

        # Latex Type: book, chapter, etc.
        latexType = currentData.type

        # Get Title if given
        if "title" in currentData.fields:
            entryTitle = currentData.fields["title"]
        else:
            entryTitle = ""

        # Get a URL if given
        if "url" in currentData.fields:
            entryUrl = currentData.fields["url"]
        else:
            entryUrl =  ""

        # Get Keywords
        if "keywords" in currentData.fields:
            keywordsEntry = currentData.fields["keywords"]
        else: 
            keywordsEntry = ""
        
        entryData = [latexKey, latexType, authorsText, entryTitle, entryUrl, keywordsEntry]
        totalData.append(entryData)

    # Create Dataframe 
    columnNames  = ["Latex Key", "Latex Type", "Autoren/Editor", "Titel", "URL", "Schlagwörter"]
    df = pd.DataFrame(data=totalData, columns=columnNames)
    df.to_csv(pExport)