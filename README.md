# MultipathRouting

## Multipath Routing with Ryu Controller and MiniNet and OpenFlow1.3

Four Cases:
1. Shortest Path Routing.
2. Load Balanced - Multipath.
3. Rate Monitor Multipath Routing with Priority.
4. Static Queues.

To use:

```
sudo python topology.py
```
```
ryu-manager <filename>.py --observe-links
```

### Shortest Path Routing: *ShortestPath.py*

Uses DFS to find all the paths from the source to the destination.
The shortest path is the path with the least number of hops.

#### *_packet_in_handler(self, ev):*

It is invoked when a packet enters a switch. If the packet is an ARP packet, it is used to install flows in the switches.

#### *install_paths(self, src, first_port, dst, last_port, ip_src, ip_dst):*

This function is called to find and install the paths between a source-destination pair.

#### *link_delete_handler(self, ev):*

Handles deleted or down links to reroute traffic to a different path, if available.


### Load Balanced - Multipath: *LoadBalancer.py*

Uses DFS to find all the paths from the source to the destination.
Indentifies the top `MAX_PATHS` (number) paths based on number of hops.
Group tables are used to perform different actions on packets originating from the same flow.

#### *get_paths(self, src, dst):*

Uses DFS to find all the paths in the network from the source to the destination.


### Rate Monitor Multipath Routing with Priority: *RateMonitorPriority.py*

#### *monitor(self):*

Function that is running on a separate thread.
Every 5 seconds, it requests stats from all the switches to compute the bandwidth utilization of each link.

#### *show_stat(self, type):*

Match the data packets in each switch. Find the difference in number of bytes between consequent statistics measurements. This is used to compute the bandwidth utilization of each link.


#### *get_optimal_paths(self, src, dst, ip_src, ip_dst):*

Takes into account the priority, and the bandwidth utilization to find the best paths for different data flows.


### Static Queues: *QOS_static.py*

A network with a single path. Manually defined queues for priority traffic for performing comparisons.
