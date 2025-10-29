import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://google.com"})
        self.assertEqual(node.to_html(),'<a href="https://google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p", 
            [LeafNode("i","Italic Text"),
             LeafNode(None, "Text"),
             LeafNode("b", "Bold Text"),
            ],
            )
        self.assertEqual(
            node.to_html(),
            "<p><i>Italic Text</i>Text<b>Bold Text</b></p>"
        )

    if __name__ == "__main__":
        unittest.main()