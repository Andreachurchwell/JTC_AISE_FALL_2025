
"""
Professional Python Toolkit
Author: Andrea Churchwell
Date: 09-29-2025
Course: AISE 2026 - W1D1

Description:
A collection of Python functions that automate common calculations
and solve real-world problems I face regularly.

Instructions:
1. Replace Andrea Churchwell with your actual name
2. Complete all TODO sections
3. Add at least 5 useful functions
4. Each function must have complete docstrings
5. Include type hints for parameters and returns
6. Test your code with test_assignment.py before submitting
"""

from typing import Union, List, Tuple, Optional
import datetime
import math


def calculate_tip(
    bill_amount: float, 
    tip_percent: float = 18.0,
    split_ways: int = 1
) -> Tuple[float, float, float]:
    """
    Calculate tip amount and total bill per person.
    
    This function helps quickly calculate tips at restaurants
    and split bills among friends.
    
    Args:
        bill_amount: The pre-tip bill total
        tip_percent: Tip percentage (default: 18%)
        split_ways: Number of people splitting the bill (default: 1)
    
    Returns:
        Tuple containing:
        - tip_amount: Total tip amount
        - total_bill: Bill including tip
        - per_person: Amount each person pays
    
    Raises:
        ValueError: If bill_amount is negative or split_ways < 1
    
    Example:
        >>> tip, total, per_person = calculate_tip(50.00, 20, 2)
        >>> print(f"Tip: ${tip:.2f}, Total: ${total:.2f}, Each pays: ${per_person:.2f}")
        Tip: $10.00, Total: $60.00, Each pays: $30.00
    """
    if bill_amount < 0:
        raise ValueError("Bill amount cannot be negative")
    if split_ways < 1:
        raise ValueError("Must split between at least 1 person")
    
    tip_amount = bill_amount * (tip_percent / 100)
    total_bill = bill_amount + tip_amount
    per_person = total_bill / split_ways
    
    return round(tip_amount, 2), round(total_bill, 2), round(per_person, 2)


