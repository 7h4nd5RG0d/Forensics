# FIle: 

# Solve: 

# Something new: 
1) Kuberntes:(multiple containerisation, K8s)  
a) Pods are smallest unit of kubernetes.  
b) Pods contain containers, shared volume and shared network address(IP).  
c) Kubernetes cluster contains of nodes, where nodes are servers either virtual or bare metal server.  
d) Inside nodes are pods.  
e) There is a master node which manages worker nodes.  
f) Master node runs only system nodes which is responsble for the functioning of the cluster( master node is the control plane).  
g) Each node has container runtime, kubelet(connects with the API server in master node), kube-proxy(resposible for netwrok communication between nodes and within the node)  
h) The master node also has scheduler(planning and distribution of load between nodes), Kube control manager(controls everything in the cluster), cloud control manager, etcd (stores all logs of cluster, stored as key-value pair), DNS servers.  
i) kubectl connects to specific cluster and allows remote control of the cluster.  
j) kubectl connects to API server using REST api.


