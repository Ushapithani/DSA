url = input("Enter a URL: ")

if url.startswith("http://") or url.startswith("https://"):
    if "." in url:
        print(" URL is valid")
    else:
        print(" URL is invalid ")
else:
    print(" URL is invalid")