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
    
    for item in codes:
        # Search by code (exact match)
        if query_str.isdigit() and str(item['code']) == query_str:
            results.append(item)
            continue
            
        # Search by phrase or description (partial match)
        if query_str in item['phrase'].lower() or query_str in item['description'].lower():
            results.append(item)
            
    return results

def format_result(item):
    return (
        f"\033[1;32mHTTP {item['code']}\033[0m: \033[1;36m{item['phrase']}\033[0m\n"
        f"Class: {item['class']}\n"
        f"Description: {item['description']}\n"
        f"{'-' * 40}"
    )

def main():
    if len(sys.argv) < 2:
        print("Usage: python httpcode.py [code or keyword]")
        print("Example: python httpcode.py 404")
        print("Example: python httpcode.py timeout")
        sys.exit(1)

    query = sys.argv[1]
    codes = load_codes()
    results = search_code(query, codes)

    if not results:
        print(f"No results found for '{query}'.")
    else:
        for res in results:
            print(format_result(res))

if __name__ == "__main__":
    main()
