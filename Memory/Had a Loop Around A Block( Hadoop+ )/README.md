# File:
https://archive.org/download/Case2-HDFS
# Solve:
https://www.petermstewart.net/magnet-weekly-ctf-week-5-had-a-loop-around-the-block/ 
https://www.petermstewart.net/magnet-weekly-ctf-week-6-the-elephant-in-the-room/  
# Resources: 
1) HADOOP FORENSICS --> https://www.youtube.com/watch?v=Mc0uiKmYIpk
2) LINUX FORENSICS --> https://www.youtube.com/watch?v=bXCmroKa9U0  
# Something new:
1) **Hadoop Cluster** : handling big data.  
       Designed for distributed storage and processing of large datasets arcoss a cluster of computers using simple programming languages.  
       Data is divided into blocks and stored across various nodes in a cluster.  
       If a node fails, data is replicated across multiple nodes ensuring no loss.  
       Namenode is the main node of the cluster along with HA(High Availability) architecture.  
   **Components :**  
   a) **HDFS( Hadoop Distributed File System) :**  
   Stores large data files across a distributed file system.  
   Data is divided into blocks and replicated for fault tolerance.  
   b) **YARN( Yet Another Rule Negotiator) :**  
   Manages cluster resources for distributed applications.  
   Schedules and monitors tasks.  
   c) **Mapreduce :**  
   A programming model for processing large data.  
   **Map:** Break data into chunks for parallel processing.  
   **Reduce:** Combine processed chuks for getting meaningful chunnks.
  
   **Ecosystem :**  
   a) **Hive:** SQL like query language.  
   b) **Pig:** High level platform for creating mapreduce programs.  
   c) **HBase:** A distributed database for real time processing.  
   d) **Spark:** For fast in-memory processing.  
   e) **Oozie:** Workflow Scheduler.  
   f) **Zookeeper:** Coordination service.  
   g) **Hadoop Common:** Common utilities.   

   
   
   
       
