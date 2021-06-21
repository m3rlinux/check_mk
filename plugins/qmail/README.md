# Qmail

Check_mk Qmail monitoring scripts


### Table of Contents
**[Getting Started](#getting-started)**<br>
**[Prerequisites](#prerequisites)**<br>
**[Installing package](#installing-package)**<br>
**[Installing agent plugin](#installing-agent-plugin)**<br>
**[License](#license)**<br>


## Getting Started

These instructions will get you the qmail plugin correctly installed on your Check_MK Server and Qmail Server.

### Prerequisites

#### On Host to be monitored
- [x] python2.7

### Installing package

1. Connect via SSH on your monitoring server;
1. change user to your site;
1. Download the qmail-1.0.mkp; `wget|curl`
1. use cmk to install de package.


#### Example
```
# su - mysite
~ wget https://github.com/m3rlinux/check_mk/raw/1.6/plugins/qmail/qmail-1.0.mkp
~ cmk -P install qmail-1.0.mpk
```


### Installing agent plugin

1. Connect via SSH on your Qmail server;
1. download the plugin; `wget|curl`
1. move the plugin into "plugins" folder of your agent;
1. add execution permission to the file.

#### Example

```
# wget https://github.com/m3rlinux/check_mk/raw/1.6/plugins/qmail/agent/mk_qmail
# mv mk_qmail /usr/lib/check_mk_agent/plugins/
# chmod +x /usr/lib/check_mk_agent/plugins/cloudmark
```

## License

This project is licensed under the GPLv3 License. [See more details in license file](../../../LICENSE)

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
