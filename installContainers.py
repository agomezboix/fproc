#!/usr/bin/python3
# -*-coding:utf-8 -*

from installUtils import *

def main():
    print("Containers Installation script")

    #Change current working directory
    os.chdir("docker")

    #Check to see if Docker is installed
    if "command not found" in subprocess.check_output(["sudo","docker","info"]).decode():
        sys.exit("Docker not installed. Install Docker to process with the installation.")

    #Build OS images
    buildDockerImageHub("ubuntu-origin","os/ubuntu/")
    buildDockerImageHub("ubuntu-browsers","browsers/ubuntu/")

    #Update Dockerfiles to include the right user/group ID
    #And build the final OS images
    #**********************************************************check --> updateGroupUserIDs() 
    #updateGroupUserIDs()
   # buildDockerImageNoPullLocal("ubuntu-fproc","run/ubuntu/")

    print("Installation of containers complete")

if __name__ == "__main__":
    main()