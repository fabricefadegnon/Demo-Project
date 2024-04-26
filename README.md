## Create a new repository on the command line

echo "# Demo-Project" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/fabricefadegnon/Demo-Project.git
git push -u origin main

## Push an existing repository from th command line

git remote add origin https://github.com/fabricefadegnon/Demo-Project.git
git branch -M main
git push -u origin main
