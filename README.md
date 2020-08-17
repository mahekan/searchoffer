# searchoffer

searchoffer is a Python library for suggestqueries google api.

## Installation

Use the package manager [pip](https://pypi.org/project/searchoffer/) to install searchoffer.

```bash
pip install searchoffer
```

## Usage

```python
import SearchOffer

keyword = "ماهکان"
language = "fa"
SearchOffer(keyword,language).offer() # Default offer
SearchOffer(keyword,language).google() # Offer from Google
```
