# Scholar Search Documentations

## Summary

This is a Google Scholar search code that can help you search for any papers you want from WebScraping powered by Google SERP API. You shall need to obtain an API key from https://www.webscrapingapi.com/pricing/serp-api and the free trial offers 100 requests per month.   

`Reminder : please replace your own API key in the search code in the folder first and then start to run the following codes`

## Parameters 

| Parameters         | Data Type | Usage                                                        |
| ------------------ | --------- | ------------------------------------------------------------ |
| query              | string    | words user want to search for                                |
| display_language   | string    | default display language set up as `en`(English) and more language can be found at : https://developers.google.com/custom-search/docs/xml_results_appendices#interfaceLanguages |
| num_results        | int       | maximum number of results return                             |
| display_citations  | int       | `0`  not display citations<br />`1` display citations        |
| display_at_year    | int       | set `0` to not use<br />return this year data                |
| display_until_year | int       | set `0` to not use<br />return the year entered to the year untill now data |

## Functions 

##### `link go straight to each function use case`

| Functions                                                    | Explain                                    |
| ------------------------------------------------------------ | ------------------------------------------ |
| [general_search](#general_search)                            | general search without any constrains      |
| [citations_search](#citations_search)                        | include with citations                     |
| [search_at_year](#search_at_year)                            | search only at year                        |
| [search_until_year](#search_until_year)                      | search only until year                     |
| [search_for_both_citations_and_at_year](#search_for_both_citations_and_at_year) | include both with citations and at year    |
| [search_for_both_citations_and_until_year](#search_for_both_citations_and_until_year) | include both with citations and until year |

#### general_search

##### [ return back to `Functions` tables](#Functions)

```python
import google_scholar_research as gr
# just in case user needs to reload module
# import importlib
# importlib.reload(gr)
result = gr.get_general_scholar_search(query = "Web3", display_language = "en", num_results = 1, 
                                      display_citations = 0, display_at_year = 0, display_until_year = 0)
print(result)
```

```bash
# exmaple output :
{'search_parameters': {'google_url': 'https://scholar.google.com/scholar?q=Web3&num=1&as_vis=0&hl=en&sourceid=chrome&ie=UTF-8',
  'engine': 'google_scholar',
  'google_domain': 'scholar.google.com',
  'device': 'desktop',
  'query': 'Web3',
  'num': '1',
  'as_vis': '0',
  'hl': 'en'},
 'search_information': {'organic_results_state': 'Results for exact spelling',
  'total_results': 23100,
  'time_taken_displayed': 0.03,
  'query_displayed': 'Web3'},
 'organic_results': [{'title': 'Decentralized ai: Edge intelligence and smart blockchain, metaverse, web3, and desci',
   'link': 'https://ieeexplore.ieee.org/abstract/document/9839452/',
   'result_id': 'H0ocG4yaluMJ',
   'snippet': 'Centralization has dominated classic scientific, social, and economic developments. Decentralization has also received increasing attention in management, decision, governance, and …',
   'publication_info': {'summary': 'L Cao\xa0- IEEE Intelligent Systems, 2022 - ieeexplore.ieee.org',
    'authors': [{'name': 'L Cao',
      'link': 'https://scholar.google.com/citations?user=cDs3DM8AAAAJ&hl=en&num=1&oi=sra',
      'author_id': 'cDs3DM8AAAAJ'}]},
   'inline_links': {'cited_by': {'total': 77,
     'link': 'https://scholar.google.com/scholar?cites=16399465019657177631&as_sdt=5,33&sciodt=0,33&hl=en&num=1',
     'cites_id': '16399465019657177631'},
    'related_pages_link': '/scholar?q=related:H0ocG4yaluMJ:scholar.google.com/&scioq=Web3&hl=en&num=1&as_sdt=0,33',
    'versions': {'total': 3,
     'link': 'https://scholar.google.com/scholar?cluster=16399465019657177631&hl=en&num=1&as_sdt=0,33',
     'cluster_id': '16399465019657177631'}},
   'position': 1}],
 'pagination': {'other_pages': {'2': 'https://scholar.google.com/scholar?start=1&q=Web3&hl=en&num=1&as_sdt=0,33',
   '3': 'https://scholar.google.com/scholar?start=2&q=Web3&hl=en&num=1&as_sdt=0,33',
   '4': 'https://scholar.google.com/scholar?start=3&q=Web3&hl=en&num=1&as_sdt=0,33',
   '5': 'https://scholar.google.com/scholar?start=4&q=Web3&hl=en&num=1&as_sdt=0,33',
   '6': 'https://scholar.google.com/scholar?start=5&q=Web3&hl=en&num=1&as_sdt=0,33',
   '7': 'https://scholar.google.com/scholar?start=6&q=Web3&hl=en&num=1&as_sdt=0,33',
   '8': 'https://scholar.google.com/scholar?start=7&q=Web3&hl=en&num=1&as_sdt=0,33',
   '9': 'https://scholar.google.com/scholar?start=8&q=Web3&hl=en&num=1&as_sdt=0,33',
   '10': 'https://scholar.google.com/scholar?start=9&q=Web3&hl=en&num=1&as_sdt=0,33'},
  'current': 1,
  'next': 'https://scholar.google.com/scholar?start=1&q=Web3&hl=en&num=1&as_sdt=0,33'},
 'searchdata_pagination': {'current': 1,
  'next': 'https://serpapi.webscrapingapi.com/v1?q=Web3&hl=en&start=1&num=1',
  'other_pages': {'2': 'https://serpapi.webscrapingapi.com/v1?q=Web3&hl=en&start=1&num=1',
   '3': 'https://serpapi.webscrapingapi.com/v1?q=Web3&hl=en&start=2&num=1',
   '4': 'https://serpapi.webscrapingapi.com/v1?q=Web3&hl=en&start=3&num=1',
   '5': 'https://serpapi.webscrapingapi.com/v1?q=Web3&hl=en&start=4&num=1',
   '6': 'https://serpapi.webscrapingapi.com/v1?q=Web3&hl=en&start=5&num=1',
   '7': 'https://serpapi.webscrapingapi.com/v1?q=Web3&hl=en&start=6&num=1',
   '8': 'https://serpapi.webscrapingapi.com/v1?q=Web3&hl=en&start=7&num=1',
   '9': 'https://serpapi.webscrapingapi.com/v1?q=Web3&hl=en&start=8&num=1',
   '10': 'https://serpapi.webscrapingapi.com/v1?q=Web3&hl=en&start=9&num=1'}}}

```

#### citations_search

##### [ return back to `Functions` tables](#Functions)

```python
import google_scholar_research as gr
# just in case user needs to reload module
# import importlib
# importlib.reload(gr)
result = gr.get_general_scholar_search(query = "Web3", display_language = "en", num_results = 1, 
                                      display_citations = 1, display_at_year = 0, display_until_year = 0)
print(result)
```

#### search_at_year

##### [ return back to `Functions` tables](#Functions)

```python
import google_scholar_research as gr
# just in case user needs to reload module
# import importlib
# importlib.reload(gr)
result = gr.get_general_scholar_search(query = "Web3", display_language = "en", num_results = 1, 
                                      display_citations = 0, display_at_year = 2023, display_until_year = 0)
print(result)
```

#### search_until_year

##### [ return back to `Functions` tables](#Functions)

```python
import google_scholar_research as gr
# just in case user needs to reload module
# import importlib
# importlib.reload(gr)
result = gr.get_general_scholar_search(query = "Web3", display_language = "en", num_results = 1, 
                                      display_citations = 0, display_at_year = 0, display_until_year = 2021)
print(result)
```

#### search_for_both_citations_and_at_year

##### [ return back to `Functions` tables](#Functions)

```python
import google_scholar_research as gr
# just in case user needs to reload module
# import importlib
# importlib.reload(gr)
result = gr.get_general_scholar_search(query = "Web3", display_language = "en", num_results = 1, 
                                      display_citations = 1, display_at_year = 2023, display_until_year = 0)
print(result)
```

#### search_for_both_citations_and_until_year

##### [ return back to `Functions` tables](#Functions)

```python
import google_scholar_research as gr
# just in case user needs to reload module
# import importlib
# importlib.reload(gr)
result = gr.get_general_scholar_search(query = "Web3", display_language = "en", num_results = 1, 
                                      display_citations = 1, display_at_year = 0, display_until_year = 2021)
print(result)
```

