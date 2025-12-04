# --------------------------------------------------
# PORTADA
# Name: Jesus Adrian Ramos Rodriguez
# Matricula: 2530056
# Group: IM-1-2
#
# RESUMEN EJECUTIVO (5-8 lines)
# A CRUD is a basic data manager that supports Create, Read, Update and Delete operations.
# Create -> add new item, Read -> retrieve item by id, Update -> change item fields, Delete -> remove item.
# I chose a dict mapping item_id -> dict for O(1) lookups and simpler uniqueness checks.
# Using functions organizes logic (validation, storage, IO separation) and makes the code testable.
# Program covers: interactive menu, create, read, update, delete and list operations + tests.
#
# Problem: In-memory CRUD manager with functions
#
# Description:
# This program implements a simple in-memory CRUD manager for items (e.g., inventory products).
# Each item has: id (string), name (string), price (float), quantity (int).
# The main data structure is a dict: items_db = { item_id: {"name":..., "price":..., "quantity":...} }
#
# Inputs:
#  - option (int) from menu
#  - for create/update: item_id (str), name (str), price (floatable), quantity (intable)
#  - for read/delete: item_id (str)
#
# Outputs:
#  - Messages such as: "Item created", "Item updated", "Item deleted", "Item not found", "Items list:",
#    or "Error: invalid input".
#
# Validations:
#  - menu option must be valid (0..5)
#  - item_id must not be empty after strip()
#  - price must be a float >= 0.0
#  - quantity must be an int >= 0
#  - create: disallow duplicate id (policy: reject creation if id already exists)
#  - read/update/delete: if id not found -> "Item not found"
#
# Test cases (implemented in run_tests()):
#  1) Normal: create -> read -> update -> delete (verifies messages and final state)
#  2) Border: create item with quantity = 0 and very short id (e.g., "a")
#  3) Error: invalid menu option, empty id, non-numeric price -> expect "Error: invalid input" or "Item not found"
#
# Diagram (optional):
#  - Flow (text): Start -> Show Menu -> Read Option -> Validate -> Call CRUD function -> Show Result -> Repeat or Exit
#
# --------------------------------------------------

# CONSTANTS
EXIT_OPTION = 0
CREATE_OPTION = 1
READ_OPTION = 2
UPDATE_OPTION = 3
DELETE_OPTION = 4
LIST_OPTION = 5
MAX_ITEMS = 1000  # arbitrary limit (not enforced strictly)

# Main data structure: dict mapping id -> dict(item fields)
# Option chosen: dict (fast lookup by id; avoids scanning list to find item)
items_db = {}

# --------- Helper / Validation Functions ---------

def is_valid_id(item_id):
    """Return True if item_id is non-empty after stripping."""
    if item_id is None:
        return False
    return bool(str(item_id).strip())

def parse_price(value):
    """Try to parse value to float and validate >= 0.0. Return (True, float_val) or (False, None)."""
    try:
        price = float(value)
        if price < 0.0:
            return False, None
        return True, price
    except (ValueError, TypeError):
        return False, None

def parse_quantity(value):
    """Try to parse value to int and validate >= 0. Return (True, int_val) or (False, None)."""
    try:
        q = int(value)
        if q < 0:
            return False, None
        return True, q
    except (ValueError, TypeError):
        return False, None

# --------- CRUD Functions ---------

def create_item(db, item_id, name, price_value, quantity_value):
    """
    Create an item in db.
    Returns True if created, False on validation error or if id exists.
    Policy: do NOT allow duplicate ids.
    Messages printed: "Item created" or "Error: invalid input"
    """
    # Validate id
    if not is_valid_id(item_id):
        print("Error: invalid input")
        return False

    item_id = str(item_id).strip()
    # Check duplicate
    if item_id in db:
        # We reject duplicates (documented decision)
        print("Error: invalid input")
        return False

    # Validate name
    if name is None or not str(name).strip():
        print("Error: invalid input")
        return False

    # Validate price
    ok, price = parse_price(price_value)
    if not ok:
        print("Error: invalid input")
        return False

    # Validate quantity
    okq, quantity = parse_quantity(quantity_value)
    if not okq:
        print("Error: invalid input")
        return False

    # Create
    db[item_id] = {
        "name": str(name).strip(),
        "price": price,
        "quantity": quantity
    }
    print("Item created")
    return True

