laptops = {
    "asus_a407m": {
        "price": 4500000,
        "ram": 4,
        "storage": "hdd",
        "cpu": "celeron",
        "use_case": ["office", "study"]
    },
    "lenovo_ideapad_3": {
        "price": 7500000,
        "ram": 8,
        "storage": "ssd",
        "cpu": "i3",
        "use_case": ["office", "study", "coding"]
    },
    "acer_nitro_5": {
        "price": 14000000,
        "ram": 16,
        "storage": "ssd",
        "cpu": "i5",
        "use_case": ["gaming", "ai", "coding"]
    }
}

user_need = {
    "budget": 8000000,
    "min_ram": 8,
    "purpose": "coding"
}

rules = {
    "budget_ok": lambda l, u: l["price"] <= u["budget"],
    "ram_ok": lambda l, u: l["ram"] >= u["min_ram"],
    "purpose_ok": lambda l, u: u["purpose"] in l["use_case"]
}

def evaluate_laptops(name, laptop, user):
    score  = 0
    reasons = []
    
    if rules["budget_ok"](laptop, user):
        score += 2
        reasons.append("Sesuai dengan budget Anda.")
    if rules["ram_ok"](laptop, user):
        score += 3
        reasons.append("Memiliki RAM yang cukup.")
    if rules["purpose_ok"](laptop, user):
        score += 5
        reasons.append("Cocok untuk kebutuhan Anda.")
    
    return{
        "name": name,
        "score": score  ,
        "reasons": reasons  
    }
    
results = []

for name, laptop in laptops.items():
    result = evaluate_laptops(name, laptop, user_need)
    results.append(result)

results.sort(key=lambda x: x["score"], reverse=True)

for r in results:
    print(f"Model: {r['name']}, Skor: {r['score']}")
    for reason in r["reasons"]:
        print(f" - {reason}")
    print()