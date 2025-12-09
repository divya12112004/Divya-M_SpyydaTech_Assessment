import random
import string

class URLShortener:
    def __init__(self):
        # Mappings between URL and code
        self.code_to_url = {}
        self.url_to_code = {}

        # Allowed characters for short code
        self.chars = string.ascii_letters + string.digits

    def generate_code(self):
        """Generate a random 6-character short code"""
        code = ''.join(random.choice(self.chars) for _ in range(6))
        return code

    def shorten(self, url):
        """Return a short unique code for a given URL"""

        # If URL was already shortened before, return same code
        if url in self.url_to_code:
            return self.url_to_code[url]

        code = self.generate_code()

        # Check for collision, generate new if needed
        while code in self.code_to_url:
            code = self.generate_code()

        # Store mapping
        self.code_to_url[code] = url
        self.url_to_code[url] = code

        return code

    def redirect(self, code):
        """Return original URL for given short code"""
        if code in self.code_to_url:
            return self.code_to_url[code]
        return None


def main():
    shortener = URLShortener()

    # Example usage
    url1 = "https://www.google.com"
    url2 = "https://www.github.com"

    code1 = shortener.shorten(url1)
    code2 = shortener.shorten(url2)

    print("Original URL:", url1)
    print("Short Code :", code1)
    print()

    print("Original URL:", url2)
    print("Short Code :", code2)
    print()

    print("Redirect", code1, "->", shortener.redirect(code1))
    print("Redirect", code2, "->", shortener.redirect(code2))
    print("Redirect ABC123 ->", shortener.redirect("ABC123"))  # Non-existing


if __name__ == "__main__":
    main()
