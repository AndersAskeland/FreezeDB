# FreezeDB <img src="graphics/logo.png" align="right" width="120" />

## Overview

FreezeDB is a simple GUI application written in Python that can be used to manage (add, delete, edit) clinical samples in freezer storage. It uses sqlite3 files to manage data storage and editing. 

The database element is managed by SQLAlchemy ORM. The GUI elements are written using Qt for Python (PySide6).

The application is still in development, pending a larger rewrite, using more object-oriented programming style. Hence, not all features are fleshed out. Current version is 0.0.1.

### Features included
* Create databases
* Delete databases
* Add samples to database
* Delete samples from database
* GUI layout
* View sample distribution in pie-charts. This feature is currently messy and written by hand as the QtGraph library is not at present included in PySide6. It will be rewritten to feature interactive graphs when PySide6 adds this functionality.
* Basic stats 
* Basic settings system using "ConfigParser".

### Upcoming features
* Dynamic database created with self-defined sample types and groups.
* More data visualization methods
* Export data to CSV. This is simple and quick, but I don’t have time right now.
* User definable settings.
* Built versions for MacOS and windows.


## Information
Git commit messages are tagged using the following system.

```
[style]       Formatting, and typos
[doc]         Alterations to the documentation or code comments
[feature]     Added/changed feature
[fix]         Bug fixes
[clean]       Cleaned up the file structure
[test]        Testing new stuff
[major]       Major changes. Usually only used if doing a large rewrite.
