import pulp

# Створення проблеми максимізації
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні для кількості вироблених лимонаду і фруктового соку
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

# Цільова функція - максимізація загальної кількості вироблених продуктів
model += lemonade + fruit_juice, "Total_Products"

# Обмеження на ресурси
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water"
model += 1 * lemonade <= 50, "Sugar"
model += 1 * lemonade <= 30, "Lemon_Juice"
model += 2 * fruit_juice <= 40, "Fruit_Puree"

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Статус:", pulp.LpStatus[model.status])
print("Кількість виробленого лимонаду:", pulp.value(lemonade))
print("Кількість виробленого фруктового соку:", pulp.value(fruit_juice))
