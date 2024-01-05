import json

candidates = [
    {
        "id": 1,
        "name": "John Dorian",
        "email": "jd@yahoo.com",
        "company": ""
    },
    {
        "id": 2,
        "name": "Chris Turk",
        "email": "chris.turk@gmail.com",
        "company": "iotech"
    },
    {
        "id": 3,
        "name": "Elliot Reed",
        "email": "elliot.reed@gmail.com",
        "company": "microsoft"
    },
    {
        "id": 4,
        "name": "Perry Cox",
        "email": "perry.cox+1@heart.com",
        "company": "microsoft"
    }
]
developers = [
    {
        "name": "John Dorian",
        "email": "john.dorian@yahoo.com",
        "company": "google"
    },
    {
        "name": "Chris Turk",
        "email": "chris.turk@gmail.com",
        "company": "netflix"
    },
    {
        "name": "Elliot Reed",
        "email": "elliot.reed@gmail.com",
        "company": ""
    },
    {
        "name": "Perry Cox",
        "email": "perry.cox@heart.com",
        "company": "microsoft"
    }
]


def add_matching_id_to_developer(candidates: list, developers: list) -> dict:
    """
    # Match Rule 1 - Exact match of the email addresses
    """
    # Key candidates by email
    candidates_by_email = {}
    for candidate in candidates:
        candidates_by_email[candidate["email"]] = candidate

    # Key developer by email
    developers_by_email = {}
    for developer in developers:
        developers_by_email[developer["email"]] = developer

    # Add candidate id to developer
    for developer in developers:
        # Validation
        if not developer["email"]:
            continue

        # Set candidate id to developer
        if developer["email"] in candidates_by_email:
            developer["id"] = candidates_by_email[developer["email"]]["id"]
            continue

    """"
    Match Rule 2 - Exact match of the name and company
    """
    # Key candidate by name_company
    candidates_by_name_company = {}
    for candidate in candidates:
        candidates_by_name_company[candidate["name"] + "_" + candidate["company"]] = candidate

    # Key developer by name_company
    developers_by_name_company = {}
    for developer in developers:
        developers_by_name_company[developer["name"] + "_" + developer["company"]] = developer

    for developer in developers:
        # Validation
        if not developer["name"] or not developer["company"]:
            continue

        # Set candidate id to developer
        if developer["name"] + "_" + developer["company"] in candidates_by_name_company:
            developer["id"] = candidates_by_name_company[developer["name"] + "_" + developer["company"]]["id"]

    return developers_by_email


if __name__ == "__main__":
    matched_people = add_matching_id_to_developer(candidates, developers)
    json_matched_people = json.dumps(matched_people, indent=4)
    print(json_matched_people)
