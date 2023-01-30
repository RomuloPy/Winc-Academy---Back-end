__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"


class Homeowners:

    def __init__(self, name, profession):
        self.name = name
        self.profession = profession


alfred_name = "Alfred Alfredson"
alfred_address = "Alfredslane 123"
alfred_needs = ["painter", "plumber"]
bert_name = "Bert Bertson"
bert_address = "Bertslane 231"
bert_needs = ["plumber"]
candice_name = "Candice Candicedottir"
candice_address = "Candicelane 312"
candice_needs = ["electrician", "painter"]


class Specialists:

    def __init__(self, name, profession):
        self.name = name
        self.address = profession


    class Electrician:

        def __init__(self, name):
            self.name = name

    class Painter:

        def __init__(self, name):
            self.name = name

    class Plumber:

        def __init__(self, name):
            self.name = name

alice_name = "Alice Aliceville"
alice_profession = "electrician"
bob_name = "Bob Bobsville"
bob_profession = "painter"
craig_name = "Craig Craigsville"
craig_profession = "plumber"




alfred_contracts = []
for need in alfred_needs:
    if need == alice_profession:
        alfred_contracts.append(alice_name)
    elif need == bob_profession:
        alfred_contracts.append(bob_name)
    elif need == craig_profession:
        alfred_contracts.append(craig_name)

bert_contracts = []
for need in bert_needs:
    if need == alice_profession:
        bert_contracts.append(alice_name)
    elif need == bob_profession:
        bert_contracts.append(bob_name)
    elif need == craig_profession:
        bert_contracts.append(craig_name)

candice_contracts = []
for need in candice_needs:
    if need == alice_profession:
        candice_contracts.append(alice_name)
    elif need == bob_profession:
        candice_contracts.append(bob_name)
    elif need == craig_profession:
        candice_contracts.append(craig_name)

print("Alfred's contracts:", alfred_contracts)
print("Bert's contracts:", bert_contracts)
print("Candice's contracts:", candice_contracts)
