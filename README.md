# fproc
Browser fingerprint mitigation system

### Disclaimer ###
This tool is experimental and still in development. We work on the basis of the [Blink](https://github.com/plaperdr/blink-docker) tool.

### Requirements ###
**Docker**, **Python 3** and **gcc** are needed to build the mitigation system.  

**Python 3 and gcc**  
For Fedora: `sudo yum install python3 gcc`  
For Ubuntu/Debian: `sudo apt-get install python3 gcc`  

**Docker**  
For Fedora: [Link](https://docs.docker.com/install/linux/docker-ce/fedora/)  
For Debian: [Link](https://docs.docker.com/install/linux/docker-ce/debian/)  
For Ubuntu: [Link](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

It is recommended to have at least **2GB** of free hard drive space to install every components.

### Quick install ###
If you want to try the system, here are 4 simple commands to get it running:
```
git clone https://github.com/agomezboix/fproc.git
cd fproc/
python3 downloadFromHub.py
python3 run.py
```
### Installation ###
The **downloadFromHub.py** script is now the recommended method of installation. It downloads the main images directly from Docker Hub.
You can also run the **installContainers.py** script to build from scratch. The process can take some time depending on your internet connection.

### Running ###
Run the **run.py** and it will launch a browsing platform on the fly in a matter of seconds. The script builds the final Docker image and launches the container.

A browser fingerprint is required to run the system. This fingerprint contains the configuration of the web browser to be built. The fingerprint is provided through the **fp** file. By default it is provided a browser fingerprint.

### Constrains ###
The recommended values for the operating system and the platform/architecture are ignored. Instead, all web browsers run on Ubuntu 18.04, in an architecture x86-64.

### Windows and MacOS support ###
Windows and MacOS are not officially supported yet.

### Docker images and containers ###

2 images are downloaded from Docker Hub (or can be built from scratch)
* gomezboix/ubuntu-origin
* gomezboix/ubuntu-browsers

1 images is built locally during the execution
* fproc/ubuntu-fproc
