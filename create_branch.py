import git
import os
from git import Repo

repo = Repo('/Users/santiagosaldivar/PycharmProjects/Working-with-repo-test') #Path to remote repo
my_new_branch = repo.create_head('Branch-Demo') #Name of new branch
my_new_branch.checkout() #Switch to a different branch
origin = repo.remote('origin') #Assigning the remote repo
repo.git.push('--set-upstream', origin, repo.head.ref) #this will push the branch to the remote repo

