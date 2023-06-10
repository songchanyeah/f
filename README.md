==================== VIRTUAL ENVIRONMENT ====================
1. create a virtual environment
python -m venv "name of the venv"

2. dir 
list out everything on my desktop
can only see flaskblog-venv

3. activate
flaskblog-venv\Scripts\activate

4. where python
path to current python command, venv directory
same as the python you used to create the venv

5. pip list
list of packages installed

6. pip freeze
copy and put it into requirements.txt file

7. pip install -r requirements.txt

8. deactivate

9. delete venv
rmdir "name of the venv directory" 





==================== RUNNING FLASK ====================
1. cd Flask_blog which has flaskblog.py

2. <windows> set FLASK_APP=flaskblog.py -> this did not work
use this instead -> $env:FLASK_APP="flaskblog.py"

3. flask run

4. $env:FLASK_DEBUG=1
*FLASK_DEBUG* -> you don't have to restart the app to renew small changes.

*FLASK_APP* -> you have to restart the app to laod new changes.

5. flask run
