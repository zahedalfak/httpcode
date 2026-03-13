import json
import sys
import os
import argparse
import csv

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
        return {}

def get_supported_langs():
    i18n_dir = os.path.join(os.path.dirname(__file__), 'i18n')
    langs = []
    if os.path.exists(i18n_dir):
        for f in os.listdir(i18n_dir):
            if f.endswith('.json'):
                langs.append(f.replace('.json', ''))
    return sorted(langs)

def search_code(query, codes):
    results = []
    query_str = str(query).lower()
    is_class_filter = query_str.endswith('xx') and len(query_str) == 3 and query_str[0].isdigit()
    
    for item in codes:
        if is_class_filter:
            if item['class'].startswith(query_str):
                results.append(item)
            continue
        if query_str.isdigit() and str(item['code']) == query_str:
            results.append(item)
            continue
        if query_str in item['phrase'].lower() or query_str in item['description'].lower():
            results.append(item)
    return results

def format_result(item, translations):
    code_str = str(item['code'])
    phrase = item['phrase']
    description = item['description']
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

def export_results(results, format, output_file, translations):
    if format == 'json':
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
    elif format == 'csv':
        keys = ['code', 'phrase', 'class', 'description', 'mdn_link']
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            for res in results:
                # Use translations for export if available
                row = res.copy()
                code_str = str(row['code'])
                if code_str in translations:
                    row['phrase'] = translations[code_str].get('phrase', row['phrase'])
                    row['description'] = translations[code_str].get('description', row['description'])
                writer.writerow({k: row.get(k, '') for k in keys})
    elif format == 'md':
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# HTTP Status Codes Export\n\n")
            f.write("| Code | Phrase | Class | Description |\n")
            f.write("|------|--------|-------|-------------|\n")
            for res in results:
                phrase = res['phrase']
                desc = res['description']
                code_str = str(res['code'])
                if code_str in translations:
                    phrase = translations[code_str].get('phrase', phrase)
                    desc = translations[code_str].get('description', desc)
                f.write(f"| {res['code']} | {phrase} | {res['class']} | {desc} |\n")
    print(f"Successfully exported {len(results)} results to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Search for HTTP status codes.")
    parser.add_argument('query', nargs='?', help="The HTTP code, keyword, or class (e.g., 404, timeout, 4xx)")
    parser.add_argument('--lang', default='en', help="The language for descriptions (e.g., en, fa)")
    parser.add_argument('--list-langs', action='store_true', help="List all supported languages")
    parser.add_argument('--export', choices=['json', 'csv', 'md'], help="Export format")
    parser.add_argument('--out', help="Output file name")
    
    args = parser.parse_args()

    if args.list_langs:
        langs = get_supported_langs()
        print("Supported languages:")
        for l in langs:
            print(f"  - {l}")
        sys.exit(0)

    if not args.query:
        parser.print_help()
        sys.exit(1)

    codes = load_codes()
    translations = load_translations(args.lang)
    
    if args.query.lower() == 'all':
        results = codes
    else:
        results = search_code(args.query, codes)

    if not results:
        print(f"No results found for '{args.query}'.")
    else:
        if args.export:
            out_file = args.out or f"export_{args.query}.{args.export}"
            export_results(results, args.export, out_file, translations)
        else:
            print(f"Found {len(results)} results in '{args.lang}':\n")
            for res in results:
                print(format_result(res, translations))

if __name__ == "__main__":
    main()
