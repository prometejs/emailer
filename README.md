# Emailer
Multithreaded email process to send emails 

**Document contents**

- [Packages](#packages)
  - [Releases](#releases)
  - [Installation](#installation)
    - [Docker](#)
    - [Executables](#)
- [Usage](#usage)
  - [Docker](#)
  - [Executables](#)
    - [Set Up Environment](#set-up-environment)
- [Development](#development)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)

## Packages
Product packages come in docker images and linux/windows exectable binaries. 

#### Releases
##### package releases
  - [linux executable stable]()
  - [linux executable experimental]()
  - [windows executable stable]()
  - [windows executable experimental]()
  - [docker image stable]()
  - [docker image experimental]()

#### Installation
##### [Docker](https://docs.docker.com/engine/installation/)
<!-- docker pull from release list -->
##### Executables
<!-- download with oras & normal from release list -->

#### Usage
##### [Docker](https://docs.docker.com/engine/installation/)
##### Executables 
<!-- stable and tags -->
<!-- versioning -->
<!-- see full list of packages -->
<!-- they come in executables and images -->
<!-- ###### Set Up Environment -->
<!-- to get started the application requires these env set -->
<!-- see full list of env here -->

#### Development
For the adventurous, unstable features are available in the `main` branch, which you can install from [source](https://github.com/Prometejs/emailer.git) and do the following:

##### _Prerequisites_
  - [Python 3.1x]()

1. ##### Clone repository
```
$ git clone https://github.com/Prometejs/emailer.git {your-development-path}
```
2. ##### Create virtual environment
```
$ python -m venv {path-to-virtual-environment}
```
3. ##### Activate virtual environment
_**linux**_
```
$ source {path-to-virtual-environment}/bin/activate
```
_**windows**_
```
$ {path-to-virtual-environment}\\Scripts\\Activate
```
4. ##### Install requirements
```
pip install -r {your-development-path}/requirements.txt
```
**NB:** _In path definitions note OS shells slash conventions_

## Environment Variables
allowed environment variables `KEYWORDS`=`VALUES`:

| KEYWORDS | DEFAULT VALUE | TYPE | DESCRIPTION | REQUIRED | 
| :------ | :-----------: | :--: | :---------: | :------: |
| mail_user || string | mail server account username | true |
| mail_password || string | mail server account password| true |
| mail_host || string | mail server host | true |
| mail_sender || string | email of account that sends emails | true |
| mail_port || integer | mail server port | true |
| mail_receivers || string | JSON list of email receipients | true |
| max_thread_count | 5 | integer | maximun number of threads to start in running process | false |

## Contributing
The original authors and maintainers of this project are:
* Elvis Segbawu @eliblurr

Contributers can fork and make pull request to [emailer](https://github.com/Prometejs/emailer.git)