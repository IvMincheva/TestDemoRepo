from errors import NameTooShortError, MustContainAtSymbolError, InvalidDomainError, InvalidDomainNameError

valid_domains = {"com", "bg", "org", "net"}

while True:
    line = input()
    if line == "End":
        break

    email_parts = line.split("@")
    if len(email_parts) == 1:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain_name = email_parts

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain_name_parts = domain_name.split(".")
    if len(domain_name_parts) < 2 or not all([len(x) > 1 for x in domain_name_parts[0:len(domain_name_parts) - 1]]):
        raise InvalidDomainNameError("Invalid domain name")

    domain = domain_name_parts[-1]
    if domain not in valid_domains:
        raise InvalidDomainError(
            f"{domain} is not valid domain. Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
