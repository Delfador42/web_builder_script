#! /usr/local/bin/python3 
#CHANGE: This will be different in pcte

"""

STEPS TO ADD PAGE

Notes:
Make the new page name a variable

/src/pages
* cp Page1.js Page3.js
* Rename file being imported to new file

/src/components/Routes.js
* Import new page
* add element to route array with new page name

/src/App.js
* Replace filename array with new array with new filename
* copy <li> line, replace number with new page number

"""

import os
from os import listdir
from os.path import isfile, join


# Directory that stores pdf files
pdf_dir='/Users/Tal/work/blog_website/script/files' #***CHANGE***

# All files in pdf_dir
files = [f for f in os.listdir(pdf_dir) if isfile(join(pdf_dir, f))]

def trackpdfs(file_name):
  # Create file to track pdfs in pdf_dir
  with open(file_name, 'w') as f: 
    for file in files:
      if file.endswith('.pdf'):
        f.write(file+"\n")
  f.close()

def create_file_list(file_name):
  f = open(file_name, "r")
  pdfs = f.read().splitlines()
  f.close()
  return(pdfs)

"""
Take the current list of pdfs and modify the website to make it for each pdf
You are only putting the file name in the page the rest is just the uniName
But first you have to recognize that a change was even made
Q: How to recognize if a file was added, deleted, or renamed in directory
A: renamed equals -1 +1, added +1, deleted -1
Make a count of the current number of files, but then you won't catch the renamed cases
Make a list of current and old, if they are not the same update, you don't need to know the specific changes made just use the new list, you only need to compare to trigger an update to the website
"""

def update_website():
  # Create an list of files from current_pdfs and track_pdf_files
  current_pdfs = create_file_list('current_pdfs')
  old_pdfs = create_file_list('track_pdf_files')
  print(current_pdfs)
  print(old_pdfs)
  current_pdfs.sort()
  old_pdfs.sort()
  print(current_pdfs)
  print(old_pdfs)
  if current_pdfs == old_pdfs:
    return False
  else:
    return True



def build_pagejs():

  page_num = 1 # Page Count
  pages_dir = "/Users/Tal/work/blog_website/script/pages" #***CHANGE***
  if not os.path.exists(pages_dir):
    os.system(f"mkdir {pages_dir}")

  # Create a list of current pdfs from the current_pdfs file
  current_pdfs = create_file_list('current_pdfs')

  # Create a Page#.js for each pdf in the pdf_dir
  for pdf in current_pdfs:
    page1 = """import React, { Component } from 'react';"""
    page2 = f"""\nimport Pdf from '../files/{pdf}';"""
    page3 = """\nexport default function Page1() {

      return (
          <div className = "pdf_container">
              <object data={Pdf} type="application/pdf" width="100%" height="100%"></object>
          </div>
        );
  }
  """
    page = page1+page2+page3
    page_name = pages_dir+"/Page"+str(page_num)+".js"
    page_num += 1

    # Create Page#.js in pages_dir
    with open(page_name, 'w') as f: 
          f.write(page)
    f.close()

  # Create the home page in the pages_dir
  home_page = """export default function Home() {
      return <h1>Home</h1>
  }
  """
  home_page_name = pages_dir+"/Home.js"
  with open(home_page_name, 'w') as f: 
        f.write(home_page)
  f.close()


# Build Routes
def build_routesjs():
  routejs = "/Users/Tal/work/blog_website/script/components/Routes.js" #***CHANGE***

  page_num = 1
  import_string = """import Home from "../pages/Home" """
  routes_string = """export const routes = [\n{path: "/",main: () => <Home />,},"""

  # Create a list of current pdfs from the current_pdfs file
  current_pdfs = create_file_list('current_pdfs')

  # Build import string
  for pdf in current_pdfs:
    import_string += f"""\nimport Page{page_num} from "../pages/Page{page_num}";"""
    routes_string += f"""\n{{path: "/Page{page_num}",main: () => <Page{page_num} />,}}, """
    page_num += 1
  routes_string += "\n];"

  with open(routejs, 'w') as f: 
        f.write(import_string+"\n")
        f.write(routes_string)
  f.close()


# Create a file of current pdfs
trackpdfs('current_pdfs')



# Check for changes to files (ie, rename, deletions, additions)
# Rebuild the site with list of pdfs every time a change is made
# Compare lists 
if update_website():
  print("The website updates")
  #print(build_page())
else:
  print("The website does not update")

build_pagejs()
build_routesjs()
"""
* You can build each page with f multi-line strings
* Build the pages directory from scratch
* Use multi-line strings to build the routes
* Build the App.js
"""



# Update track_pdf_files with current list of pdfs in pdf_dir
trackpdfs('track_pdf_files')