# TODO: Add Function 1 - Time Management
def study_time_planner(
    pages_to_read: int,
    reading_speed: float = 2.0,
    break_interval: int = 25
) -> Tuple[float, int, str]:
    """
    TODO: Calculate study time needed with Pomodoro breaks.
    
    Args:
        pages_to_read: Number of pages to read
        reading_speed: Minutes per page (default: 2.0)
        break_interval: Minutes between breaks (default: 25 for Pomodoro)
    
    Returns:
        Tuple containing:
        - total_time: Total time including breaks (minutes)
        - num_breaks: Number of breaks needed
        - time_string: Formatted time string (e.g., "2h 15m")
    
    Example:
        >>> time, breaks, formatted = study_time_planner(50, 2.0, 25)
        >>> print(f"Need {formatted} with {breaks} breaks")
    """
    # TODO: Implement this function
    # time spent on reading pages x mins per page
    time_reading = pages_to_read * reading_speed
    # num of breaks needed
    num_breaks = int(time_reading // break_interval)
    # each break is 5 mins
    break_len = 5
    # total reading time + total break time
    total_time = time_reading + num_breaks * break_len
    # converting into hours and mins
    hours = int(total_time // 60)
    minutes = int(total_time % 60)
    # makes nice format string
    time_string = f'{hours}h {minutes}m'
    # return all 3 results
    return total_time, num_breaks, time_string
 


# TODO: Add Function 2 - Financial
def monthly_savings_calculator(
    income: float,
    expenses: List[float],
    savings_goal_percent: float = 20.0
) -> dict:
    """
    TODO: Analyze monthly budget and savings potential.
    
    Args:
        income: Monthly income
        expenses: List of monthly expenses
        savings_goal_percent: Target savings percentage (default: 20%)
    
    Returns:
        Dictionary containing:
        - 'total_expenses': Sum of all expenses
        - 'actual_savings': Income minus expenses
        - 'savings_percent': Actual savings as percentage
        - 'goal_difference': Difference from savings goal
        - 'recommendation': String with advice
    
    Example:
        >>> results = monthly_savings_calculator(3000, [1200, 400, 300, 200])
        >>> print(results['recommendation'])
    """
    # TODO: Implement this function
    # adding up expenses
    total_expenses = sum(expenses)
    # whats left over
    actual_savings = income - total_expenses
    # % of income that is saved
    savings_percent = (actual_savings / income) * 100
    # compare savings% to goal%
    goal_difference = savings_percent - savings_goal_percent
# returning a dictionay so we have mult values
    return {
        'total_expenses': total_expenses,
        'actual_savings': actual_savings,
        'savings_percent': savings_percent,
        'goal_difference': goal_difference
    }



# TODO: Add Function 3 - Health/Fitness
def workout_tracker(
    exercise_type: str,
    duration_minutes: int,
    intensity: str = "moderate"
) -> dict:
    """
    TODO: Track workout and estimate calories burned.
    
    Args:
        exercise_type: Type of exercise (e.g., "running", "cycling", "swimming")
        duration_minutes: Duration of workout
        intensity: Workout intensity ("light", "moderate", "vigorous")
    
    Returns:
        Dictionary with workout statistics
    
    Hint: You can use these approximate calories/minute values:
    - Running: light=8, moderate=11, vigorous=15
    - Cycling: light=6, moderate=8, vigorous=12
    - Swimming: light=7, moderate=10, vigorous=14
    """
    # TODO: Implement this function
    # validation
    if duration_minutes <= 0:
        raise ValueError('duration_minutes must be > 0')
    # normalize strings
    exercise_type = exercise_type.lower().strip()
    intensity = intensity.lower().strip()
    # calories per min table
    calorie_map = {
        'running': {'light': 8, 'moderate': 11, 'vigorous': 15},
        'cycling': {'light': 6, 'moderate': 8, 'vigorous': 12},
        'swimming': {'light': 7, 'moderate': 10, 'vigorous': 14}
    }
    # validate choices
    if exercise_type not in calorie_map:
        raise ValueError('Has to be either running, cycling, or swimming.')
    if intensity not in calorie_map[exercise_type]:
        raise ValueError('Pick either light/moderate/vigorous.')
    
    # compute calories
    calories_per_min = float(calorie_map[exercise_type][intensity])
    estimated_calories = round(calories_per_min * duration_minutes, 1)
    return {
        'exercise_type': exercise_type,
        'duration_minutes': duration_minutes,
        'intensity': intensity,
        'calories_per_min': calories_per_min,
        'estimated_calories': estimated_calories
    }


# # TODO: Add Function 4 - Your Choice
# def your_custom_function() -> None:
#     """
#     TODO: Create a function that solves a problem you face.
    
#     Ideas:
#     - Grade calculator for your classes
#     - Unit converter (metric/imperial)
#     - Password strength checker
#     - Task priority calculator
#     - Recipe ingredient scaler
#     """
#     # TODO: Implement this function
#     pass

# FUNCTION 4
def read_louies_mind(action: str) -> str:
    """
    Translate Louie's actions into what he's really thinking.

    Args:
        action: A short description of what Louie is doing.
                Examples: "on back tail tapping", "at feet treats", "on computer"

    Returns:
        A string with Louie's 'thoughts'.
    """
    action = action.lower().strip()

    if "back" in action and "tail" in action:
        return "⚠️ Louie thinks: 'Watch out, human… I might attack!'"
    elif "feet" in action and "treat" in action:
        return "🍪 Louie thinks: 'Treats, treats, treats — hand them over!'"
    elif "computer" in action:
        return "🪟 Louie thinks: 'I don’t care about your work… open the window!'"
    else:
        return "😼 Louie is impossible to read right now… mysterious as always."

def demo_louie() -> None:
    """Show Louie's mind-reading results in a pretty format."""
    print("4. READ LOUIE'S MIND")
    print("-" * 30)
    actions = [
        "on back tail tapping",
        "at feet treats",
        "walking across my computer",
        "sleeping on the couch",
    ]
    for action in actions:
        thought = read_louies_mind(action)
        print(f"{action!r} → {thought}")
    print() 
# # TODO: Add Function 5 - Your Choice
# def another_custom_function() -> None:
#     """
#     TODO: Create another function for your toolkit.
    
#     This function should:
#     - Solve a different real-world problem
#     - Use at least one other function from your toolkit
#     - Include error handling
#     """
#     # TODO: Implement this function
#     pass

# FUNCTION 5
def check_advisor_appointments():
    advisors = ["Asha", "Archana", "Peter", "Sarah", "Jason"]
    results = {}

    for name in advisors:
        made = input(f"Have you scheduled with {name}? (y/n): ").strip().lower()
        if made == "y":
            when = input(f"When is your appointment with {name}? ").strip()
            results[name] = f"Yes, on {when}"
        else:
            results[name] = "Not yet scheduled"

    return results

def demo_appointments() -> None:
    """Ask about advisor appointments and print them in a checklist style."""
    print("5. ADVISOR APPOINTMENT CHECKER")
    print("-" * 30)
    
    results = check_advisor_appointments()  # this will prompt you
    
    for name, status in results.items():
        if status.lower().startswith("yes"):
            when = status.split("Yes, on ", 1)[-1] if "Yes, on " in status else status
            print(f"[✔] {name} — {when}")
        else:
            print(f"[ ] {name} — not scheduled")
    print()


def display_menu() -> None:
    """Display an interactive menu for the toolkit."""
    print("\n" + "="*50)
    print("Professional Python Toolkit")
    print("="*50)
    print("1. Calculate tip and split bill")
    print("2. Plan study session with breaks")
    print("3. Calculate monthly savings")
    print("4. Track workout and calories")
    print("5. [Your Function 4 Name]")
    print("6. [Your Function 5 Name]")
    print("0. Exit")
    print("="*50)


def main() -> None:
    """
    Main program demonstrating all toolkit functionality.
    """
    print("Welcome to My Professional Python Toolkit!")
    print(f"Created by: Andrea Churchwell")
    print(f"Date: {datetime.date.today()}")
    print("\nThis toolkit helps me solve everyday problems:\n")
    
    # Demonstrate Function 0: Tip Calculator
    print("1. TIP CALCULATOR DEMO")
    print("-" * 30)
    tip, total, per_person = calculate_tip(75.50, 20, 3)
    print(f"Restaurant bill: $75.50")
    print(f"20% tip: ${tip}")
    print(f"Total: ${total}")
    print(f"Split 3 ways: ${per_person} each\n")
    
    # TODO: Demonstrate your Function 1
    print("2. STUDY PLANNER DEMO")
    print("-" * 30)
    time, breaks, formatted = study_time_planner(50, 2.0, 25)
    print(f"Reading 50 pages will take {formatted} with {breaks} breaks.\n")
    
    # Add your demo code here
    
    # TODO: Demonstrate your Function 2
    print("3. SAVINGS CALCULATOR DEMO")
    print("-" * 30)
    # Add your demo code here
    results = monthly_savings_calculator(3000, [1000, 200,100,100,100])
    print('results to monthly savings calc function: ', results)
    
    # TODO: Demonstrate Functions 3-5
    print('4. READ LOUIES MIND FUNCTION')
    print("-" * 30)
    # print(read_louies_mind("on back tail tapping"))
    # print(read_louies_mind("at feet treats"))
    # print(read_louies_mind("walking across my computer"))
    # print(read_louies_mind("sleeping on the couch"))
    demo_louie()

    demo_appointments()
    



    # Optional: Add interactive menu
    # Uncomment below to make toolkit interactive
    """
    while True:
        display_menu()
        choice = input("\nSelect an option (0-6): ")
        
        if choice == "0":
            print("Thanks for using the toolkit!")
            break
        elif choice == "1":
            # Tip calculator interaction
            pass
        # Add more choices...
    """


if __name__ == "__main__":
    main()
