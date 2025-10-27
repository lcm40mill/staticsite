class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    
    def to_html(self):
        #Child classes will override this method
        raise NotImplementedError
    
    def props_to_html(self):
        prop_str = ""
        if self.props is None:
            return prop_str
        for prop in self.props:
            prop_str += f' {prop}="{self.props[prop]}"'
        return prop_str
    
    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"