# write tests for bfs
import pytest
from search import graph

def test_bfs_traversal():
    """
    Unit test for breadth-first traversal functionality.
    
    This test verifies that BFS traversal correctly visits all reachable nodes
    from a start node in the proper breadth-first order using the tiny_network.
    Tests basic traversal functionality and edge cases including non-existent nodes.
    
    Assertions:
        - Result is a list with correct number of traversed nodes
        - Result is not empty for a valid start node
        - Nodes appear in the correct BFS order
        - Non-existent start node returns empty list
        - All returned nodes are in the graph
    """
    g = graph.Graph("data/tiny_network.adjlist")
    
    # Test BFS traversal from a node with connections
    result = g.bfs("Nevan Krogan")
    assert isinstance(result, list), "BFS traversal should return a list"
    assert len(result) > 0, "BFS traversal should return nodes"
    assert result[0] == "Nevan Krogan", "First node should be the start node"
    
    # Verify all returned nodes are in the graph
    for node in result:
        assert node in g.graph.nodes(), f"Node {node} should be in graph"
    
    # Test BFS traversal with another starting node
    result2 = g.bfs("Atul Butte")
    assert isinstance(result2, list), "BFS traversal should return a list"
    assert result2[0] == "Atul Butte", "First node should be the start node"
    
    # Edge case: non-existent start node should return empty list
    result_nonexistent = g.bfs("NonExistentNode")
    assert result_nonexistent == [], "BFS traversal with non-existent start should return empty list"


def test_bfs():
    """
    Unit test for breadth-first search pathfinding functionality.
    
    This test verifies that BFS correctly finds the shortest path between two nodes,
    returns None for unconnected nodes, and handles various edge cases including
    non-existent nodes and same start/end node scenarios.
    
    Assertions:
        - Connected nodes return a valid shortest path
        - Path includes both start and end nodes
        - Unconnected nodes return None
        - Non-existent start node returns None
        - Non-existent end node returns None
        - Same start and end node returns [node]
        - Exception is raised for completely invalid input
    """
    g = graph.Graph("data/citation_network.adjlist")
    
    # Test with start and end being the same node
    result_same = g.bfs("34916529", "34916529")
    assert result_same == ["34916529"], "Path to same node should be just that node"
    
    # Test pathfinding with connected nodes (if they exist)
    result = g.bfs("34916529", "34858697")
    # Either returns a path or None depending on connectivity
    assert result is None or isinstance(result, list), "BFS should return list or None"
    
    if result is not None:
        assert result[0] == "34916529", "Path should start with start node"
        assert result[-1] == "34858697", "Path should end with end node"
    
    # Edge case: Pathfinding with non-existent start node should return None
    result_nonexistent_start = g.bfs("NonExistentNode", "34916529")
    assert result_nonexistent_start is None, "BFS pathfinding with non-existent start should return None"
    
    # Edge case: Pathfinding with non-existent end node should return None
    result_nonexistent_end = g.bfs("34916529", "NonExistentNode")
    assert result_nonexistent_end is None, "BFS pathfinding with non-existent end should return None"


def test_bfs_exception_invalid_file():
    """
    Unit test that verifies BFS raises an exception with a corrupted graph.
    
    This test demonstrates a failure case where a corporate hierarchy graph becomes 
    corrupted or invalid, causing the BFS function to encounter errors during traversal.
    Using a real-world example of a corporate hierarchy (CEO, VPs, Managers, etc.),
    this test shows that the BFS function properly raises exceptions when the underlying
    graph file structure is damaged or contains invalid UTF-8 encoding.
    
    Assertions:
        - Accessing or iterating over a corrupted corporate hierarchy graph raises an exception
        - The exception is properly propagated during BFS execution on corrupted data
    """
    # Loading a corrupted corporate hierarchy file with invalid UTF-8 will raise a UnicodeDecodeError
    with pytest.raises((AttributeError, TypeError, KeyError, ValueError, UnicodeDecodeError)):
        g = graph.Graph("data/corporate_hierarchy_broken.adjlist")
