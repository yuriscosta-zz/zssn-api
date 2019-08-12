from core.models import Survivor


def validate_survivor(id):
    survivor = Survivor.objects.filter(id=id).first()

    return survivor if survivor else False


def calculate_points(water, food, medication, ammunition):
    return int(water) * 4 + int(food) * 3 + int(medication) * 2 + int(ammunition) * 1


def are_points_equal(items):
    sender_points = calculate_points(items['sender_water'],
                                          items['sender_food'],
                                          items['sender_medication'],
                                          items['sender_ammunition'])
    receiver_points = calculate_points(items['receiver_water'],
                                            items['receiver_food'],
                                            items['receiver_medication'],
                                            items['receiver_ammunition'])

    return sender_points == receiver_points


def are_trade_components_valid(sender, receiver, items):
    is_sender_inventory_valid = sender.inventory.water >= items['sender_water'] and \
        sender.inventory.food >= items['sender_food'] and \
        sender.inventory.medication >= items['sender_medication'] and \
        sender.inventory.ammunition >= items['sender_ammunition']
    is_receiver_inventory_valid = receiver.inventory.water >= items['receiver_water'] and \
        receiver.inventory.food >= items['receiver_food'] and \
        receiver.inventory.medication >= items['receiver_medication'] and \
        receiver.inventory.ammunition >= items['receiver_ammunition']

    return is_sender_inventory_valid and is_receiver_inventory_valid


def trade_items(sender, receiver, items):
    sender.inventory.water += items['receiver_water']
    sender.inventory.water -= items['sender_water']
    sender.inventory.food += items['receiver_food']
    sender.inventory.food -= items['sender_food']
    sender.inventory.medication += items['receiver_medication']
    sender.inventory.medication -= items['sender_medication']
    sender.inventory.ammunition += items['receiver_ammunition']
    sender.inventory.ammunition -= items['sender_ammunition']

    receiver.inventory.water -= items['receiver_water']
    receiver.inventory.water += items['sender_water']
    receiver.inventory.food -= items['receiver_food']
    receiver.inventory.food += items['sender_food']
    receiver.inventory.medication -= items['receiver_medication']
    receiver.inventory.medication += items['sender_medication']
    receiver.inventory.ammunition -= items['receiver_ammunition']
    receiver.inventory.ammunition += items['sender_ammunition']

    sender.inventory.save()
    receiver.inventory.save()
