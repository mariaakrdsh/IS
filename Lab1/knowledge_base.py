import csv

# Questions
questions = {
    'purpose': 'What is the primary purpose of the car?',
    'fuel_efficiency': 'How important is fuel efficiency to you?',
    'size': 'What size of car are you looking for?',
    'brand_preference': 'Do you have a preferred car brand?',
    'budget': 'What is your budget range for a car?',
    'tech_features': 'Are advanced tech features important to you?',
    'color_preference': 'Do you have a preference for the car\'s color?',
    'driving_conditions': 'Will you be driving in challenging road conditions?',
}

# Car models and their conditions
car_conditions = {
    "sedan": {
        "purpose": "daily_commute",
        "fuel_efficiency": "moderate",
        "size": "compact",
        "brand_preference": "no",
        "budget_range": "affordable",
        "tech_features": "basic",
        "color_preference": "any",
        "driving_conditions": "normal"
    },
    "sports_car": {
        "purpose": "joyful_driving",
        "fuel_efficiency": "low",
        "size": "small",
        "brand_preference": "no",
        "budget_range": "affordable",
        "tech_features": "basic",
        "color_preference": "bright",
        "driving_conditions": "normal"
    },
    "SUV": {
        "purpose": "family_transport",
        "fuel_efficiency": "moderate",
        "size": "midsize",
        "brand_preference": "no",
        "budget_range": "affordable",
        "tech_features": "basic",
        "color_preference": "any",
        "driving_conditions": "normal"
    },
    "pickup_truck": {
        "purpose": "hauling",
        "fuel_efficiency": "low",
        "size": "full_size",
        "brand_preference": "no",
        "budget_range": "affordable",
        "tech_features": "basic",
        "color_preference": "any",
        "driving_conditions": "fair"
    },
    "luxury_car": {
        "purpose": "joyful_driving",
        "fuel_efficiency": "moderate",
        "size": "full_size",
        "brand_preference": "yes",
        "budget_range": "premium",
        "tech_features": "advanced",
        "color_preference": "elegant",
        "driving_conditions": "normal"
    },
    "hatchback": {
        "purpose": "daily_commute",
        "fuel_efficiency": "high",
        "size": "compact",
        "brand_preference": "no",
        "budget_range": "affordable",
        "tech_features": "basic",
        "color_preference": "any",
        "driving_conditions": "normal"
    },
    "convertible": {
        "purpose": "joyful_driving",
        "fuel_efficiency": "low",
        "size": "small",
        "brand_preference": "no",
        "budget_range": "affordable",
        "tech_features": "basic",
        "color_preference": "bright",
        "driving_conditions": "normal"
    },
    "crossover": {
        "purpose": "family_transport",
        "fuel_efficiency": "moderate",
        "size": "midsize",
        "brand_preference": "no",
        "budget_range": "affordable",
        "tech_features": "basic",
        "color_preference": "any",
        "driving_conditions": "normal"
    },
    "minivan": {
        "purpose": "family_transport",
        "fuel_efficiency": "moderate",
        "size": "full_size",
        "brand_preference": "no",
        "budget_range": "affordable",
        "tech_features": "basic",
        "color_preference": "any",
        "driving_conditions": "challenging"
    }
}

cars = {
    "sedan": {
        "description": "Sedan\nA practical and fuel-efficient choice for daily commuting. Compact in size."
    },
    "sports_car": {
        "description": "Sports Car\nDesigned for joyful driving with a focus on performance. Small and sporty."
    },
    "SUV": {
        "description": "SUV\nIdeal for family transport with moderate fuel efficiency. Midsize for versatility."
    },
    "pickup_truck": {
        "description": "Pickup Truck\nGreat for hauling and heavy-duty tasks. Low fuel efficiency, full-size."
    },
    "luxury_car": {
        "description": "Luxury Car\nA prestige choice with moderate fuel efficiency. Full-size with luxury features."
    },
    "hatchback": {
        "description": "Hatchback\nPerfect for urban driving. High fuel efficiency and compact size."
    },
    "convertible": {
        "description": "Convertible\nEnjoy the open road with this low-fuel-efficiency, small-sized convertible."
    },
    "crossover": {
        "description": "Crossover\nVersatile and practical for a variety of uses. Moderate fuel efficiency and midsize."
    },
    "minivan": {
        "description": "Minivan\nGreat for family transport. Moderate fuel efficiency and full-size."
    }
}

def purpose():
    answer = None
    while answer not in ['daily_commute', 'family_transport', 'hauling', 'joyful_driving']:
        answer = input(f"{questions['purpose']} (daily_commute/family_transport/hauling/joyful_driving) ")
    return answer


def fuel_efficiency():
    answer = None
    while answer not in ['high', 'low', 'moderate']:
        answer = input(f"{questions['fuel_efficiency']} (high/low/moderate) ")
    return answer


def size():
    answer = None
    while answer not in ['compact', 'small', 'midsize', 'full_size']:
        answer = input(f"{questions['size']} (compact/small/midsize/full_size) ")
    return answer


def brand_preference():
    answer = None
    while answer not in ['yes', 'no']:
        answer = input(f"{questions['brand_preference']} (yes/no) ")
    return answer


def budget_range():
    answer = None
    while answer not in ['affordable', 'premium']:
        answer = input(f"{questions['budget']} (affordable/premium) ")
    return answer


def tech_features():
    answer = None
    while answer not in ['basic', 'advanced']:
        answer = input(f"{questions['tech_features']} (basic/advanced) ")
    return answer


def color_preference():
    answer = None
    while answer not in ['any', 'bright', 'neutral', 'elegant']:
        answer = input(f"{questions['color_preference']} (any/bright/neutral/elegant) ")
    return answer


def driving_conditions():
    answer = None
    while answer not in ['normal', 'fair', 'challenging']:
        answer = input(f"{questions['driving_conditions']} (normal/fair/challenging) ")
    return answer


def find_car():
    selected_conditions = {
        'purpose': purpose(),
        'fuel_efficiency': fuel_efficiency(),
        'size': size(),
        'brand_preference': brand_preference(),
        'budget_range': budget_range(),
        'tech_features': tech_features(),
        'color_preference': color_preference(),
        'driving_conditions': driving_conditions()
    }

    matching_cars = []

    for car, conditions in car_conditions.items():
        if all(conditions[key] == selected_conditions[key] for key in conditions):
            matching_cars.append(car)

    if matching_cars:
        print("Based on your preferences, the following cars may suit you:")
        for car in matching_cars:
            print(cars[car]['description'])
    else:
        print("Sorry, we couldn't find a matching car based on your preferences.")


def main():
    print('What type of car suits you best?')
    find_car()


if __name__ == "__main__":
    main()