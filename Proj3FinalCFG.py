# Our project was a spreadsheet analysis
# we did a sales analysis for the duration of a year
# Tasks: (1) read the data; (2) collect all sales from each cell into single list;
# (3) output total sales across all months.
# Extra: (1) output result summary; (2) calculate: monthly changes as %;
# (2) avg; (3) month with highest to lowest sales.

import csv  # to read CSV file and import csv library
import statistics
import matplotlib.pyplot as plt
import seaborn as sns

filename= "sales.csv"

with open('sales.csv') as csv_file:  # defaults to 'r' only
    rows = csv.DictReader(csv_file)  # same as csvreader = csv.reader(csv_file)
    sales = []  # list with the same keys
    month_to_sales = {}  # dictionary

    for row in rows:  # iterate through 'rows' data each item 'row' each item is dictionary is variable name
        sale = int(row['sales'])  # variable 'sale' to value
        sales.append(sale)  # to add a single element to the list

    total = sum(sales)  # function to output results
    print('Total sales: {}'.format(total))  # str format as a method place-holdder for values

    average = round(statistics.mean(sales))
    # average = sum(sales)/len(sales)
    print('Average sales: {}'.format(average))


with open('summary.csv', 'w') as csvfile:   # open function pass 'w' argument mode 'as' file handler object
    fieldnames = ['summary statistics', 'values', 'month']  # define the columns to use into variable 'fieldnames' as keys
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  # list of fields to key parameter
    # now begin adding lines to the file
    writer.writeheader()  # call '' to get headers on writer object as first row passed to all fieldnames
    writer.writerow({'summary statistics': 'Total sales', 'values': total})
    writer.writerow({'summary statistics': 'Average sales', 'values': average})


with open('sales.csv') as csv_file:  # defaults to 'r' only
    rows = csv.DictReader(csv_file)  # iterate through 'rows' data each item 'row' each item is dictionary

    sales = []
    month_to_sales = {}
    for row in rows:  # used 'for' operator to run through list with code
        # could have used a function with multiple arguments?
        sale = int(row['sales'])  # values name
        month_to_sales.update({row['month']:sale})
        # print(row['month'])
        # print(sale)
        sales.append(sale)
    # print(month_to_sales)

    min_sales = min(sales)
    # for key,value in month_to_sales.items():
    #     print(key,value)
    for month in month_to_sales:
        # print(month)
        # print(month_to_sales[month])
        sale = month_to_sales[month]
        if sale == min_sales:  # conditional run equal to
            print('Month with minimum sales: {} {}'.format(month, sale))
            from csv import writer

            minimum_sales = 'Month with minimum sales', sale, month

            with open('summary.csv', 'a') as f_object:  # 'a' is append mode
                # Pass this file object to csv.writer()
                # and get a writer object
                writer_object = writer(f_object)

                # Pass the list as an argument into
                # the writerow()
                writer_object.writerow(minimum_sales)

    max_sales = max(sales)
    # for key,value in month_to_sales.items():
    #     print(key,value)
    for month in month_to_sales:
        # print(month)
        # print(month_to_sales[month])
        sale = month_to_sales[month]
        if sale == max_sales:
            print('Month with maximum sales: {} {}'.format(month, sale))
            from csv import writer

            maximum_sales = 'Month with maximum sales', sale, month

            with open('summary.csv', 'a') as f_object:  # 'a' is append mode
                # Pass this file object to csv.writer()
                # and get a writer object
                writer_object = writer(f_object)

                # Pass the list as an argument into
                # the writerow()
                writer_object.writerow(maximum_sales)

with open('sales.csv') as csv_file:  # defaults to 'r' only
    rows = csv.DictReader(csv_file)
    # or
    # csvreader = csv.reader(csv_file)
    sales = []
    # month_to_sales = {}
    # percentage_to_month = {}
    for row in rows:
        sale = int(row['sales'])
        # month_to_sales.update({row['month']:sale})
        # print(row['month'])
        # print(sale)
        sales.append(sale)
    print(month_to_sales)

    for month in month_to_sales:
        sale_for_this_month = month_to_sales[month]

    for index in range(len(sales)):
        # print(index)
        if index != 0:
            difference = sales[index]-sales[index-1]
            per_increase = round((difference/sales[index-1])*100)
            print(str(per_increase) +'%')

with open('sales.csv') as csv_file:  # defaults to 'r' only
    rows = csv.DictReader(csv_file)

    profits = []
    for row in rows:
        sale = int(row['sales'])

        expend = int(row['expenditure'])

        profit_per_mon = sale - expend

        profits_int = int(profit_per_mon)
        profits.append(profits_int)

        print(profit_per_mon)

        total_profit = sum(profits)
    print('Total Profit: {}'.format(total_profit))

    from csv import writer

    Profit = 'Total Profit', total_profit

    with open('summary.csv', 'a') as f_object:  # 'a' is append mode
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)

        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(Profit)

#  Are we going bankrupt?

    if total_profit > 0:
        print("Status: You are going to be rich")
    else:
        print("Status: You to sell the company and run")

with open('sales.csv') as csv_file:  # defaults to 'r' only
    rows = csv.DictReader(csv_file)
    # or
    # csvreader = csv.reader(csv_file)
    sales = []
    months = []
    profits = []
    Expenditures = []
    # month_to_sales = {}
    # percentage_to_month = {}
    for row in rows:
        sale = int(row['sales'])
        # month_to_sales.update({row['month']:sale})
        # print(row['month'])
        # print(sale)
        sales.append(sale)

        month = row['month']
        months.append(month)

    for row in rows:
        sale = int(row['sales'])
        expend = int(row['expenditure'])
        profit_per_mon = sale - expend

        profits_int = int(profit_per_mon)
        profits.append(profits_int)

        print(profit_per_mon)

        total_profit = sum(profits)
    print('Total Profit: {}'.format(total_profit))

    x = months
        # y axis values
    y = sales
#
#
#
