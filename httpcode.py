import json
import sys
import os

def load_codes():
    file_path = os.path.join(os.path.dirname(__file__), 'codes.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        sys.exit(1)

def search_code(query, codes):
    results = []
    query_str = str(query).lower()
    
    # Check if query is a class filter (e.g., 2xx, 4xx)
    is_class_filter = query_str.endswith('xx') and len(query_str) == 3 and query_str[0].isdigit()
    
    for item in codes:
        # Filter by class (e.g., 2xx)
        if is_class_filter:
            if item['class'].startswith(query_str):
                results.append(item)
            continue

        # Search by code (exact match)
        if query_str.isdigit() and str(item['code']) == query_str:
            results.append(item)
            continue
            
        # Search by phrase or description (partial match)
        if query_str in item['phrase'].lower() or query_str in item['description'].lower():
            results.append(item)
            
    return results

def format_result(item):
    output = (
        f"\033[1;32mHTTP {item['code']}\033[0m: \033[1;36m{item['phrase']}\033[0m\n"
        f"Class: {item['class']}\n"
        f"Description: {item['description']}\n"
    )
    if 'mdn_link' in item:
        output += f"MDN: \033[4;34m{item['mdn_link']}\033[0m\n"
    output += f"{'-' * 40}"
    return output

def main():
    if len(sys.argv) < 2:
        print("Usage: python httpcode.py [code | keyword | class | all]")
        print("Examples:")
        print("  python httpcode.py 404       # Search by code")
        print("  python httpcode.py timeout   # Search by keyword")
        print("  python httpcode.py 4xx       # Filter by class")
        print("  python httpcode.py all       # List all codes")
        sys.exit(1)

    query = sys.argv[1]
    codes = load_codes()
    
    if query.lower() == 'all':
        results = codes
    else:
        results = search_code(query, codes)

    if not results:
        print(f"No results found for '{query}'.")
    else:
        print(f"Found {len(results)} results:\n")
        for res in results:
            print(format_result(res))

if __name__ == "__main__":
    main()
