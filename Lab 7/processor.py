import math


def sanitize_license_plate(plate):
    """Remove delimiters from a license plate and upper-case it.
    Returns "" for non-string input (None, numbers, etc.)."""
    if not isinstance(plate, str):
        return ""
    plate = plate.strip()
    for ch in ['-', ' ', '_', '#']:
        plate = plate.replace(ch, '')
    return plate.upper()


def parse_trip_mileage(mileage_csv):
    """Parse a comma-separated string of mileages into a list of floats.
    Invalid, empty, negative, NaN or infinite entries are skipped.
    Returns [] for non-string or empty input."""
    if not isinstance(mileage_csv, str):
        return []
    result = []
    for part in mileage_csv.split(','):
        part = part.strip()
        if not part:
            continue
        try:
            value = float(part)
        except ValueError:
            continue
        if math.isfinite(value) and value >= 0:
            result.append(value)
    return result


def format_rental_invoice(record):
    """Format 'Driver:Days:Category' into an invoice string.
    Returns an 'Invalid rental record' message for any bad input."""
    if not isinstance(record, str):
        return "Invalid rental record: input must be text"
    parts = record.split(':')
    if len(parts) != 3:
        return "Invalid rental record: expected Driver:Days:Category"
    driver = parts[0].strip()
    category = parts[2].strip()
    if not driver or not category:
        return "Invalid rental record: driver and category cannot be empty"
    try:
        days = int(parts[1].strip())
    except ValueError:
        return "Invalid rental record: days must be a whole number"
    if days <= 0:
        return "Invalid rental record: days must be positive"
    daily_rate = 50.0 if category.lower() == "suv" else 30.0
    total = days * daily_rate
    return f"Driver {driver} booked {category} for {days} days: Total ${total:.2f}"


def main():
    print("==== Running sanitize_license_plate ====")
    raw_plate = input("Enter license plate with delimiters (-, _, #): ")
    clean_plate = sanitize_license_plate(raw_plate)
    print("Sanitized Plate:", clean_plate)

    print("\n==== Running parse_trip_mileage ====")
    csv_input = input("Enter CSV of mileages (e.g. 100.5, 45.2, 80.0): ")
    mileage_list = parse_trip_mileage(csv_input)
    print("Parsed Mileage List:", mileage_list)

    print("\n==== Running format_rental_invoice ====")
    record_input = input("Enter rental record (Driver:Days:Category): ")
    invoice = format_rental_invoice(record_input)
    print("Rental Invoice:", invoice)


if __name__ == "__main__":
    main()