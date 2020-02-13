from pybtex.database.input import bibtex
from pybtex.database import BibliographyData, Entry

#open a bibtex file
parser = bibtex.Parser()
bibdata = parser.parse_file("Harrington.bib")
projectCitationMap= {}

for bib_id in bibdata.entries:
    b = bibdata.entries[bib_id].fields
    try:
        projects = b["projects"].split(",")
        for project in projects:
            projectCitationMap[project.strip()] = [] 
    except(KeyError):
        continue    

#loop through the individual references
for bib_id in bibdata.entries:
    b = bibdata.entries[bib_id].fields
    url = b['url']
    pdflink = b['pdf']

    citation="<p>"
    try:
        # create the authors section of the citation
        authors = bibdata.entries[bib_id].persons["author"]
        for i in range(len(authors)):
            name = authors[i].last()[0] + ", " + authors[i].first()[0] 
            if(i == len(authors)-2):
                citation = citation + name + " and "
            elif(i == len(authors)-1): 
                citation = citation + name + ". "
            else:
                citation = citation + name + ", "
        # create a link tag
        citation = citation + "<a href=\"" + b['url'] + "\">"  
        # add the title of the paper
        citation = citation + "\"" + b["title"] + ".\" " + "</a>"
        # if the journal exists, add the journal to the citation
        try:
            citation = citation + b["booktitle"] + " "
        except:
            citation = citation + ""
        #add the year to the citation
        citation = citation + "(" + b["year"] + ")."
        try:
            citation = citation + "<a href=\"" + b["pdf"] + "\">" + "[pdf]" + "</a>"
        except:
            citation = citation + ""  
        try:
            citation = citation + "<a href=\"" + b["doi"] + "\">" + "[doi]" + "</a>"
        except:
            citation = citation + ""
        citation = citation + "</p>"
        #print(citation)
        projects = b["projects"].split(",")
        for project in projects:
            citationList = projectCitationMap[project.strip()]
            citationList.append(citation)
            projectCitationMap[project] = citationList
        
    # field may not exist for a reference
    except(KeyError):
        continue


# for each project, create an html file with it's citations
for project in projectCitationMap:
    if(project != ""):
        filename = project.replace(" ", "") + "citations.html"
        f = open(filename, "w")
        listOfCitations = projectCitationMap[project]
        for c in listOfCitations:
            f.write(c + "\n");
        f.close()

    