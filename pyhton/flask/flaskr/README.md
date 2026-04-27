<!-- Goto my workspace -->
`cd C:\Users\subah\works\basics`
<!-- Clone my repo -->
`git clone https://github.com/asgeeketteamber/basics.git`
<!-- create sub project directory  -->
`mkdir flaskr`
`cd flaskr`
<!-- Create  virtual env -->
`python -m venv .venv`
<!-- Create requirement.txt and install requirments-->
 `.\.venv\Scripts\Activate.ps1`
 `pip install  -r requirment.txt`
 `cd ..`
 <!-- Initialize database  -->
`flask --app flaskr init-db`
 <!--Run the app  -->
`flask --app "flaskr:create_app" --debug run`

