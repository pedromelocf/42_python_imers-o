#!/usr/bin/env python3
def famous_births(women_scientists):
    test = dict(women_scientists.items())

    test1 = dict(sorted(test.items()))
    print(test1)
    # for women in test.items():
    #     print(women[1]["name"])
    #     print(women[1]["date_of_birth"])

    # for women in sorted(women_scientists):
    #     # print(women_scientists["ada"]["name"])
    #     # print(women_scientists["ada"]["date_of_birth"])
    #     print(women)

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)