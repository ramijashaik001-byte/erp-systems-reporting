import os

def count_lines(directory):
    total_lines = 0
    file_counts = {}
    
    for root, dirs, files in os.walk(directory):
        # Exclude common non-source dirs
        if any(ignored in root for ignored in ['.git', '__pycache__', 'venv', '.pytest_cache']):
            continue
            
        for file in files:
            if file.endswith('.py'):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        lines = len(f.readlines())
                        file_counts[path] = lines
                        total_lines += lines
                except Exception as e:
                    print(f"Error reading {path}: {e}")
                    
    return total_lines, file_counts

if __name__ == '__main__':
    target_dir = os.path.join(os.path.dirname(__file__), 'erp')
    if not os.path.exists(target_dir):
        print(f"Directory {target_dir} does not exist yet. Please run generate_erp_system.py first.")
    else:
        total, details = count_lines(target_dir)
        print("\n--- Line Count Summary ---")
        sorted_files = sorted(details.items(), key=lambda x: x[1], reverse=True)
        for path, count in sorted_files[:20]:
            rel_path = os.path.relpath(path, os.path.dirname(__file__))
            print(f"{rel_path}: {count} lines")
        if len(sorted_files) > 20:
            print(f"... and {len(sorted_files) - 20} more files")
        print("--------------------------")
        print(f"Total Python files: {len(details)}")
        print(f"Total Lines of Code: {total}")
        print("--------------------------")
