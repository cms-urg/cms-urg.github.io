from pybtex.database.input import bibtex
from pybtex.database import BibliographyData, Entry

#open a bibtex file
parser = bibtex.Parser()
bibdata = parser.parse_file("Harrington.bib")
projectCitationMap = {}
personCitationMap = {}
# File path for the folder where the individual html pages for each project are stored
PROJECTFILEPATH = "../../"
# File path for the folder where the individual markdown pages for each person are stored
PEOPLEFILEPATH = "../../_people/"

# initialize the citation maps
for bib_id in bibdata.entries:
    # get a bibdata.entries.fields object
    b = bibdata.entries[bib_id].fields
    try:
        # get the list of projects
        projects = b["projects"].split(",")
        # for each project create an empty list to store their citations
        for project in projects:
            projectCitationMap[project.strip()] = []
    except(KeyError):
        pass
    # get the authors
    authors = bibdata.entries[bib_id].persons["author"]
    # for each other create an empty list to store their citations
    for person in authors:
        name = person.first()[0] + person.last()[0]
        if(name not in personCitationMap.keys()):
            personCitationMap[name] = [] 

#loop through the individual references
for bib_id in bibdata.entries:
    b = bibdata.entries[bib_id].fields
    url = b['url']
    pdflink = b['pdf']

    citation="<p>"
    try:
        # create the authors section of the citation
        authors = bibdata.entries[bib_id].persons["author"]
        #print(authors)
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
        try: 
            projects = b["projects"].split(",")
            for project in projects:
                citationList = projectCitationMap[project.strip()]
                citationList.append(citation)
                projectCitationMap[project] = citationList
        except:
            pass
        
        # populate the person citation map
        for person in authors:
            citationName = person.last()[0] + ", " + person.first()[0]
            name = person.first()[0] + person.last()[0]
            if citationName in citation:
                citationList = personCitationMap[name]
                citationList.append(citation)
                personCitationMap[name] = citationList
        
        
    # field may not exist for a reference
    except(KeyError):
        continue


# for each project, append to the existing html file
for project in projectCitationMap:
    if(project != ""):
        filename = PROJECTFILEPATH + project.replace(" ", "").lower() + ".html"
        try:
            f = open(filename, "r")
            data = f.readlines()
            i = 0
            string = "Relevant Citations"
            while(i < len(data)-1 and string not in data[i]):
                i += 1
            i+=1
            listOfCitations = projectCitationMap[project]
            for c in listOfCitations:
                if(i <= len(data)-1):
                    data[i] = c + "\n"
                    i+=1
                else:
                    data.append(c + "\n")
                    i+=1
            newdata = ''.join(data)
            f = open(filename, "w")
            f.write(newdata)
            f.close()
            print("Finished updating relevant citations for project: " + project)
        except:
            print("No html file for project: " + project)
            continue

# for each person concatenate their relevant citations to their md file
for person in personCitationMap:
    filename = PEOPLEFILEPATH + person + ".md"
    try:
        f = open(filename, "r")
        data = f.readlines()
        i = 0
        string = "Relevant Citations"
        while(i < len(data)-1 and string not in data[i]):
            i += 1
        #print(data[i])
        i+=1
        
        listOfCitations = personCitationMap[person]
        for c in listOfCitations:
            c = c.replace("<p>", "<h6>")
            c = c.replace("</p>", "</h6>")
            if(i <= len(data)-1):
                data[i] = c + "\n"
                i+=1
            else:
                data.append(c + "\n")
                i+=1
        newdata = ''.join(data)
        #print(newdata)
        f = open(filename, "w")
        f.write(newdata)
        f.close()
        print("Finished updating relevant citations for " + person)
    except:
        print("No markdown file for " + person)
        continue