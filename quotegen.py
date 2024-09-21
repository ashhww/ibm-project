import random

def load_quotes(positive):
    """loads quotes from a file into a list"""
    try:
        with open(positive, 'r') as file:
            quotes = file.readlines()

        quotes = [quote.strip() for quote in quotes]
        return quotes
    except FileNotFoundError:
        print(f"Error: The file '{positive}' does not exist.")
        return []

def get_random_quote(quotes):
 """Returns a random quote from the list of quotes."""
 if quotes:
     return random.choice(quotes)
 else:
     return "No quotes available."

def main():
    filename = 'positive.txt'  
    quotes = load_quotes(filename)  
    random_quote = get_random_quote(quotes) 
    print("Random Quote: ", random_quote)  

if __name__ == "__main__":
    main()

