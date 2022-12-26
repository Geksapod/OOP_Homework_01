import product
import customer
import order


if __name__ == '__main__':
    try:
        battery_1 = product.Product('battery ABP7-12L', 776, '12v 7Ah AGM', '156 x 94 x 65')
        battery_2 = product.Product('battery AGM LPM 6V - 12 Ah', 658, '6v 12Ah AGM', '151 x 96 x 50')
        battery_3 = product.Product('battery LP1212', 1798, '12v 12Ah gel', '151 x 98 x 95')
        battery_4 = product.Product('battery GEL 12-12A-BS', 1290, '12v 10Ah gel', '150 x 87 x 106')

        customer_1 = customer.Customer('Petrenko', 'Petro', '+380123123123', 'Kyiv')
        order_1 = order.Order('No 0001', customer_1)
        order_1.add_product(battery_1, battery_1.price, quantity=2)
        order_1.add_product(battery_4, battery_4.price)
        order_1.add_product(battery_2, battery_2.price)

    except (TypeError, ValueError) as error:
        print(error)

    print(order_1, "\n")

    try:
        print(f"{order_1[battery_2][0]} - {order_1[battery_1][1]} pcs\n")

        for items in order_1:
            product, quantity = (*items,)
            print(f"{product} - {quantity} pcs")

        print(f"{order_1[battery_3][0]} - {order_1[battery_1][1]} pcs")

    except KeyError as error:
        print(error)












