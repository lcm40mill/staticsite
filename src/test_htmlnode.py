import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_partial_eq(self):
        node = HTMLNode("a", "stuff")
        node2 = HTMLNode("a", "stuff")
        self.assertEqual(node, node2)

    def test_full_eq(self):   
        node = HTMLNode("h", "Heading", "", {"href": "https://google.com", "target": "_blank"})
        node2 = HTMLNode("h", "Heading", "", {"href": "https://google.com", "target": "_blank"})
        self.assertEqual(node, node2)

    def test_partial_props_eq(self):    
        node = HTMLNode("p", "beepboop")
        node2 = HTMLNode("p", "beepboop")
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_full_props_eq(self):
        node = HTMLNode("h", "Heading", "", {"href": "https://google.com", "target": "_blank"})
        node2 = HTMLNode("h", "Heading", "", {"href": "https://google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    if __name__ == "__main__":
        unittest.main()