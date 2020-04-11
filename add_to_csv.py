# store form data into csv
from csv import DictWriter
 
def add_to_csv(name, email, phone, message):

    field_names = ['name', 'email', 'phone_no', 'message']
    dict_of_elem = {'name': name, 'email': email, 'phone_no': phone, 'message': message}
    # Open file in append mode
    with open('feedback.csv', 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_names, dialect='excel')
        # Add dictionary as wor in the csv
        dict_writer.writerow(dict_of_elem)
