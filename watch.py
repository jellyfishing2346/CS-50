import re

# Main function
def main():
    print(parse(input("HTML: ")))

# Parse function
def parse(s):
    if re.search(r"<iframe(.)*><\/iframe.", s):
        url = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)", s)
        if url:
            pattern = url.groups()
            return "http://youtu.be/" + pattern[3]

if __name__ = "__main__":
    main()