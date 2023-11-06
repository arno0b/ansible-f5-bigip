# Git Beginner Commands

Git commands for pushing the files locally to the repository


### Clone the Repository
Open your terminal and clone the repository using the following command:

```sh
git clone https://your-gitea-server.com/username/repository.git
```

Replace ```https://your-gitea-server.com/username/repository.git``` with the URL of your Gitea repository.

### Navigate to the Repository Directory
Change into the directory that was created by the clone operation:

```sh
cd repository
```
Replace ```repository``` with the actual name of your repository directory.

### Create a New Branch
It's a good practice to create a new branch for your changes. You can do this with:

```sh
git checkout -b test
```
Replace ```test``` with the name you want for your new branch.

### Copy the Required Files
Use the cp command to copy files from your desired directory to the repository directory:

```sh
cp /path/to/your/files/* /path/to/repository/
```
Replace ```/path/to/your/files/*``` with the path to your files and ```/path/to/repository/``` with the path to your repository directory.

### Add the Files to Git
Add the new files to your local Git repository for staging:

```sh
git add .
```
The . tells Git to add all the files in the current directory.

### Configure your Git user
Set up your Git configuration with your username and email

```sh
git config --local user.name "saadman.arnob"
git config --local user.email "saadman.arnob@bkash.com"
```
```--local``` means these settings are applied to the specific repository you are currently working in. They are stored in ```.git/config``` in the repository's directory.
Now, whenever you commit to a Git repository, your commits will be attributed to the name ```"saadman.arnob"```. 

### Commit the Changes
Commit the changes to your local repository:

```sh
git commit -m "Add initial project files"
```

### Push the Changes to Gitea
Push your new branch and changes to the Gitea server:

```sh
git push -u origin test
```
Replace ```test``` with the name of the branch you created. The ```-u``` flag sets the upstream for your branch, so in the future, you can simply use git push or git pull without specifying the branch.