def read_item(db, item_id):
    """
    Return the item dict if exists, None otherwise.
    Prints "Item not found" if missing.
    """
    if not is_valid_id(item_id):
        print("Error: invalid input")
        return None
    item_id = str(item_id).strip()
    item = db.get(item_id)
    if item is None:
        print("Item not found")
        return None
    # Print readable representation
    print(f"Item found: id={item_id}, name={item['name']}, price={item['price']}, quantity={item['quantity']}")
    return item

def update_item(db, item_id, new_name=None, new_price_value=None, new_quantity_value=None):
    """
    Update fields of an existing item. Fields set to None are left unchanged.
    Returns True if updated, False on error or if item not found.
    Prints "Item updated", "Item not found", or "Error: invalid input".
    """
    if not is_valid_id(item_id):
        print("Error: invalid input")
        return False
    item_id = str(item_id).strip()
    if item_id not in db:
        print("Item not found")
        return False

    # Validate name if provided
    if new_name is not None and not str(new_name).strip():
        print("Error: invalid input")
        return False

    # Validate price if provided
    if new_price_value is not None:
        ok, new_price = parse_price(new_price_value)
        if not ok:
            print("Error: invalid input")
            return False
    else:
        new_price = None

    # Validate quantity if provided
    if new_quantity_value is not None:
        okq, new_quantity = parse_quantity(new_quantity_value)
        if not okq:
            print("Error: invalid input")
            return False
    else:
        new_quantity = None

    # Apply updates
    if new_name is not None:
        db[item_id]["name"] = str(new_name).strip()
    if new_price is not None:
        db[item_id]["price"] = new_price
    if new_quantity is not None:
        db[item_id]["quantity"] = new_quantity

    print("Item updated")
    return True

def delete_item(db, item_id):
    """
    Delete item by id. Returns True if deleted, False if not found or invalid input.
    Prints "Item deleted", "Item not found", or "Error: invalid input".
    """
    if not is_valid_id(item_id):
        print("Error: invalid input")
        return False
    item_id = str(item_id).strip()
    if item_id not in db:
        print("Item not found")
        return False
    del db[item_id]
    print("Item deleted")
    return True

def list_items(db):
    """
    Print all items in a readable format and return a list of tuples (id, item_dict).
    Prints "Items list:" then each item line. If empty, prints "Items list: (empty)".
    """
    print("Items list:")
    if not db:
        print("(empty)")
        return []
    for k, v in db.items():
        print(f"- id={k}, name={v['name']}, price={v['price']}, quantity={v['quantity']}")
    return list(db.items())

# --------- Menu / Interactive Loop ---------

def show_menu():
    print("\n--- Main Menu ---")
    print(f"{CREATE_OPTION}) Create item")
    print(f"{READ_OPTION}) Read item by id")
    print(f"{UPDATE_OPTION}) Update item by id")
    print(f"{DELETE_OPTION}) Delete item by id")
    print(f"{LIST_OPTION}) List all items")
    print(f"{EXIT_OPTION}) Exit")

def handle_create():
    item_id = input("Enter item id: ").strip()
    name = input("Enter name: ").strip()
    price = input("Enter price: ").strip()
    quantity = input("Enter quantity: ").strip()
    create_item(items_db, item_id, name, price, quantity)

def handle_read():
    item_id = input("Enter item id to read: ").strip()
    read_item(items_db, item_id)

def handle_update():
    item_id = input("Enter item id to update: ").strip()
    # For update we allow skipping fields by pressing Enter
    name = input("Enter new name (leave blank to keep current): ")
    price = input("Enter new price (leave blank to keep current): ")
    quantity = input("Enter new quantity (leave blank to keep current): ")
    # Convert blank to None
    name_param = None if name.strip() == "" else name
    price_param = None if price.strip() == "" else price
    quantity_param = None if quantity.strip() == "" else quantity
    update_item(items_db, item_id, new_name=name_param, new_price_value=price_param, new_quantity_value=quantity_param)

def handle_delete():
    item_id = input("Enter item id to delete: ").strip()
    delete_item(items_db, item_id)

