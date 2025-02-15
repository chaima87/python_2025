expenses =[
    {'date': '05-02-2025', 'amount':200, 'category': 'grocerie', 'description': 'weekly groceries shopping'}
]
def add_expense(date, amount, category, description):
    if amount < 0:
        return "the amount should be more than 0"
    expense = {
        'date': date,
        'amount': amount,
        'category': category,
        'description': description
    }
    expenses.append(expense)
    return "expense added successfuly!"

def view_expenses():
    if not expenses:
        return "no expenses recorded "
    
    total_spent = 0
    for ex in expenses:
        print(f"date:{ex['date']}, amount:{ex['amount']}, category:{ex['category']}, description:{ex['description']}")
        total_spent += ex['amount']
    print(f"total amount spent:{total_spent}")
    
    add_expense('05-02-2025', 10 , 'entertainment', 'movie_tickets')
    add_expense('12-02-2025', 30, 'entertainment', 'paintball' )
    add_expense(amount=80.50, date='07-10-2025', category='dining out', description='dining at restaurant with freinds')
    print(view_expenses())







result = add_expense('12-02-2025', 20, 'entertainement','movie tickets')
print(result)