import networkx as nx

class Graph:
    """
    A directed graph container that supports breadth-first search (BFS) traversal and pathfinding.
    
    This class wraps a NetworkX directed graph loaded from an adjacency list file format.
    It provides BFS functionality for graph traversal and finding shortest paths between nodes.
    
    Attributes:
        graph (nx.DiGraph): A NetworkX directed graph object containing the loaded network.
    
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        Performs breadth-first search (BFS) traversal or pathfinding on the graph.
        
        This method implements BFS to either traverse the graph from a start node or find
        the shortest path between two nodes. It handles various edge cases including empty
        graphs, disconnected components, and missing nodes.
        
        Args:
            start: The starting node for BFS traversal
            end (optional): The destination node for shortest path search. If None, performs
                          complete BFS traversal from start node. Defaults to None.
        
        Returns:
            - If end is None: A list of nodes in BFS traversal order starting from the start node.
                            Returns empty list if start node doesn't exist in graph.
            - If end is provided and a path exists: A list of nodes representing the shortest path
                                                    from start to end (inclusive of both endpoints).
            - If end is provided and no path exists: Returns None.
            - If end is provided but end node doesn't exist in graph: Returns None.
        
        Edge Cases Handled:
            - Empty graph: Returns empty list (BFS) or None (pathfinding)
            - Start node doesn't exist: Returns empty list (BFS) or None (pathfinding)
            - End node doesn't exist: Returns None
            - Unconnected graph: Only traverses/searches reachable nodes from start
            - Start and end are the same: Returns [start]
            - Single node graph: Returns appropriate result
        
        Time Complexity: O(V + E) where V is vertices and E is edges
        Space Complexity: O(V) for the queue and visited set
        """
        # Edge case: start node doesn't exist in the graph
        if start not in self.graph:
            return [] if end is None else None
        
        # Edge case: empty graph
        if len(self.graph) == 0:
            return [] if end is None else None
        
        # Edge case: end node provided but doesn't exist in graph
        if end is not None and end not in self.graph:
            return None
        
        # Edge case: start and end are the same node
        if end is not None and start == end:
            return [start]
        
        from collections import deque
        
        queue = deque([start])
        visited = {start}
        traversal_order = [start]
        parent = {start: None}  # Track parent for path reconstruction
        
        while queue:
            node = queue.popleft()
            
            # If searching for end node and found it, reconstruct path
            if end is not None and node == end:
                path = []
                current = end
                while current is not None:
                    path.append(current)
                    current = parent[current]
                return path[::-1]  # Reverse to get start -> end order
            
            # Explore neighbors
            for neighbor in self.graph.neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    traversal_order.append(neighbor)
                    parent[neighbor] = node
        
        # If end node was specified, we didn't find a path
        if end is not None:
            return None
        
        # Return BFS traversal order
        return traversal_order




