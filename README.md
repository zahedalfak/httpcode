# HTTP Status Codes (Standard & Unofficial)

A comprehensive reference for HTTP status codes, including standard IETF codes and unofficial codes used by major platforms like Cloudflare, Nginx, AWS, and Laravel.

## 🚀 Features

- **Standard Codes**: All 63 codes defined in RFCs (100 to 511).
- **Unofficial Codes**: 20+ codes from Cloudflare, Nginx, AWS, Microsoft IIS, Twitter, Shopify, and Laravel.
- **CLI Tool**: A simple Python script to search and filter codes quickly.
- **Reference Links**: Direct MDN links for all standard codes.
- **Developer-Friendly**: Data stored in a clean `codes.json` format.
- **i18n Support**: Descriptions available in multiple languages (EN, FA, AR, ZH, ES, FR).

## 🛠 Usage

### Using the CLI Tool

You can search by code, keyword, or filter by class (1xx, 2xx, etc.).

```bash
# Search by specific code
python httpcode.py 404

# Search by keyword
python httpcode.py timeout

# Filter by class
python httpcode.py 5xx

# List all codes
python httpcode.py all
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
