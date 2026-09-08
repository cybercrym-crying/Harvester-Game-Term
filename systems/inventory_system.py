from entities.item import Item, ItemStack
from core.enums import ItemType
import copy
from InquirerPy import inquirer
from rich.table import Table, Console


class InventorySystem:
    def __init__(self):
        self.slot = 10
        self.inventory_item: list[ItemStack | None] = [None] * self.slot

    def sort_by_name(self):
        self.inventory_item.sort(
            key=lambda item_stack: (
                item_stack.item.name if item_stack is not None else ""
            )
        )

    def sort_by_type(self):  # sort item by name and stackit
        self.inventory_item.sort(
            key=lambda item_stack: (
                item_stack.item._item_type.name if item_stack is not None else ""
            )
        )

    def add_new_item(self, new_item: ItemStack, type_add="default"):
        while new_item.quantity > 0:
            if new_item.item._item_type != ItemType.TOOLS and type_add == "default":
                found = next(
                    (
                        slot
                        for slot in self.inventory_item
                        if slot
                        and slot.item.name == new_item.item.name
                        and slot.quantity < 33
                    ),
                    False,
                )
            else:
                found = False
            if isinstance(found, ItemStack):
                new_item.quantity = found.add_quantity(new_item.quantity)
                continue
            else:
                try:
                    empty_slot = self.inventory_item.index(None)
                    new_slot = copy.deepcopy(new_item)
                    self.inventory_item[empty_slot] = new_slot
                    new_slot.quantity = 0
                    new_item.quantity = new_slot.add_quantity(new_item.quantity)
                except ValueError:
                    print("Your Bag Is Full")
                    return

    def delete_item(self, index):
        if index <= 10 and index >= 1:
            index -= 1
            m = f"Are you sure, wanted to delete item {self.inventory_item[index].item.name}"
            confirm = inquirer.select(
                message=m,
                choices=["Yes", "No"],
            ).execute()
            if confirm == "Yes":
                self.inventory_item[index] = None
                return
            else:
                return
        print("Item Not Found")
        return

    def split_item(self, index, amount):
        if (
            self.inventory_item[index].item._item_type != ItemType.TOOLS
            and index <= 10
            and index >= 1
            and amount > 0
            and amount < self.inventory_item[index].quantity
        ):
            index -= 1
            m = f"Are you sure, wanted to split item {self.inventory_item[index].item.name}"
            confirm = inquirer.select(
                message=m,
                choices=["Yes", "No"],
            ).execute()
            if confirm == "Yes":
                split_item = copy.deepcopy(self.inventory_item[index])
                split_item.quantity = amount
                self.add_new_item(split_item, "split")
                self.inventory_item[index].quantity -= amount
                return
            else:
                return
        print("Item Not Found")
        return

    def get_info(self):
        table = Table(title="🎒 Bag", style="cyan", title_style="bold magenta")
        table.add_column("Slot", justify="center", style="dim", width=5)
        table.add_column("Item Name", style="bold white")
        table.add_column("Price", justify="right", style="yellow")
        table.add_column("Quantity", justify="right", style="yellow")
        table.add_column("Type", justify="right", style="red")
        console = Console()
        slot = 1
        for info in self.inventory_item:
            if info != None:
                data = info.get_info()
                table.add_row(
                    f"{slot}",
                    f"{data["name"]}",
                    f"{data["price"]}",
                    f"{data["quantity"]}",
                    f"{data["type"].name}",
                )
            slot += 1
        console.print(table)
