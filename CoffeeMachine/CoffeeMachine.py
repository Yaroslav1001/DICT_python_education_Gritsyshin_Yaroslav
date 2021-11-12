print('Starting to make a coffee\nGrinding coffee beans\nBoiling water\nMixing boiled water with crushed coffee beans')
print('Pouring coffee into the cup\nPouring some milk into the cup\nCoffee is ready!')
coffee_water = 200
coffee_milk = 50
coffee_beans = 15
count_cups = int(input("\nWrite how many cups of coffee you will need:"))
water = count_cups * coffee_water
milk = count_cups * coffee_milk
beans = count_cups * coffee_beans
print('For ' + str(count_cups) + ' cups of coffee you will need:')
print(str(water) + ' ml of water')
print(str(milk) + ' ml of milk')
print(str(beans) + ' g of coffee beans')