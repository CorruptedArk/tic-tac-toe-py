# tic-tac-toe-py
## Description
tic-tac-toe-py is a simple terminal tic tac toe game written in Python

## Usage
If installed on your system, you run it as `tictactoe`
If not installed, run `python3 -m tictactoe` from this git project root directory. 

## Installation
To install without a distro specific package, run `make install` from the project root directory

### Debian Package (Coming Soon)
You can install it from my [PPA](https://launchpad.net/~corruptedark/+archive/ubuntu/ppa).

#### On Ubuntu 20.04+ based distros 
To add the repository to your system, run:
```
sudo add-apt-repository ppa:corruptedark/ppa
sudo apt update
```
After adding the repository, install the package with: 

`sudo apt install python3-tictactoe`

#### On Debian Buster
First install `software-properties-common`
	
Then to add the repository to your system, run:
```
sudo sh -c 'echo "deb http://ppa.launchpad.net/corruptedark/ppa/ubuntu focal main\ndeb-src http://ppa.launchpad.net/corruptedark/ppa/ubuntu focal main" > /etc/apt/sources.list.d/corruptedark.list'
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E2BA18922C0D6991
sudo apt update
```
After adding the repository, install the package with: 

`sudo apt install python3-tictactoe`

### Red Hat Package
On Red Hat and Fedora based distros you can install the .rpm package once it is released.

## Packaging
To build a .deb package, first install the package `stdeb` either from apt or pip3. 
Next, run `make deb` from this project root directory.

To build a .rpm package, first install the package `rpmdevtools` from dnf.
Next, run `make rpm` from this project root directory.
