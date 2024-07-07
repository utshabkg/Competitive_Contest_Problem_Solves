class Codec:
    def __init__(self):
        self.urls = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        short = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        while short in self.urls:
            short = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        self.urls[short] = longUrl
        return short

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urls.get(shortUrl, '')

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
