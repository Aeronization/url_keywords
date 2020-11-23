import time

def match_keyword_in_url(url: str, keywords: list) -> list:
    """
    (R. Friel - November 18, 2020)
    Adhere to single responsiblity principal
    Perform a list comprehension on the keywords and check if a keyword is in the url.
    """

    # (R. Friel - November 18, 2020) - This is a list comprehension.
    # Basically the for loop, conditional, and output are all in one line.
    # Similar to this:
    #
    # keyword_matches = []
    # for keyword in keywords:
    #   if keyword in url:
    #       keyword_matches.append(keyword)

    keyword_matches: list = [ keyword for keyword in keywords if keyword in url ]

    return keyword_matches


# keywords = ["www", "rockerbox", "data", "badword", "word", "tornado", "django"]
# url = "www.rockerbox.com?data=tornado"

start_time = time.time()
print(match_keyword_in_url(url=url,keywords=keywords))
print(f"--- {(time.time() - start_time)} seconds ---")