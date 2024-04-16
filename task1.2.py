# meal planner
import random
days =  ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
meals = ['Breakfast', 'Lunch', 'Dinner']
foods = ['Pizza', 'Burger', 'Fries', 'Pasta', 'Salad']
for day in days:
    for meal in meals:
        food = random.choice(foods)
        print ('On', day, 'for', meal, 'im having' , food)