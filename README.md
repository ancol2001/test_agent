# test_agent

LANCS_HOME="/var/lancsnet"
service lancs-agent stop 2> /dev/null
$LANCS_HOME/bin/lancs-control stop 2> /dev/null
rm -rf $LANCS_HOME
find /etc/systemd/system -name "lancs*" | xargs rm -f
systemctl daemon-reloads
userdel lancs 2> /dev/null
groupdel lancs 2> /dev/null

LANCS_HOME="/var/lancsnet"
service lancs-manager stop 2> /dev/null
$LANCS_HOME/bin/lancs-control stop 2> /dev/null
rm -rf $LANCS_HOME
[ -f /etc/rc.local ] && sed -i'' '/lancs-control start/d' /etc/rc.local
find /etc/{init.d,rc*.d} -name "*lancs*" | xargs rm -f
userdel lancs 2> /dev/null
groupdel lancs 2> /dev/null
