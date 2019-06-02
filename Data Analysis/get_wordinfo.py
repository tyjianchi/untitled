from docx import Document
from docx.document import Document as _Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import _Cell,_Row, Table
from docx.text.paragraph import Paragraph

def iter_block_items(parent):

    if isinstance(parent, _Document):
        parent_elm = parent.element.body
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    elif isinstance(parent, _Row):
        parent_elm = parent._tr
    else:
        raise ValueError("something's not right")
    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)

def get_word_info():
    word_info=Document(r"C:\Elven_Code\frs_example\frs_example.docx")
    for block_info in iter_block_items(word_info):
        if isinstance(block_info, Paragraph):
            print(block_info.text)
        elif isinstance(block_info, Table):
            for row in block_info.rows:
                row_data = []
                for cell in row.cells:
                    for paragraph in cell.paragraphs:
                        row_data.append(paragraph.text)
                print("\t".join(row_data))

get_word_info()