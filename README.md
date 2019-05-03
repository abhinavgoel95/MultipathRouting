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
