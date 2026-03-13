import json
import sys
import os
import argparse

def load_codes():
    file_path = os.path.join(os.path.dirname(__file__), 'codes.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        sys.exit(1)

def load_translations(lang):
    file_path = os.path.join(os.path.dirname(__file__), 'i18n', f'{lang}.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # Default to empty if language file not found
        return {}

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

def format_result(item, translations):
    code_str = str(item['code'])
    phrase = item['phrase']
    description = item['description']
    
    # Override with translation if available
    if code_str in translations:
        phrase = translations[code_str].get('phrase', phrase)
        description = translations[code_str].get('description', description)

    output = (
        f"\033[1;32mHTTP {item['code']}\033[0m: \033[1;36m{phrase}\033[0m\n"
        f"Class: {item['class']}\n"
        f"Description: {description}\n"
    )
    if 'mdn_link' in item:
        output += f"MDN: \033[4;34m{item['mdn_link']}\033[0m\n"
    output += f"{'-' * 40}"
    return output

def main():
    parser = argparse.ArgumentParser(description="Search for HTTP status codes.")
    parser.add_argument('query', help="The HTTP code, keyword, or class (e.g., 404, timeout, 4xx)")
    parser.add_argument('--lang', default='en', help="The language for descriptions (e.g., en, fa)")
    
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    codes = load_codes()
    translations = load_translations(args.lang)
    
    if args.query.lower() == 'all':
        results = codes
    else:
        results = search_code(args.query, codes)

    if not results:
        print(f"No results found for '{args.query}'.")
    else:
        print(f"Found {len(results)} results in '{args.lang}':\n")
        for res in results:
            print(format_result(res, translations))

if __name__ == "__main__":
    main()
