import matplotlib.pyplot as plt 

def show_spending_by_category(expenses) :
    from collections import defaultdict

    category_totals = defaultdict(float)
    for exp in expenses :
        category_totals[exp['category']] += float(exp['amount'])

    labels = list(category_totals.keys())
    sizes = list(category_totals.values())

    plt.pie(sizes , labels= labels , autopct= '%1.1f')
    plt.title("Spending by Category")
    plt.show()
