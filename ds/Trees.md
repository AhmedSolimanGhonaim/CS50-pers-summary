# Binary Trees

A **binary tree** is a hierarchical data structure similar to a family tree, where each node points to its children, starting from a root node. In a binary tree, each node (except leaf nodes) has up to two pointers referencing its left and right children. This structure enables efficient operations, often with a time complexity of O(log n), though it may use more memory due to the extra pointers.

## Properties

- **Left child**: Always less than the parent node.
- **Right child**: Always greater than the parent node.
- The structure is recursive, similar to the Fibonacci sequence.

When searching or inserting, we pass a pointer to the root and a search value. The tree is recursively divided, making the search space smaller at each step.

- **Worst-case insertion**: O(n), which can occur if the tree becomes unbalanced (like a linked list).
- **Optimized (balanced) trees**: Use rotations to maintain O(log n) operations.

## Common Operations

### 1. Traversal

Traversal means visiting all nodes in the tree. There are two main categories:

#### Depth-First Search (DFS)
DFS explores as far as possible along each branch before backtracking. It is usually implemented recursively. Main types:

- **Preorder (current-left-right)**: Visit node, then left subtree, then right subtree.
- **Inorder (left-current-right)**: Visit left subtree, then node, then right subtree.
- **Postorder (left-right-current)**: Visit left subtree, then right subtree, then node.

#### Breadth-First Search (BFS)
BFS visits all nodes at the current depth before moving to the next level. It is typically implemented using a queue and is also known as **Level Order Traversal**.

---

For more details, see [Binary Tree in Python - GeeksforGeeks](https://www.geeksforgeeks.org/python/binary-tree-in-python/)

## gemini interactive explainer
[text](https://g.co/gemini/share/7049db50ad80)