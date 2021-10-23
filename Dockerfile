# 引入公共的java1.8镜像
FROM python:v2

# 名字
MAINTAINER chenqinggang

COPY test.sh /

RUN chmod +x ./test.sh.sh

# Run command to allocate the default system resources to JMeter at 'docker run' and start jmeter-server with all required parameters
ENTRYPOINT ["/test.sh"]

