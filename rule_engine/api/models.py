from django.db import models

class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.node_type = node_type  # "operator" or "operand"
        self.value = value           # Value for operand nodes (e.g., comparison values)
        self.left = left            # Reference to left child
        self.right = right          # Reference to right child

    def to_dict(self):
        """Convert the Node instance to a dictionary for JSON serialization."""
        node_dict = {
            "type": self.node_type,
            "value": self.value,
            "left": self.left.to_dict() if self.left else None,
            "right": self.right.to_dict() if self.right else None,
        }
        return node_dict