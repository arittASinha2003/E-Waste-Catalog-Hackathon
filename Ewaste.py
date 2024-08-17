class EwasteItem:
    def __init__(self, type, quantity, location):
        self.type = type
        self.quantity = quantity
        self.location = location

class CollectionPoint:
    def __init__(self, id, location):
        self.id = id
        self.location = location
        self.ewaste_items = []

class RecyclingFacility:
    def __init__(self, id, location, capacity):
        self.id = id
        self.location = location
        self.capacity = capacity
        self.current_waste = 0


ewaste_items = []
collection_points = []
recycling_facilities = []

def register_ewaste():
    type = input("Enter e-waste type: ")
    quantity = int(input("Enter quantity: "))
    location = input("Enter location: ")
    ewaste_item = EwasteItem(type, quantity, location)
    ewaste_items.append(ewaste_item)
    print("E-waste registered successfully.")

def register_collection_point():
    id = int(input("Enter collection point ID: "))
    location = input("Enter collection point location: ")
    collection_point = CollectionPoint(id, location)
    collection_points.append(collection_point)
    print("Collection point registered successfully.")

def register_recycling_facility():
    id = int(input("Enter recycling facility ID: "))
    location = input("Enter recycling facility location: ")
    capacity = int(input("Enter recycling facility capacity: "))
    recycling_facility = RecyclingFacility(id, location, capacity)
    recycling_facilities.append(recycling_facility)
    print("Recycling facility registered successfully.")

def collect_ewaste():
    collection_point_id = int(input("Enter collection point ID: "))
    collection_point = next((cp for cp in collection_points if cp.id == collection_point_id), None)
    if collection_point:
        print(f"Collected e-waste from collection point {collection_point_id}")
    else:
        print("Collection point not found.")

def recycle_ewaste():
    facility_id = int(input("Enter recycling facility ID: "))
    ewaste_type = input("Enter e-waste type to recycle: ")
    ewaste = next((item for item in ewaste_items if item.type == ewaste_type), None)
    if ewaste:
        facility = next((rf for rf in recycling_facilities if rf.id == facility_id), None)
        if facility and facility.capacity >= ewaste.quantity:
            facility.current_waste += ewaste.quantity
            ewaste_items.remove(ewaste)
            print(f"Recycled {ewaste.quantity} units of {ewaste.type} at facility {facility_id}")
        else:
            print("Recycling facility not found or capacity exceeded.")
    else:
        print("E-waste type not found.")

def generate_report():
    total_ewaste = sum(item.quantity for item in ewaste_items)
    print(f"Total e-waste collected: {total_ewaste} units")

def main():
    while True:
        print("\nE-waste Management System")
        print("1. Register E-waste")
        print("2. Register Collection Point")
        print("3. Register Recycling Facility")
        print("4. Collect E-waste")
        print("5. Recycle E-waste")
        print("6. Generate Report")
        print("7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            register_ewaste()
        elif choice == 2:
            register_collection_point()
        elif choice == 3:
            register_recycling_facility()
        elif choice == 4:
            collect_ewaste()
        elif choice == 5:
            recycle_ewaste()
        elif choice == 6:
            generate_report()
        elif choice == 7:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
