# CLOUDMARK

Check_mk cloudmark monitoring scripts


### Table of Contents
**[Getting Started](#getting-started)**<br>
**[Prerequisites](#prerequisites)**<br>
**[Installing package](#installing-package)**<br>
**[Installing agent plugin](#installing-agent-plugin)**<br>
**[License](#license)**<br>


## Getting Started

These instructions will get you the cloudmark plugin correctly installed on your Check_MK Server.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing package

1. Connect via SSH on your monitoring server;
1. change user to your site;
1. Download the cloudmark-v1.0.mkp; `wget|curl`
1. use cmk to install de package.


#### Example
```
# su - mysite
~ wget http://github.com/m3rlinux/check_mk/cloudmark/cloudmark-v1.0.mpk
~ cmk -P install cloudmark-v1.0.mpk
```


### Installing agent plugin

1. Connect via SSH on your Cloudmark server;
1. download the plugin; `wget|curl`
1. move the plugin into "plugins" folder of your agent;
1. add execution permission to the file.

#### Exampe

```
# wget http://github.com/m3rlinux/check_mk/cloudmark/cloudmark/plugins/cloudmark
# mv cloudmark /usr/lib/check_mk_agent/plugins/
# chmod +x /usr/lib/check_mk_agent/plugins/cloudmark
```

## License

This project is licensed under the GPLv3 License. [See more details in license file](../LICENSE)

