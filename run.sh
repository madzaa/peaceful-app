echo  "Building the docker container"
# shellcheck disable=SC2046
eval $(minikube docker-env)
docker build . -t peacefulapp

echo "Adding minikube ingress addon"
minikube addons enable ingress

echo "Adding the bitnami repo"
helm repo add bitnami https://charts.bitnami.com/bitnami
echo "Installing postgresql "
helm install postgresql-ha  \
      --set postgresql.replicaCount=2 \
      --set postgresql.password=password \
      --set global.postgresql.username=postgres \
      --set global.postgresql.password=postgres \
      --set global.postgresql.database=blacklisted \
      --set global.postgresql.repmgrUsername=repgres \
      --set global.postgresql.repmgrPassword=repword \
      --set global.postgresql.repmgrDatabase=blacklisted \
            bitnami/postgresql-ha

helm install peacefulapp helm
minikube service peacefulapp-helm --url
