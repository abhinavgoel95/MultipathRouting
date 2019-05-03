# MultipathRouting

## Multipath Routing with Ryu Controller and MiniNet and OpenFlow1.3

Four Cases:
1. Shortest Path Routing.
2. Load Balanced - Multipath.
3. Rate Monitor Multipath Routing.
4. Rate Monitor Multipath Routing with Priority.

To use:

```
sudo python topology.py
ryu-manager <filename>.py --observe-links
```

### Shortest Path Routing: ShortestPath.py

Uses DFS to find all the paths from the source to the destination.
The shortest path is the path with the least number of hops.

#### _packet_in_handler(self, ev):

It is invoked when a packet enters a switch. If the packet is an ARP packet, it is used to install flows in the switches.

#### install_paths(self, src, first_port, dst, last_port, ip_src, ip_dst):

This function is called to find and install the paths between a source-destination pair.

#### link_delete_handler(self, ev):

Handles deleted or down links to reroute traffic to a different path, if available.


### Load Balanced - Multipath: LoadBalancer.py

Uses DFS to find all the paths from the source to the destination.
Indentifies `MAX_PATHS`
