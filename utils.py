import random as r
from patient import Patient

def binary_insert(heapOrdenado, patient):
    left, right = 0, len(heapOrdenado) - 1
    while left <= right:
        mid = (left + right) // 2
        if heapOrdenado[mid].getLifeExpectation() < patient.getLifeExpectation():
            left = mid + 1
        else:
            right = mid - 1
    heapOrdenado.insert(left, patient)

def generate_name():
    names = [
        "Sophia", "Jackson", "Olivia", "Liam", "Emma", "Noah", "Ava", "Aiden", "Isabella", "Lucas",
        "Mia", "Ethan", "Amelia", "Mason", "Harper", "Logan", "Evelyn", "Elijah", "Abigail", "Oliver",
        "Emily", "Jacob", "Elizabeth", "Benjamin", "Mila", "William", "Ella", "James", "Avery", "Alexander",
        "Sofia", "Michael", "Camila", "Elijah", "Scarlett", "Daniel", "Victoria", "Matthew", "Aria", "Henry",
        "Grace", "Sebastian", "Chloe", "Joseph", "Penelope", "Samuel", "Riley", "David", "Zoey", "Carter",
        "Nora", "Wyatt", "Lily", "Jayden", "Lillian", "John", "Addison", "Owen", "Aubrey", "Dylan", "Layla",
        "Luke", "Amelia", "Gabriella", "Grayson", "Madelyn", "Isaac", "Harper", "Christopher", "Sofia", "Joshua",
        "Aaliyah", "Andrew", "Ellie", "Julian", "Stella", "Cameron", "Natalie", "Dominic", "Zoe", "Jaxon", "Leah",
        "Joseph", "Hazel", "Levi", "Violet", "Adam", "Aurora", "Lincoln", "Savannah", "Dylan", "Audrey", "Leo",
        "Brooklyn", "Brayden", "Bella", "Anthony", "Claire", "Theodore", "Skylar"
    ]
    lastNames = [
        "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
        "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
        "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
        "Young", "Hall", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams",
        "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts", "Gomez", "Phillips", "Evans",
        "Turner", "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes", "Stewart", "Morris", "Morales", "Murphy",
        "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper", "Peterson", "Bailey", "Reed", "Kelly", "Howard",
        "Ramos", "Kim", "Cox", "Ward", "Richardson", "Watson", "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray",
        "Mendoza", "Ruiz", "Hughes", "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers","Sánchez","Rodriguez","Cano"
    ]
    return f'{r.choice(names)} {r.choice(lastNames)}'

def create_patients(heap, n):
    id = 0
    for _ in range(n):
        name = generate_name()
        id += 1
        lifeExpectation = r.randint(1, 3650)
        patient = Patient(name, id, lifeExpectation)
        heap.insertar(patient)
    return heap, id

def add_patient(heap, id):
    name = generate_name()
    id += 1
    lifeExpectation = r.randint(1, 3650)
    patient = Patient(name, id, lifeExpectation)
    heap.insertar(patient)
    return id, patient

def print_patients(heap):
    print("******************************************")
    print("LISTA DE ESPERA:\n\n")
    for patient in heap.heapOrdenado[:min(10, len(heap.heapOrdenado))]:
        print("----------------------------\n")
        print(f'{patient}\n')
    print("******************************************")
