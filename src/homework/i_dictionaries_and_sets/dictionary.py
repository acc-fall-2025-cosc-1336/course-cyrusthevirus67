def add_inventory(widgets: dict, widget_name: str, quantity: int) -> None:
    """
    Add or update a widget in the inventory.

    - If widget_name is not in widgets, add it with the given quantity.
    - If it exists, increase its quantity by the given amount (can be negative).
    """
    if widget_name in widgets:
        widgets[widget_name] += quantity
    else:
        widgets[widget_name] = quantity


def remove_inventory_widget(widgets: dict, widget_name: str) -> str:
    """
    Remove widget_name from widgets if it exists.

    - If it exists: delete it and return 'Record deleted'
    - If it does not exist: return 'Item not found'
    """
    if widget_name in widgets:
        del widgets[widget_name]
        return "Record deleted"
    else:
        return "Item not found"
