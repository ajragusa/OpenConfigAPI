# OpenConfigAPI
OpenConfig YANG generated API in Python Flask

Credit here
http://ipengineer.net/2018/10/yang-openapi-swagger-code-generation/


How I generated this
$ wget https://github.com/ict-strauss/COP/tree/master/pyang_plugins/swagger.py
$ git clone https://github.com/openconfig/public
$ git clone https://github.com/OpenNetworkingFoundation/EAGLE-Open-Model-Profile-and-Tools.git
$ cd EAGLE-Open-Model-Profile-and-Tools
$ virtualenv eagle
$ source eagle/bin/activate # At this point, the prompt will change to signify the venv activation
$ pip install pyang
$ export PYBINDPLUGIN=`echo $PWD`
$ mkdir export
$ copy swagger.py -> whereever pyang/plugins are for your environment
$ pyang --plugindir $PYBINDPLUGIN -f swagger -p $YANGDIR -o export/oc_interfaces.json ../public/release/modules/interfaces/openconfig-interfaces.yang
$ ls -la export
$ #now download the swagger codegen
$ wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.4.5/swagger-codegen-cli-2.4.5.jar
$ java -jar swagger-codegen-cli-2.4.5.jar generate -i export/oc_interfaces.json -l python-flask -o python-flask
