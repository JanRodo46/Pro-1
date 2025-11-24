def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"


def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    for benefit in list_benefits():
        print(build_sentence(benefit))


name_the_benefits_of_functions()
