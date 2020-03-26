import os
import csv
import statistics

from data.data_types import Purchase


def main():
    print_header()
    filename = get_data_file()
    # print(filename)
    data = load_file(filename)
    query_data(data)


def print_header():
    print('-------------------------')
    print('     Real Estate App     ')
    print('-------------------------')


def get_data_file():  # getting the file name
    base_folder = os.path.dirname(__file__)  # searching file directory
    return os.path.join(base_folder, 'data',  # searching for file directory name 'data
                        'SacramentoRealEstateTransactions2008.csv')
    # return os.path.join('.', 'data', 'SacramentoRealEstateTransactions2008.csv')


# def load_file_basic(filename):
# with open(filename, 'r', encoding='utf-8') as fin:
#     # parsing csv in strings
#     # tackling csv files from scratch
#     header = fin.readline().strip()
#     print('found header: ' + header)
#
#     lines = []
#     for line in fin: # line by line
#         line_data = line.strip().split(',') # separate value by ','
#         bed_count = line_data[4]
#         lines.append(line_data)
#
#     print(lines[:5])


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin) # returns a collection of dicts
        purchases = []
        for row in reader:
            # p = Purchase()
            # p = p.create_from_dict(row) # attempting to use the self from the class by using p. (Purchase.)
            p = Purchase.create_from_dict(row) # directly work with the method otherwise create_from_dict doesn't work
            purchases.append(p)

        #print(purchases[0].__dict__)

        return purchases
            #print(type(row), row)
            #print("Bed count: {}".format(row["beds"])) data comes back as str

            # purchases.append(p)


        # header = fin.readline().strip()
        # reader = csv.reader(fin, delimiter = ',')  # fin is an iterable. data is split with the comma
        # for row in reader: # rows are lists
        #     print(type(row), row)


# def get_price(p):
#     return p.price


def query_data(data):  #list[Purchase]
    # if data was sorted by price:
    # get_price is passed on to data.sort
    #data.sort(key=get_price) # when it's time to get the key to sort, the get_price function will be called on each element of the list and will return the price of whatever the lists passes to it
    data.sort(key= lambda p: p.price) # because of lambda, I get the same info and I don't need the above function passed in
    # the Purchase class is in a list and so we have access to all of the attributes and method
    # most expensive house
    high_purchase = data[-1]
    #print(high_purchase.price)
    print("The most expensive house is ${:,} with {} beds and {} baths ".
          format(high_purchase.price, high_purchase.beds, high_purchase.baths))
    # least expensive house
    low_purchase = data[0]
    #print(low_purchase.price)
    print("The most least house is ${:,} with {} beds and {} baths ".
          format(low_purchase.price, low_purchase.beds,low_purchase.price))


    #average price house
    prices = []
    for pur in data:
        prices.append(pur.price)

    # prices = [ # an expression that builds the list
    #     p.price  # projection or items
    #     for p in data  # set to process
    # ]


    # print(prices)
    # return
    avg_price = statistics.mean(prices)
    print("The average cost of a house is: ${:,} ".format(int(avg_price)))

    # average price of 2 bedroom house

    # prices = []
    # for pur in data:
    #     if pur.beds == 2:
    #         prices.append(pur.price)

    # prices = [  # an expression that builds the list
    #     p.price  # projection or items
    #     for p in data  # set to process
    #   if p.beds == 2  # test/condition
    #
    # ]

    two_bedroom_home = [  # an expression that builds the list
        p  # projection or items
        for p in data  # set to process
        if p.beds == 2  # test/conditions
    ]

    #avg_price = statistics.mean(prices)
    avg_price = statistics.mean([p.price for p in two_bedroom_home])
    avg_baths = statistics.mean([p.baths for p in two_bedroom_home])
    avg_sq_ft = statistics.mean([p.sq__ft for p in two_bedroom_home])
    print("Average 2 bedroom home price is ${:,}, baths ={}, sq ft={:,}"
    .format(int(avg_price),round(avg_baths, 1),round(avg_sq_ft,1)))


def announce(item, msg):
    print("Pulling item {} for {}".format(item,msg))
    return item


if __name__ == '__main__':
    main()























#
# import os
# import csv
# import statistics
# from data.data_types import Purchase
#
#
# def main():
#     print_header()
#     filename = get_data_file()
#     # print(filename)
#     data = load_file(filename)
#     query_data(data)
#
#
# def print_header():
#     print('-----------------------------------')
#     print('        Real Estate Analysis       ')
#     print('-----------------------------------')
#
#
# def get_data_file():  # getting file name
#     base_folder = os.path.dirname(__file__)
#     return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')
#
#
# def load_file(filename):
#     with open(filename, 'r', encoding='utf-8') as fin:
#         reader = csv.DictReader(fin)
#         purchases = []
#         for row in reader:
#             p = Purchase.create_from_dict(row)
#             purchases.append(p)
#         # print(purchases[0].__dict__)
#         # print(type(row), row)
#         # print("Display City: {}".format(row['city']))
#
#         return purchases
#
#
# # def load_file(filename):
# #     # dealing with csv files from scratch
# #     with open(filename, 'r', encoding='utf-8') as fin:
# #         header = fin.readline().strip()
# #         print('found header: ' + header)
# #         lines = []
# #         for line in fin:
# #             line_data = line.strip().split(',')
# #             bed_count = line_data[4]  # just an example
# #             lines.append(line_data)
# #
# #         print(lines[:5])
#
#
# def query_data(data):  # list[Purchase]
#     data.sort(key=lambda p: p.price)
#     # most expensive house
#     most_expensive = data[-1]
#     print("The most expensive house is ${:,} with {} bed and {} baths"
#           .format(most_expensive.price, most_expensive.beds, most_expensive.baths))
#     # least expensive house
#     least_expensive = data[0]
#     print("The least expensive house is ${:,} with {} bed and {} baths"
#           .format(least_expensive.price, least_expensive.beds, least_expensive.baths))
#
#     # average price house
#     prices = [  # list comprehensions
#         p.price
#         for p in data
#     ]
#
#     average_price = statistics.mean(prices)
#     print("The average cost of a house is: ${:,} ".format(int(average_price)))
#
#     # Price of a 2 bedroom house
#
#     # for pur in data:
#     #     if pur.beds == 2:
#     #         prices.append(pur.price)
#     two_bedroom_homes = [
#         p
#         for p in data
#         if p.beds == 2
#     ]
#     # average_price = statistics.mean(prices)
#     average_price = statistics.mean(p.price for p in two_bedroom_homes)
#     average_baths = statistics.mean(p.baths for p in two_bedroom_homes)
#     average_sq_ft = statistics.mean(p.sq__ft for p in two_bedroom_homes)
#     print("Average 2 bedroom home price is ${:,}, baths ={}, sq ft={:,}"
#          .format(int(average_price),round(average_baths, 1),round(average_sq_ft,1)))
#
#
# if __name__ == '__main__':
#     main()
