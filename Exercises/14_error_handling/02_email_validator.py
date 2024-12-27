class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


VALID_DOMAINS = [".com", ".bg", ".org", ".net"]

while True:
    emails = input("Enter an email (or 'End' to stop): ")

    if emails == "End":
        break

    try:
        # Check if the email contains '@'
        if "@" not in emails:
            raise MustContainAtSymbolError("Email must contain @")

        # Extract the name and domain
        name, domain = emails.split("@")

        # Check if the name is long enough
        if len(name) < 5:
            raise NameTooShortError("Name must be more than 4 characters")

        # Check if the domain is valid
        if not any(domain.endswith(valid_domain) for valid_domain in VALID_DOMAINS):
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

        # If all checks pass
        print("Email is valid")

    except (NameTooShortError, MustContainAtSymbolError, InvalidDomainError) as e:
        print(e)
