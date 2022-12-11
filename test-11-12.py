monkeys = [
    {
        "items": [61],
        "operation": lambda old: old * 11,
        "test": lambda x: 7 if x % 5 == 0 else 4,
    },
    {
        "items": [76, 92, 53, 93, 79, 86, 81],
        "operation": lambda old: old + 4,
        "test": lambda x: 2 if x % 2 == 0 else 6
    },
    {
        "items": [91, 99],
        "operation": lambda old: old * 19,
        "test": lambda x: 5 if x % 13 == 0 else 0
    },
    {
        "items": [58, 67, 66],
        "operation": lambda old: old * old,
        "test": lambda x: 6 if x % 7 == 0 else 1
    },
    {
        "items": [94, 54, 62, 73],
        "operation": lambda old: old + 1,
        "test": lambda x: 3 if x % 19 == 0 else 7
    },
    {
        "items": [59, 95, 51, 58, 58],
        "operation": lambda old: old + 3,
        "test": lambda x: 0 if x % 11 == 0 else 4
    },
    {
        "items": [87, 69, 92, 56, 91, 93, 88, 73],
        "operation": lambda old: old + 8,
        "test": lambda x: 5 if x % 3 == 0 else 2
    },
    {
        "items": [71, 57, 86, 67, 96, 95],
        "operation": lambda old: old + 7,
        "test": lambda x: 3 if x % 17 == 0 else 1
    }
]

number_inspections = [0 for _ in range(len(monkeys))]

for j in range(10000):
    print(f"Round {j}")
    print([monkey["items"] for monkey in monkeys])
    for i in range(len(monkeys)):
        monkey = monkeys[i]
        number_inspections[i] += len(monkey["items"])
        while len(monkey["items"]) > 0:
            worry = monkey["items"].pop(0)
            new_worry = monkey["operation"](
                worry) % (5 * 2 * 13 * 7 * 19 * 11 * 3 * 17)
            new_monkey = monkey["test"](new_worry)
            monkeys[new_monkey]["items"].append(new_worry)

number_inspections.sort(reverse=True)
business = number_inspections[0]*number_inspections[1]

print(business)
