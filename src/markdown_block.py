from htmlnode import HTMLNode, ParentNode
from codework import *
from textnode import *
from block_types import *

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        if block == "":
            continue
        new_blocks.append(block.strip())
    return new_blocks

def markdown_to_html_node(markdown):
    blocks_list = markdown_to_blocks(markdown)
    capture_nodes = []
    for b in blocks_list:
        b_type = block_to_block_type(b)
        parent = create_html_parent_node(b, b_type)
        capture_nodes.append(parent)
    return ParentNode(tag="div", children=capture_nodes)

def create_html_parent_node(block, block_type):
    match block_type:
        case "heading":
            header_number = count_headers(block)
            prefix = header_number * "#" + " "
            header_value = block.split(prefix)[1]
            return ParentNode(tag=f'h{header_number}', children=text_to_children(header_value))
        case "code":
            code_child = code_block_processing(block)
            code_block = [ParentNode(tag="code", children=code_child)]
            return ParentNode(tag="pre", children=code_block)
        case "quote":
            quote_child = quote_block_processing(block)
            return ParentNode(tag="blockquote", children=quote_child)
        case "unordered_list":
            un_list = unordered_block_processing(block)
            return ParentNode(tag="ul", children=un_list)
        case "ordered_list":
            ordered_child = quote_block_processing(block)
            return ParentNode(tag="ol", children=ordered_child)
        case "paragraph":
            paragraph_child = paragraph_block_processing(block)
            return ParentNode(tag="p", children=paragraph_child)
        case _:
            raise ValueError("Invalid Block Type")


def count_headers(header_markdown):
    heading_prefix = header_markdown.split(" ")[0]
    header_count = 0
    for char in heading_prefix:
        if char == "#":
            header_count += 1
    if header_count > 6:
        header_count = 6
    return header_count

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_children = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        if isinstance(html_node, HTMLNode):
            html_children.append(html_node)
        else:
            raise Exception(f"{html_node} is not an HTMLNode Object.")
    return html_children        

def code_block_processing(block):
    code_content = block.split("```")[1]
    code_children = text_to_children(code_content)
    return code_children

def quote_block_processing(block):
    quote_lines = block.split("\n")
    quote_children = []

    for line in quote_lines:
        if line != "":
            content = line[2:]
            quote_children += text_to_children(content)
    return quote_children

def unordered_block_processing(block):
    list_lines = block.split("\n")
    list_children = []
    for line in list_lines:
        if line != "":
            content = line[2:]
            list_parent = ParentNode(tag="li", children=text_to_children(content))
            list_children.append(list_parent)
    return list_children

def ordered_block_processing(block):
    list_lines = block.split("\n")
    list_children = []
    for line in list_lines:
        if line != "":
            content = line[3:]
            list_parent = ParentNode(tag="li", children=text_to_children(content))
            list_children.append(list_parent)
    return list_children

def paragraph_block_processing(block):
    lines = block.split("\n")
    para_child = []
    for line in lines:
        if line != "":
            para_child += text_to_children(line)
            para_child += LeafNode(tag="br", value="")
    return para_child