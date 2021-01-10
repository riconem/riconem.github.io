from sh import git
from subprocess import call

def git_pull():
    git("pull", "origin", "master")

def git_change():
    call('./git_changes.sh')
