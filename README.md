# HTTP Status Codes (Standard & Unofficial)

A comprehensive reference for HTTP status codes, including standard IETF codes and unofficial codes used by major platforms like Cloudflare, Nginx, AWS, and Laravel.

## 🚀 Features

- **Standard Codes**: All 63 codes defined in RFCs (100 to 511).
- **Unofficial Codes**: 20+ codes from Cloudflare, Nginx, AWS, Microsoft IIS, Twitter, Shopify, and Laravel.
- **CLI Tool**: A simple Python script to search and filter codes quickly.
- **Reference Links**: Direct MDN links for all standard codes.
- **Developer-Friendly**: Data stored in a clean `codes.json` format.
- **i18n Support**: Descriptions available in 34+ languages (EN, FA, AR, ZH, ES, FR, DE, JA, RU, PT, TR, HI, IT, KO, VI, NL, PL, ID, TH, EL, SV, RO, HE, UK, BN, FI, HU, CS, DA, NO, MS, TL, SW, CA).
- **Guides**: Multi-language guides available in `i18n/guides/`.
- **Exporting**: Export search results to JSON, CSV, or Markdown via CLI.
- **Web UI**: Modern, beautiful web interface to explore codes in your browser.

## 🛠 Usage

### Web Interface

Simply open `web/index.html` in your browser to explore the codes with a modern UI.

### Using the CLI Tool

You can search by code, keyword, filter by class, or export results.

```bash
# List supported languages
python httpcode.py --list-langs

# Search by specific code in a specific language
python httpcode.py 404 --lang fa

# Export all 4xx errors to a Markdown file
python httpcode.py 4xx --export md --out errors.md

# Export all codes to a CSV file in Turkish
python httpcode.py all --export csv --lang tr --out codes_tr.csv
```

### Using the JSON Data

The data is available in `codes.json` for easy integration into your own projects:

```json
{
  "code": 418,
  "phrase": "I'm a teapot",
  "description": "April Fools' joke (RFC 2324), Hyper Text Coffee Pot Control Protocol.",
  "class": "4xx Client Error",
  "mdn_link": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/418"
}
```

## 📋 Included Unofficial Codes

- **Cloudflare**: 520, 521, 522, 524, 525, 526, 527, 530
- **Nginx**: 444, 494, 495, 496, 497, 499
- **AWS ELB**: 460, 463, 561
- **Laravel**: 419
- **Microsoft IIS**: 440, 449, 450
- **Shopify**: 430
- **Twitter**: 420

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
