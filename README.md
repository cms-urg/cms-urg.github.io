# CMS URG Website

> This is a Jekyll theme modified from https://github.com/koenbok/Cactus

## Creating Posts

To create a post, make a new file under `_posts` folder with standard Jekyll post format.

## Adding Members

To add a new member, follow the instructions below. 
1.	Create a new file called `FirstNameLastName.md` under the `_people` folder
2.	Next add the following content

```
---
category: faculty, student or alumni
name: Your full name
photo: Your photo URL ( which is /assets/photos/photoname.jpg)
projects: list the project names that you are involved in as it is written in the name field in the project’s md file found in the _projects folder separated by a space
citations: yes if you have any, no if you don’t
---
```
3.	If you have any relevant citations, add the line `<h6> Relevant Citations </h6>` below the `---` Execute the python script `bibtexparser.py` found in the `_pubs/bibs` folder. The script will update your md file with your citations. 
4.	Upload your photo in the `assets/photos` folder. For easy reference name the photo as `yourname.jpg`

Notes: Note the forward slash `/` before `assets` in your photo url. Make sure this is there.

## Editing Members
To edit the fields of an existing user follow the instructions below.
| Field         | Value         | 
| ------------- |:-------------:| 
| category      | Simply change the value to one of the following: faculty, student, alumni |
| name          | Simply edit your name      |
| photo         | Simply change the name of the photo in the file path      |
| projects      | To remove a project, simply remove its name, to add a project simply add it to the list separated by a space     |
| citations     | Simply change it to yes or no. If you have any citations make sure to add the line `<h6> Relevant Citations </h6>` below the `---`. Then run the python script `bibtexparser.py` in `_pubs/bibs folder`. The script will update your md file with your citations.    |

See `JunZheng.md` in the `_people` folder for an example of an markdown file for a member.

## Adding Projects

1.	Create a new file called `ProjectName.md` in the `_projects folder`
2.	Add the following content 

```
---
name: Project name
description:
    >
    Project description
    can have multiple lines
github: GitHub URL
website: https://cms-urg.github.io/projects/projectname/
---
```
3.	Create a new file called projectname.html in the root folder
4.	Add the following content to this file
```
---
permalink: /projects/projectname/
layout: default
---

{% for project in site.projects %}
  {% if project.name == 'project_name' %}
    <h1>{{ project.name }}</h1>
    <p>{{ project.description }}</p>
  {% endif %}
{% endfor %}

<h2>People</h2>
{% for person in site.people %}
    {% if person.projects contains "project_name" %}
        <div class="people-card">
            <img src="{{ person.photo }}" />
            <label>{{ person.name }}</label>
        </div>
    {% endif %}
{% endfor %}

<hr/>

<h2>Relevant Citations</h2>
```

5.	Replace `project_name` with the name of the project as it is written in the project’s md file. Note the quotations.
6.	The permalink can be found in the project’s md page in the website field. the permalink is the `/projects/projectname/`part of the following url: https://cms-urg.github.io/projects/projectname/ 
Note the forward slash before `projects` and after `projectname`. Make sure this is there. 
7.	To add relevant citations to the html file:
You will need to edit the `Harrington.bib` file found in the `_pubs/bib` folder. For each project, add the projects field. In         this field, you can add the names of the projects that the citation is relevant to. If the citation has no relevant projects, you       can omit the projects field. If there are multiple projects, simply separate them by a comma. Make sure the project names in this       field are written in the same way as it is in the project’s md file.
Execute the python script bibtexparser.py found in the `_pubs/bib` folder to add the relevant citations for the project. Make sure the html file is created and is in the root folder before executing the script.

## Editing Projects
To edit the fields of an existing user follow the instructions below.
| Field         | Value         | 
| ------------- |:-------------:| 
| name          | Simply edit the project name. If you edit the project name, make sure to update `projectname` in the url in in the website field. Change `projectname`  in the permalink in the corresponding html file. Change the name of the html file for easy reference.|
| description   | Simply edit the description       |
| github        | Simply replace the url      |
| website        | If you are editing this field, the only part that needs to be edited is `projectname`. If you do edit this part, you will need to change the `projectname` part in the permalink in the project’s html file.    |

To update the relevant citations, simply execute the python script `bibtexparser.py` found in the `_pubs/bib` folder to update the relevant citations for the project. 

See `CodeClash.md` in the `_projects` folder for an example of a markdown file for a project and `codeclash.html` in the root folder for an example of an html file for a project.

## How to Update the References Page
Simply execute the bash script `make_search_table.bash` found in the `_pubs` folder. It will create the html file `publications.html` which is the table with all the citations. This file will be found in the root folder.
