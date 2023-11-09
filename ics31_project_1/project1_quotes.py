FILENAME = "movie_quotes.txt"

def get_quotes():
    """
    Returns a list of tuples (pairs) of movie quotes, where
    the first entry in the pair is a quote from a movie and
    the second entry is the response to that quote in that
    movie.
    
    The question and answer pairs in each line are 
    separated by a tab "\t". Only lines with 2 sections of text 
    separated by a tab are considered valid. All other lines can 
    be ignored.
    """
    
    quotes = []
    
    file = open(FILENAME, "r")
    
    for line in file:
        parts = line.split("\t")
        
        if len(parts) == 2:
            parts[1] = parts[1].strip()
            quotes.append((parts[0], parts[1]))
        else:
            print("Warning: found problem line in movie quotes file:\n" + line)
        
    file.close()
    
    return quotes

def get_practice_quotes():
    """
    Returns a small set of (made up) quotes in the same format
    as get_quotes.
    """
    
    return [("quote1", "quote2"),
            ("first", "second"),
            ("first they said this", "then this"),
            ("what?", "that's what"),
            ("what?", "now you've it!")]