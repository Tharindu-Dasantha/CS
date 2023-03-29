def main():
    print("Welcome to the email slicer!\n")
    
    email_input = input("Input your email address: ")
    
    (user_name, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    
    print("Username: ", user_name)
    print("Domain: ", domain)
    print("Extension: ", extension)
    
main()