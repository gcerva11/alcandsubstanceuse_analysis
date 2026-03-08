from data.dictionary import data

def classify_year(response_label):
    under = {
        "1st year undergraduate",
        "2nd year undergraduate",
    }

    upper = {
        "3rd year undergraduate",
        "4th year undergraduate",
        "5th year or more undergraduate",
    }

    if response_label in under:
        return "Underclassmen"
    elif response_label in upper:
        return "Upperclassmen"
    else:
        return "Other"