# Service.ai dash application overview

**Set up**: 
+ Clone the repository to a local directory
+ Create a "data" directory in the parent directory as the index.py file
+ Download data from the box folder (link below)
+ Run the application
    + Open index.py file 
    + Run all lines in the index.py file
    + In the python console a url will be printed (e.g. Running on http://127.0.0.1:8050/)
    + Open a browser and paste the link into the URL bar to navigate to the page and see the application running. 

The data is not synced to the repository but can be found here:
+ https://mckinsey.box.com/s/8e183apdqmkzig63eab2hqsmmbcazhhy
+ https://mckinsey.box.com/s/feowu0dfav75i65wxk2ju9q7nyb4ruyo

**Usage**:
> Workflow: tabs -> pages -> index
+ Add a tab in the tabs folder
+ Add a page in the pages folder
+ Reference the layout in the index file

> App location: https://jupyterhub-9d68ffb61b6f08101ce3542d1e4bcb49.ncod.mckinsey.com/app/

If the web server is not running. Then navigate to /asset-launchpadai/ and start the web app by running sh run.sh on the terminal.

Components:
+ Tabs: /asset-launchpadai/tabs/ contains individual tabs for the app
+ Pages: /asset-launchpadai/pages/ contains hyperlinked pages of the app and brings all the pages together for a specific layout
+ /asset-launchpadai/index.py brings all the pages together
+ /asset-launchpadai/app.py contains app configuration
+ /asset-launchpadai/app/ contains templates which is used for defining the structure of the web app and also the charting templates to add plotly viz
+ /asset-launchpadai/run.sh script to run the web server which uses JH token to host it on the Jupyter hub

## Authors
+ Mark Huntington (Initial work)
+ Pavan Naidu  
