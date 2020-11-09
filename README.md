# Exercise.py
let's python
Developer Environment Setup:
Step 1: Create a SSH Key in your local machine. Command to create a ssh key "ssh-keygen -t rsa". The Generated ssh key is stored in this location: "C:\Users\username.ssh\id_rsa.pub".

Step 2: Create a GitLab Account. Add the SSH Key to the GitLab Profile.

Step 3: Modify Hosts file in the machine to access the developer enviroment virtual machine IP's

The Location of the hostfile is mentioned below. location: "C:\Windows\System32\drivers\etc\hosts"(OPEN AND EDIT AS AN ADMINISTRATOR)

Step 4: Add the necessary IP given by the admin eg: 139.59.42.248 dev.screel.in 139.59.42.248 code.dev.screel.in 139.59.42.248 traefik.dev.screel.in 139.59.42.248 config.dev.screel.in

Step 5: Install Cygwin Download Link: https://cygwin.com/install.html

Step 6: SSH into the Cloud Based Virtual Machine. Command: "ssh coder@167.71.273.224" or "ssh coder@dev.screel.in"

Step 7: Change Directory to ohr Perform git fetch and git pull to update the repository

NOTE: change the username and email in the git config file Commands to change the username and email. git config --global user.name "FIRST_NAME LAST_NAME" git config --global user.email "MY_NAME@example.com"

To verify the Git config Command: cat .git/config

Step 8: Docker commands
Run the following commands to start the docker container

docker --version (Optional) docker ps -> To Check the running containers. docker-compose build frontend -d docker-compose build backend -d docker-compose up -d docker-compose down

Docker Command to check the logs: docker-compose log -f

Dev urls and credentials:

url: To webbased code editor. http://code.dev.screel.in [password:ohr] url: To Dev server. http://code.dev.screel.in url to the admin tool: http://config.dev.screel.in [username: admin; password:ohr] url to see the openapi swagger ui: "http://dev.screel.in/docs"
