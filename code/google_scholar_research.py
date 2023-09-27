from requests import Session
import pandas as pd
import requests
SERP_API_KEY = "81dJcwYeeqC8NxorykUp36UG91iAFr1O"

# sort_by=relevance
def get_general_scholar_search(query : str, display_language : str, num_results : int, display_citations : int, display_at_year : int, display_until_year : int)->dict:
	"""
	get the general result for Google Scholar search from Serp API

	Args:
	query (str) : search queries 
	display_language (str) : determine the display language of the result
	display_citations (int) : 0 to be not display citations, vice versa
	display_at_year (int) : display at year data only
	display_until_year (int) : display until year data only
	sorting (str) : sort by relevance / date

	Return:
	dict : search result
	"""
	# https://serpapi.webscrapingapi.com/v1?api_key=<YOUR_API_KEY>&engine=google_scholar&q=python
	try:

		url = "https://serpapi.webscrapingapi.com/v1?"

		# case 1 : display all years data 
		if ((display_at_year == 0) & (display_until_year == 0)):
			parameters = {"api_key" : SERP_API_KEY, "engine" : "google_scholar", "q" : query, "hl" : display_language, "num" : num_results, "as_vis" : display_citations}
		
		# case 2 : display until year data only
		elif ((display_at_year == 0) & (display_until_year)):
			parameters = {"api_key" : SERP_API_KEY, "engine" : "google_scholar", "q" : query, "hl" : display_language, "num" : num_results, "as_vis" : display_citations, "as_yhi" : display_until_year}
		
		# case 3 : display at year data only
		elif ((display_at_year) & (display_until_year == 0 )):
			parameters = {"api_key" : SERP_API_KEY, "engine" : "google_scholar", "q" : query, "hl" : display_language, "num" : num_results, "as_vis" : display_citations, "as_ylo" : display_at_year}

		session = Session()

		response = session.get(url, params = parameters)
		result = response.json()

		return result
	
	except Exception as e:
		raise e	


def view_df_data(search_result : dict)->pd.DataFrame:
	"""
	organize data into DataFrame

	Args:
	search_result (dict) : search result from previous function
	
	Return:
	DataFrame : result of organized data
	"""
	try:
		# initialize dataframe
		result_df = pd.DataFrame()

		total_results = search_result["search_information"]["total_results"]
		print("total search results : ", str(total_results))

		search_results = search_result["organic_results"]
		#print(search_result)

		# loop results 
		for result in search_results:

			# check if "type" key exists 
			check_key = "type" in result.keys()

			if (check_key == True):
				temp_df = pd.DataFrame([[result["type"], result["title"], result["snippet"], result["link"]]], columns=["result_type", "title", "snippet", "research_link"])
			else:
				temp_df = pd.DataFrame([["papers", result["title"], result["snippet"], result["link"]]], columns=["result_type", "title", "snippet", "research_link"])
			
			result_df = pd.concat([result_df, temp_df], ignore_index=True)

			# display whole messages
			pd.set_option('display.max_colwidth', None) 


		return result_df

	except Exception as e:
		raise e


# if __name__ == '__main__':

# 	main()

# test1 = get_general_scholar_search(query = "Web3", display_language = "en", num_results = 10, display_citations = 0, display_at_year = 2023, display_until_year = 0)
# print(view_df_data(test1))






