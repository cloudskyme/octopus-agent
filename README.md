Short Description
=================
````
Octopus agent is a application that is used to collect containers, hosts, such as CPU, MEM, disk, net, diskio, and external API.
````

Full Description
================

##��������ģʽ
ֱ�ӳ����������ϣ�����ʽ

````
tar zxvf octopus-agent.tar.gz
mkdir /opt/modules
mv octopus-agent /opt/modules/
````
###scheduler.json
����scheduler.json�ļ�

###octopus.conf
�޸�����/opt/modules/octopus-agent/conf/octopus.conf�ļ�

###��������
��Ҫpython2.7.5�汾����Ҫ��װpython�����Flask��Flask-APScheduler��ipaddr����װ����pip install Flask
��������
python /opt/modules/octopus-agent/run.py
��������

##docker ����ģʽ

### ��װoctopus-agent����
````
docker load -i octopus-agent-image-0.01.tar.gz
````

### ��������
��Ҫ��װdocker����֧��1.7���ϰ汾������1.10.3�����ϰ汾
��������
docker run --name octopus-agent -v /:/rootfs:rw -v /usr/bin/docker-current:/usr/bin/docker:rw -v /var/run/docker.sock:/var/run/docker.sock:rw -p 80:80 -d octopus-agent:0.01
��������

###octopus�����޸�
---------
#### 1.����������ʽ�޸�

|������������                 | Ĭ��ֵ                                 | ˵��                            |
| --------------------------- | -------------------------------------  | ------------------------------  |
|OCTOPUS_AGENT_ACCESS_KEY     | o2ldsd9323udae20dsad32w3k3             | api���Ӽ���key                  |
|OCTOPUS_AGENT_ACCESS_ID      | octopus_agent_api_id                   | api���Ӽ���id                   |
|OCTOPUS_AGENT_ACCESS_IPS     | 127.0.0.1                              | �������IP��Ĭ��ֻ�ܱ�������    |
|OCTOPUS_AGENT_SCHEDULER_FILE |                                        | Ĭ�ϲ������ƻ�����              |
|OCTOPUS_AGENT_LOG_FILE       | logging.conf                           | ϵͳ��־�����ļ�                |

#### ��������ʹ��
docker run --name octopus-agent -v /home/zhengqs/octopus/octopus-agent/conf/test11.json:/opt/modules/octopus-agent/conf/scheduler.json:ro -v /:/rootfs:rw -v /usr/bin/docker-current:/usr/bin/docker:rw -v /var/run/docker.sock:/var/run/docker.sock:rw -p 33601:80 -e "OCTOPUS_AGENT_ACCESS_IPS=10.1.101.66;192.168.137.1" -e "OCTOPUS_AGENT_ACCESS_KEY=abcdefghijklmn" -d octopus-agent:0.01

#### 2.���ڷ�ʽ
�ڱ��ش���octopus.conf�����ļ���ͨ��-v /etc/octopus-agent/octopus.conf:/opt/modules/octopus-agent/conf/octopus.conf:ro ��ʽ���ص������С�

#### 3.����cp��ʽ
���ȴ���������Ȼ���ڱ��ش���octopus.conf�����ļ�����ͨ��docker cp octopus.conf octopus-agent:/opt/modules/octopus-agent/conf/octopus.conf�����������У������������docker restart octopus-agent.

### ���üƻ�����

ͨ��docker cp��ʽ���ƻ����������ļ�����������
````
����ͨ��docker cp scheduler.json octopus-agent:/opt/modules/octopus-agent/conf/scheduler.json
````
ͨ��docker run -v ��ʽ�����ļ�
��������
docker run --name octopus-agent -v /etc/scheduler.json:/opt/modules/octopus-agent/conf/scheduler.json:ro -v /:/rootfs:rw -v /usr/bin/docker-current:/usr/bin/docker:rw -v /var/run/docker.sock:/var/run/docker.sock:rw -p 80:80 -d octopus-agent:0.01
��������

