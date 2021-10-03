.# v0.1
* Pure Python
* Distributable as single binary (Pyinstaller)
* SQLite3 DB to cache known documents by deal and cache serialized LawDoc objects for faster retrieval
* JSON for config
* Build and installer scripts that update version info
* rex is not a version control system
* User customization of e.g. homophone traps ("statute"/"statute") etc. in the config.json

## Commands

* Version
	
	$ rex --version

* Run core ctrl-Fs

	$ rex typos -d "myDocumentName.docx" 

	-d arg optional. If no active doc set, prompt user to set one

* Status: Identify current document and list all documents associated with this deal
	
	$ rex status

* Add doc to deal:

	$ rex add myfilename.extension

* Change deal:

	$ rex checkout [-d] myDealName

	-d arg analogous to git checkout -b to create new branch

## Core typo checks:

### Workflow:
* Save local backup
* Run ctrl fs

### Traditional ctrl-fs:
* MS word spell check
* isBalanced(x) for x in ["(", "[", "{"]
* List of dates and their context info for manual review
* List of core business symbols and their context for manual review:
	["$", "%", ",000", "€", "£"]
* List of "provideds" and similar for manual review of formatting uniformity
* "Compiling" related strings for manual review:
	["Exhibit", "Schedule", "Annex"]
* "the any"
* "the such"
* >1 consecutive any punctuation symbol
* See old lawdoc\_models.py LawDoc.nvr\_regexes 
* Red fonts
* Other non black fonts
* Strikethrough font
* Highlighting
* Comments
* Track changes
