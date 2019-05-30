# OpenConfigAPI
OpenConfig YANG generated API in Python Flask

Credit here
http://ipengineer.net/2018/10/yang-openapi-swagger-code-generation/


How I generated this<br>
$ wget https://github.com/ict-strauss/COP/tree/master/pyang_plugins/swagger.py<br>
$ git clone https://github.com/openconfig/public<br>
$ git clone https://github.com/OpenNetworkingFoundation/EAGLE-Open-Model-Profile-and-Tools.git<br>
$ cd EAGLE-Open-Model-Profile-and-Tools<br>
$ virtualenv eagle<br>
$ source eagle/bin/activate # At this point, the prompt will change to signify the venv activation<br>
$ pip install pyang<br>
$ export PYBINDPLUGIN=`echo $PWD`<br>
$ mkdir export<br>
$ copy swagger.py -> whereever pyang/plugins are for your environment<br>
$ pyang --plugindir $PYBINDPLUGIN -f swagger -p $YANGDIR -o export/oc_interfaces.json ../public/release/modules/interfaces/openconfig-interfaces.yang<br>
$ ls -la export<br>
$ #now download the swagger codegen<br>
$ wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.4.5/swagger-codegen-cli-2.4.5.jar<br>
$ java -jar swagger-codegen-cli-2.4.5.jar generate -i export/oc_interfaces.json -l python-flask -o python-flask<br>
