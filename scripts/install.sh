#!/bin/bash

# TODO: a lot of things...
#       1) it should be parametric
#       2) it should handle server/agent scenarios
#       3) it should handle install/uninstall
#       4) it should print appropriate warnings (eg. need to install both on Cmk server and ag
#       5) it should detect or ask for paths and user/group instead of hardcoding them
#       5) It should have the option to create both server and agent RPMs

echo "AS/400 SNMP checks installation script"

cp -v ./checks/* /usr/share/check_mk/checks/
cp -v ./docs/* /usr/share/doc/check_mk/checks/
cp -v ./templates/*.php /usr/share/nagios/html/pnp4nagios/templates/
cp -v ./perfometer/perfometer_*.py /usr/share/check_mk/web/plugins/perfometer
cp -v ./wato/*.py /usr/share/check_mk/web/plugins/wato/

chown apache:nagios -R \
  /usr/share/check_mk/checks/ \
  /usr/share/doc/check_mk/checks/

chown apache:nagios -R \
  /usr/share/nagios/html/pnp4nagios/templates/

chown apache:nagios -R \
  /usr/share/check_mk/web/plugins/perfometer/

chmod ug+x \
  /usr/share/check_mk/checks/snmp_as400*

exit 0
