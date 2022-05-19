from src.trees.node import Node, T
from src.trees.tree_operations import TreeOperations
import types
from typing import TypeVar
import unittest


class TreeOperationTest(unittest.TestCase):
    def setUp(self) -> None:
        # left heavy tree
        l_left2 = Node("left2", None, None)
        l_left = Node("left", l_left2, None)
        l_right = Node("right", None, None)
        self.left_heavy_tree = Node("root", l_left, l_right)

        # right heavy tree
        r_right2 = Node("right2", None, None)
        r_right = Node("right", r_right2, None)
        r_left = Node("left", None, None)
        self.right_heavy_tree = Node("root", r_left, r_right)

        # single node tree
        self.root_tree = Node("root", None, None)

        # An instance of TreeOperations
        self.tree_op_class_instance = TreeOperations()


    def test_bfs_left_heavy(self) -> None:
        self.assertListEqual(
            TreeOperations.bfs(self.left_heavy_tree),
            ['root', 'left', 'right', 'left2']
        )


    def test_bfs_right_heavy(self) -> None:
        self.assertListEqual(
            TreeOperations.bfs(self.right_heavy_tree),
            ['root', 'left', 'right', 'right2']
        )


    def test_bfs_root(self) -> None:
        self.assertListEqual(
            TreeOperations.bfs(self.root_tree),
            ['root']
        )


    def test_bfs_none(self) -> None:
        self.assertListEqual(TreeOperations.bfs(None), [])


    def test_pre_order_left_heavy(self) -> None:
        self.assertListEqual(
            TreeOperations.pre_order(self.left_heavy_tree),
            ['root', 'left', 'left2', 'right']
        )


    def test_pre_order_right_heavy(self) -> None:
        self.assertListEqual(
            TreeOperations.pre_order(self.right_heavy_tree),
            ['root', 'left', 'right', 'right2']
        )


    def test_pre_order_root(self) -> None:
        self.assertListEqual(
            TreeOperations.pre_order(self.root_tree),
            ['root']
        )


    def test_pre_order_none(self) -> None:
        self.assertListEqual(TreeOperations.pre_order(None), [])


    def test_max_depth_left_heavy(self) -> None:
        self.assertEqual(TreeOperations.max_depth(self.left_heavy_tree), 3)


    def test_max_depth_right_heavy(self) -> None:
        self.assertEqual(TreeOperations.max_depth(self.right_heavy_tree), 3)


    def test_max_depth_root(self) -> None:
        self.assertEqual(TreeOperations.max_depth(self.root_tree), 1)


    def test_max_depth_none(self) -> None:
        self.assertEqual(TreeOperations.max_depth(None), 0)


    def test_bfs_is_static_method(self) -> None:
        self.assertIsInstance(
            self.tree_op_class_instance.bfs,
            types.FunctionType
        )


    def test_pre_order_is_static_method(self) -> None:
        self.assertIsInstance(
            self.tree_op_class_instance.pre_order,
            types.FunctionType
        )


    def test_max_depth_is_static_method(self) -> None:
        self.assertIsInstance(
            self.tree_op_class_instance.max_depth,
            types.FunctionType
        )


    def test_a_is_typedef_object(self) -> None:
        self.assertIsInstance(T, TypeVar)


    # def test_a_is_typedef_a_object(self) -> None:
    #     self.assertEqual(T, TypeVar('T'))
