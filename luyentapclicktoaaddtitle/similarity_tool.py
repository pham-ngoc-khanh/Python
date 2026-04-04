import os
import ast
import difflib
import string
from pathlib import Path

class SimilarityTool:
    def __init__(self):
        # Stop words for document similarity (Vietnamese/English)
        self.stop_words = set(['và', 'là', 'của', 'trong', 'có', 'cho', 'với', 'the', 'a', 'an', 'is', 'are', 'of', 'in', 'to', 'for', 'with'])

    def preprocess_text(self, text):
        """Preprocess text for document similarity."""
        # Convert to lowercase
        text = text.lower()
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        # Split into words
        words = text.split()
        # Remove stop words
        words = [w for w in words if w not in self.stop_words]
        return set(words)

    def get_doc_similarity(self, content1, content2):
        """Calculate document similarity using Jaccard Similarity."""
        set1 = self.preprocess_text(content1)
        set2 = self.preprocess_text(content2)
        
        if not set1 or not set2:
            return 0.0
            
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        return (intersection / union) * 100

    def get_code_similarity(self, code1, code2):
        """Calculate code similarity (%) using SequenceMatcher (textual)."""
        matcher = difflib.SequenceMatcher(None, code1, code2)
        return matcher.ratio() * 100

    def get_ast_structure(self, code):
        """Extract a structural representation of the code using AST."""
        try:
            tree = ast.parse(code)
            structure = []
            for node in ast.walk(tree):
                # We collect the node type name to focus on structure
                structure.append(type(node).__name__)
            return " ".join(structure)
        except SyntaxError:
            # If code is invalid, fallback to empty structure
            return ""

    def get_logic_similarity(self, code1, code2):
        """Evaluate logical similarity by comparing AST structures."""
        struct1 = self.get_ast_structure(code1)
        struct2 = self.get_ast_structure(code2)
        
        if not struct1 or not struct2:
            return 0.0
            
        matcher = difflib.SequenceMatcher(None, struct1, struct2)
        return matcher.ratio() * 100

    def compare_files(self, file_path1, file_path2):
        """Compare two files and return similarity results."""
        with open(file_path1, 'r', encoding='utf-8', errors='ignore') as f1, \
             open(file_path2, 'r', encoding='utf-8', errors='ignore') as f2:
            content1 = f1.read()
            content2 = f2.read()
            
        is_python = file_path1.endswith('.py') and file_path2.endswith('.py')
        
        results = {}
        if is_python:
            results['code_sim'] = self.get_code_similarity(content1, content2)
            results['logic_sim'] = self.get_logic_similarity(content1, content2)
        
        # For all files (including essays/reports)
        results['doc_sim'] = self.get_doc_similarity(content1, content2)
        
        return results

    def compare_folders(self, folder1, folder2):
        """Compare all files in folder1 with all files in folder2."""
        folder1_path = Path(folder1)
        folder2_path = Path(folder2)
        
        if not folder1_path.is_dir() or not folder2_path.is_dir():
            print(f"Lỗi: Một trong hai đường dẫn không phải thư mục.")
            return

        files1 = list(folder1_path.glob('**/*'))
        files2 = list(folder2_path.glob('**/*'))
        
        # Filter only files
        files1 = [f for f in files1 if f.is_file()]
        files2 = [f for f in files2 if f.is_file()]
        
        print(f"--- Comparing {folder1} and {folder2} ---")
        print(f"Number of files in folder 1: {len(files1)}")
        print(f"Number of files in folder 2: {len(files2)}")
        print("-" * 50)
        
        all_results = []
        
        for f1 in files1:
            for f2 in files2:
                # Basic check: only compare files of same extension or relevant ones
                if f1.suffix == f2.suffix:
                    res = self.compare_files(str(f1), str(f2))
                    all_results.append({
                        'file1': f1.name,
                        'file2': f2.name,
                        'results': res
                    })
                    
        return all_results

def main():
    tool = SimilarityTool()
    
    # In practice, you would pass folder paths here
    # For demo, let's create two dummy folders
    folder_a = "product_a"
    folder_b = "product_b"
    
    os.makedirs(folder_a, exist_ok=True)
    os.makedirs(folder_b, exist_ok=True)
    
    # Create dummy files for demonstration
    with open(f"{folder_a}/script.py", "w", encoding='utf-8') as f:
        f.write("def hello():\n    print('Hello world')\n    a = 1 + 2\n    return a")
    with open(f"{folder_b}/script.py", "w", encoding='utf-8') as f:
        f.write("def greet():\n    # greeting function\n    print('Hello world')\n    x = 10 + 20\n    return x")
        
    with open(f"{folder_a}/report.txt", "w", encoding='utf-8') as f:
        f.write("Bao cao bai tap lon ve tri tue nhan tao. Nhom 1 thuc hien.")
    with open(f"{folder_b}/report.txt", "w", encoding='utf-8') as f:
        f.write("Bao cao bai tap lon ve Tri tue Nhan tao. Nhom 2 hoan thanh.")

    results = tool.compare_folders(folder_a, folder_b)
    
    if results:
        for r in results:
            print(f"Comparing [{r['file1']}] vs [{r['file2']}]:")
            if 'code_sim' in r['results']:
                print(f"  - Source code similarity: {r['results']['code_sim']:.2f}%")
                print(f"  - Logic similarity (**): {r['results']['logic_sim']:.2f}%")
            print(f"  - Document similarity (doc): {r['results']['doc_sim']:.2f}%")
            print("-" * 30)

if __name__ == "__main__":
    main()
