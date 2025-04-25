On Collin's machine, the github was created and 4a was implemented. Maci and Madison worked on 4b, but had issues getting it to run on their machines. We decided to run the actual code on Collin's machine and debugged / handled errors as needed. Hyunjun implemented 4c but this was also pushed from Collin's machine to overcome any disparencies in downloads. 

Collin: 1-4a
-   created the github and worked on writing a script for auto running bandit within a conda enviorment.
-   created the bandit.yaml file to exclude certain directories from being scanned
-   modified the environment.yml file to set up the conda environment for the project
-   created the README file and added team member information
-   created the githooks folder and added the pre-commit hook to run bandit before each commit

What I learned:
Having a standardized enviorment makes for easier collaboration. Initially I worked locally in a wsl running ubunutu. However, this approach is not easily transferable to other devlopers. 
Creating support files such as the yaml files makes for more consistent results. 

Utilizing the instruction and enviorment files to create github actions provides for many new possibilities with automatic scripts within github. Getting the actions to work with the existing dependencies was difficult as some are windows only and took lots of debugging to identify.

Maci: 4b
- completed 1/2 of 4c, integrated logging into scanForSecrets and scanForOverPriviledges functions in scanner.py
  Logging from scanForSecrets function provides users with the total secret-containing keys, while logging from scanForOverPriviledges function provides users with the total privilege issues.


Madie: 4b
- completed 1/2 of 4c, integrated logging into the username, password and key functions in scanner.py
  Although already done in a previous workshop, adding logging info to such a large file was helpful in checking import bodies and methods.


Hyunjun: 4c
- I implemented fuzz.py to automatically test 6 functions from scanner.py: isValidUserName, isValidPasswordName, isValidKey, checkIfValidSecret, scanUserName, and
  getYAMLFiles. A variety of test inputs (valid, invalid, empty, emoji, and special strings) were used to uncover possible bugs or input handling issues.

