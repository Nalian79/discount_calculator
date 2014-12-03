import logging

logging.basicConfig(filename="output.log", level=logging.DEBUG)

def calculate_discount(item_cost, relative_discount, absolute_discount):
    """ Calculate the discount on an item from a shopping cart """

    logging.info("Running program with inputs {}, {}, {}".format(
            item_cost, relative_discount, absolute_discount))
    item_cost = float(item_cost)
    relative_discount = float(relative_discount)
    absolute_discount = float(absolute_discount)
    if item_cost <= 0 or relative_discount < 0 or absolute_discount < 0:
        raise ValueError("Negative and zero numbers are not valid")
    cost = item_cost
    logging.debug("Turning item_cost into a float: {!r}".format(cost))
    # Steepest discount we will give is 90%
    lowest_cost = cost - (cost * (90.0/100.0))
    logging.debug("Lowest posible cost for item is: {!r}".format(lowest_cost))

    cost = cost - (cost * (relative_discount/100.0))

    logging.debug("After the relative discount, cost is: {!r}".format(cost))
    if not cost <= lowest_cost:
        final_cost = cost - absolute_discount
    else:
        print("Item discount is at 90% already!")
        return lowest_cost
    if not final_cost <= lowest_cost:
        logging.debug("After the absolute discount, cost is: {!r}".format(
                final_cost))
        return final_cost
    else:
        logging.debug(
            "Default discount of 90% applied: {!r} is invalid price.".format(
                final_cost))
        return lowest_cost
