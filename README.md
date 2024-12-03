The following commands are used for starting the application in kubernetes with minikube:

minikube start
  
eval $(minikube docker-env) 

cd into the yaml folder and run:

kubectl create -f .

minikube tunnel

On first creation youll need to enter the bash terminal of the sql pod and enter: 

mysql -pmessageboard

use messageboard;

CREATE TABLE messages(identity VARCHAR(256), message TEXT(16384));
