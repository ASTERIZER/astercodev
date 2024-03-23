
# Tips
- To run VScode as sudo directly to avoid frequeny sudo permissions (LINUX) - Not Recommended
  - sudo code --user-data-dir="~/.vscode-root"
- To give write permission to flders/files (LINUX)
 - chmod +w <file/folder path with name and extension>
- Set Multiple python versions as Default (LINUX)
 - "sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1"



# Installing DJANGO
- pip install django
- django-admin startproject codev .
- python manage.py startapp todo


 # Installing Node.js with Next.js
- Node Version - v18.19.1
- NPM Version - 10.2.4
- To create APP - npx create-next-app codev_web_ui
- Export and Build - npm run build
  -Export build to custom folder, modify under "scripts" in package.json - "Export"-key
    - also edit "next.config.js"


# Git Commands (LINUX)
**To Clone (as per latest update no HTTPS supported, hence use SSH key approach), create ssh key of your machine**
  - ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
  <Skip pass phrase if not required>
**Run ssh agent**
  - eval "$(ssh-agent -s)"
**Add SSH private key to the SSH agent**
  - ssh-add ~/.ssh/id_rsa
**Open Git configuration file (~/.gitconfig) in a text editor and make sure it's configured to use SSH. If not, we can set it up by running:** (Optional)
  - git config --global url."git@github.com:".insteadOf "https://github.com/"
**Copy SSH public key to the clipboard:**
  - cat ~/.ssh/id_rsa.pub | xclip -selection clipboard 
**Configure SSH Key in Visual Studio Code**
  - Open Visual Studio Code, go to the Command Palette (Ctrl+Shift+P or Cmd+Shift+P), and type "Git: Clone". Select "Git: Clone" from the list, and when prompted for the repository URL, paste the SSH URL of the repository you want to clone (e.g., git@github.com:username/repository.git). Visual Studio Code should now use your SSH key for authentication when cloning and pushing to Git repositories.