import zipfile
import xml.etree.ElementTree as ET
import sys

def read_pptx(file_paths):
    output_lines = []
    for file_path in file_paths:
        output_lines.append(f"====== FILE: {file_path} ======")
        try:
            with zipfile.ZipFile(file_path, 'r') as z:
                slide_files = [f for f in z.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml') and '_rels' not in f]
                
                # Sort by slide number
                slide_files.sort(key=lambda x: int(x.split('slide')[-1].split('.')[0]))
                
                for slide_file in slide_files:
                    output_lines.append(f"--- {slide_file} ---")
                    xml_content = z.read(slide_file)
                    root = ET.fromstring(xml_content)
                    ns = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
                    texts = [node.text for node in root.findall('.//a:t', ns) if node.text]
                    output_lines.extend(texts)
        except Exception as e:
            output_lines.append(f"Error: {e}")
        output_lines.append("\n")
        
    with open("pptx_output.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))

if __name__ == '__main__':
    read_pptx(sys.argv[1:])
