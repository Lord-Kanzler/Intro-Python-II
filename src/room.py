# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
	def __init__(self, name, description, items=None):
	self.name = name
	self.description = description
	if(items is None):
        self.items = {}
    else:
        self.items = {item.id:item for item in items}

    #Available rooms to direction
	self.n_to = None
	self.s_to = None
	self.e_to = None
	self.w_to = None

	# def __str__(self):
	# output = ""
	# output += f"Room: {self.name}\n"
	# output += f"Description: {self.description}"

	# if len(self.items) > 0:
	# for index, item in enumerate(self.items):
	# output += "\nRoom Item: "+str(item)

	# return output

    # Accessor method to return  key/value pairs of the items dict
    def view_items(self):
        return items.items()