def main_loop():
    while True:
        show_menu()
        option = input("Select option: ").strip()
        # Validate option numeric and in allowed range
        try:
            opt = int(option)
        except ValueError:
            print("Error: invalid input")
            continue
        if opt == EXIT_OPTION:
            print("Exiting program. Goodbye.")
            break
        elif opt == CREATE_OPTION:
            handle_create()
        elif opt == READ_OPTION:
            handle_read()
        elif opt == UPDATE_OPTION:
            handle_update()
        elif opt == DELETE_OPTION:
            handle_delete()
        elif opt == LIST_OPTION:
            list_items(items_db)
        else:
            print("Error: invalid input")

# --------- Test Cases (Normal, Border, Error) ---------

def run_tests():
    """
    Run 3 test scenarios and print results.
    Tests do not require user interaction and demonstrate function usage.
    """
    print("\n=== Running automated tests ===\n")
    # Clear db
    db = {}
    print("Test 1 (Normal): create -> read -> update -> delete")
    # Create
    assert create_item(db, "100", "Widget", "12.5", "10") is True
    # Read
    item = read_item(db, "100")
    assert item is not None and item["name"] == "Widget"
    # Update
    assert update_item(db, "100", new_name="SuperWidget", new_price_value="15.0", new_quantity_value="5") is True
    # Verify update
    item2 = db.get("100")
    assert item2["name"] == "SuperWidget" and item2["price"] == 15.0 and item2["quantity"] == 5
    # Delete
    assert delete_item(db, "100") is True
    assert "100" not in db
    print("Test 1 passed.\n")

    print("Test 2 (Border): create item with quantity=0 and short id 'a'")
    assert create_item(db, "a", "Tiny", "0.0", "0") is True
    assert db["a"]["quantity"] == 0
    print("Test 2 passed.\n")

    print("Test 3 (Error cases): invalid inputs")
    # Invalid menu option - simulated by calling validation (we cannot simulate input here; check function behavior)
    # Empty id on create
    assert create_item(db, "", "NoID", "1.0", "1") is False
    # Non-numeric price
    assert create_item(db, "b", "BadPrice", "abc", "1") is False
    # Negative quantity
    assert create_item(db, "c", "NegQ", "1.0", "-5") is False
    # Read non-existent
    assert read_item(db, "nonexistent") is None
    # Update non-existent
    assert update_item(db, "nonexistent", new_name="X") is False
    # Delete non-existent
    assert delete_item(db, "nonexistent") is False
    print("Test 3 passed.\n")

    print("All tests executed. Current DB state:")
    list_items(db)
    print("\n=== Tests finished ===\n")

# --------- If run as script ---------
if __name__ == "__main__":
    # If user wants to auto-run tests, they can pass a special prompt at start
    print("CRUD Manager (in-memory). Type 'tests' to run automated tests, or press Enter to continue to menu.")
    initial = input("Enter command (or press Enter): ").strip().lower()
    if initial == "tests":
        run_tests()
    else:
        print("Starting interactive menu...")
        main_loop()

# --------------------------------------------------
# CONCLUSIONS (Comments at end) - 5 to 8 lines
# Using functions reduced repetition and separated concerns: validation, storage, and user I/O.
# The dict structure made lookups and uniqueness enforcement straightforward and efficient.
# Input validation was the trickiest part (parsing floats/ints and handling blanks); helper functions simplified it.
# The modular design makes it easy to extend the program (e.g., persist to file or DB, add search filters).
# For larger systems, functions here could be adapted as methods of a repository class and backed by SQLite or JSON files.
#
# REFERENCES (minimum 3)
# 1) Python documentation - Built-in Types (dict, list): https://docs.python.org/3/library/stdtypes.html
# 2) Python documentation - Defining functions: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# 3) Real Python - Working with JSON Data in Python: https://realpython.com/python-json/
# 4) Tutorialspoint - CRUD Operations using Python: https://www.tutorialspoint.com/python/python_database_access.htm
#
# GITHUB REPOSITORY URL:
# Replace the URL below with your repository URL that contains this assignment.
# Example placeholder:
# https://github.com/2530056-boop/Homeworks_Python_jaar.git
#
# --------------------------------------------------
