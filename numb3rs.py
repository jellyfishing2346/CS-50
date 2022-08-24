import re

# Main function
def main():
    print(validate(input("IPv4 Address: ")))

# Validate function
def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        ipInfo = ip.split(".")
        for index in ipInfo:
            if int(index) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()