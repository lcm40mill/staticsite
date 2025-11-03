from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown):
    heading_pattern = r"^#{1,6} "
    code_pattern = r"^```.*```$"
    quote_pattern = r"^>"
    unordered_pattern = r"^- "

    #heading return
    text = re.match(heading_pattern, markdown)
    if text:
        return BlockType.HEADING
    
    #code return
    text = re.match(code_pattern, markdown, re.DOTALL)
    if text:
        return BlockType.CODE
    
    #quote return
    quotes = markdown.split("\n")
    if all(re.match(quote_pattern, quote) for quote in quotes):
        return BlockType.QUOTE
    
    #unordered list return
    lines = markdown.split("\n")
    if all(re.match(unordered_pattern, line) for line in lines):
        return BlockType.UNORDERED_LIST
    
    #ordered list return
    lines = markdown.split("\n")
    ordered = True
    starting_index = 1

    for line in lines:
        if not line.startswith(f"{starting_index}. "):
            ordered = False
            break
        starting_index += 1

    if ordered == True:
        return BlockType.ORDERED_LIST
    
    #Regular Text Return
    block = BlockType.PARAGRAPH
    return block