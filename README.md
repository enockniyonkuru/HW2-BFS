# Breadth-First Search (BFS) Implementation

## Overview
This project implements a breadth-first search algorithm for graph traversal and shortest path finding using directed graphs loaded from adjacency list format files.

## Methods

### `Graph.__init__(filename: str)`
Initializes a Graph object by loading a directed graph from an adjacency list file.

**Parameters:**
- `filename` (str): Path to the adjacency list file to load

**Returns:** None

---

### `Graph.bfs(start, end=None)`
Performs breadth-first search traversal or pathfinding on the graph.

**Parameters:**
- `start`: The starting node for BFS traversal. Can be any hashable type.
- `end` (optional): The destination node for shortest path search. If None, performs complete BFS traversal. Defaults to None.

**Returns:**
- If `end` is None: A list of nodes in BFS traversal order starting from the start node. Returns empty list if start node doesn't exist.
- If `end` is provided and a path exists: A list of nodes representing the shortest path from start to end (inclusive of both endpoints).
- If `end` is provided and no path exists: Returns None.
- If `end` is provided but end node doesn't exist in graph: Returns None.

**Edge Cases Handled:**
- Empty graph
- Start node doesn't exist in the graph
- End node doesn't exist in the graph
- Unconnected/disconnected graph (only traverses/searches reachable nodes from start)
- Start and end are the same node
- Corrupted graph structure (raises appropriate exception)

**Time Complexity:** O(V + E) where V is vertices and E is edges

**Space Complexity:** O(V) for the queue and visited set

---

## Test Functions

### `test_bfs_traversal()`
Tests BFS traversal functionality using the tiny_network dataset. Verifies that BFS correctly visits all reachable nodes from a start node and returns them in proper order. Tests both normal traversal and edge case with non-existent start nodes.

### `test_bfs()`
Tests BFS pathfinding functionality using the citation_network dataset. Verifies that BFS correctly finds shortest paths between connected nodes, returns None for unconnected nodes, and handles edge cases like non-existent nodes and same start/end nodes.

### `test_bfs_exception_invalid_file()`
Tests that BFS properly raises an exception when the underlying graph structure is corrupted or invalid. Demonstrates error handling by attempting BFS on a corrupted graph.


