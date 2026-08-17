def add_setting(dictionary, my_tuple):
    key = my_tuple[0].lower()
    value = my_tuple[1].lower()
    if key in dictionary.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dictionary.update({key: value})
        return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(dictionary, my_tuple):
    key = my_tuple[0].lower()
    value = my_tuple[1].lower()
    if key in dictionary.keys():
        dictionary[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(dictionary, key):
    key = key.lower()
    if key in dictionary.keys():
        dictionary.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return 'Setting not found!'


def view_settings(dictionary):
    if dictionary == {}:
        return 'No settings available.'
    lines = [(str(key)).capitalize() + ': ' + str(value) for key, value in dictionary.items()]

    return ('Current User Settings:\n' +
            '\n'.join(lines) + '\n')


test_settings = {'theme': 'dark', 'volume': 'high'}
view_settings(test_settings)











