# QOS in Software Defined Networks

## How to use Static Flows?
*http://csie.nqu.edu.tw/smallko/sdn/ingress_policing_queue.htm*

A simple application, but provides good understanding of how to use static flows.
You can clearly see the usefulness of adding Queues to guarantee QOS.

## QOS in a simple single path networks using Ryu:
*https://osrg.github.io/ryu-book/en/html/rest_qos.html*

Here, they introduce the REST API.
From my understanding, you have to first set up a connection between the SDN controller and the computer running the mininet network simulator. Then use `curl` and `POST` commands to build and interact with the queues. This is similar to using `ofctl` commands on the computer running mininet.

I also tried writing a QOS handler function, that responds to QOS_requests that the controller can make. To make it work, it loops back to using `ofctl` to build the queues. But with using `ofctl` the queues are set in stone, it is not possible to reconfigure or delete the queues.
