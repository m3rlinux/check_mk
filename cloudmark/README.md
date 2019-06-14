CLOUDMARK
=====
Check_mk cloudmark monitoring scripts

Usage:

On Client:
 
        cp plugins/cloudmark /usr/lib/check_mk_agent/plugins
 
        chmod 700 /usr/lib/check_mk_agent/plugins/cloudmark

On Monitoring Server:

If using OMD: 
        cp checks/cloudmark ~/local/share/check_mk/checks/
        cp checkman/cloudmark ~/local/share/check_mk/checkman/
        cp wato/plugins/cloudmark.py ~/local/share/check_mk/web/plugins/wato/
