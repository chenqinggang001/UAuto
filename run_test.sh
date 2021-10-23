#!/bin/bash
len=50 ch='='
printf '%*s' "$len" | tr ' ' "$ch"; echo -e '开始检测\c';printf '%*s\n' "$len" | tr ' ' "$ch"
MY_IMAGE="chenqinggang/autotest"
MY_CONTAINER="autotest_ulearning_cn"
MY_NETWORK_IP="172.10.0.0/24"
MY_NETWORK_NAME="cqgnetwork"
MY_CONTAINER_HOST="172.10.0.3"
DOCKER_RUN="run -itd -v /mytest/reports/xml:/mytest/reports/xml -v /mytest/results/xml:/mytest/results/xml -p 12333:12333/tcp --network $MY_NETWORK_NAME --ip $MY_CONTAINER_HOST --name $MY_CONTAINER $MY_IMAGE"
cd / | ls | grep mytest
if [ $? -eq  0 ]; then
echo "mytest存在"
else
mkdir -p /mytest/results/xml
mkdir -p /mytest/reports/xml
chmod 777 /mytest
echo "创建文件夹"
fi
function docker_install_network()
{
	echo "检查DockerNetword......"
	docker -v
	if [ $? -eq  0 ]; then
	echo "检查到Docker已安装!"

	else
	echo "安装docker环境..."
	curl -sSL https://get.daocloud.io/docker | sh
	echo "安装docker环境...安装完成!"
	fi
	echo "检查网桥ing......"
	docker network ls | grep $MY_NETWORK_NAME
	if [ $? -eq  0 ]; then
	echo "检查到Docker网桥!"
	else
	echo "配置docker网桥..."
	docker network create --subnet=$MY_NETWORK_IP $MY_NETWORK_NAME
	fi
}
docker_install_network
printf '%*s' "$len" | tr ' ' "$ch"; echo -e '开始拉取镜像\c';printf '%*s\n' "$len" | tr ' ' "$ch"
function docker_container()
{
	docker ps -a | grep $MY_CONTAINER
	if [ $? -eq  0 ]; then
		docker ps | grep $MY_CONTAINER
		if [ $? -eq  0 ]; then
		docker stop $MY_CONTAINER
		docker rm $MY_CONTAINER
		docker $DOCKER_RUN
		else
		docker rm $MY_CONTAINER
		docker $DOCKER_RUN
		fi
	else
	docker $DOCKER_RUN
	fi
}
function docker_pull_run()
{
	echo "检查镜像是否存在......"
	docker images | grep $MY_IMAGE
	if [ $? -eq  0 ]; then
	docker_container
	printf '%*s' "$len" | tr ' ' "$ch"; echo -e '启动成功!\c';printf '%*s\n' "$len" | tr ' ' "$ch"
	else
	echo "拉取镜像......"
	docker pull $MY_IMAGE
	echo "拉取镜像成功！"
	echo "启动容器......"
	docker $DOCKER_RUN
	printf '%*s' "$len" | tr ' ' "$ch"; echo -e '启动成功!\c';printf '%*s\n' "$len" | tr ' ' "$ch"
	fi
}
docker_pull_run
docker exec -i $MY_CONTAINER /bin/bash -c "cd /mytest && python3 run_test.py"