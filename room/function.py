def slug_create(room_name):
    slug = ''
    for i in room_name:
        if 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57:
            slug += i
        else:
            slug += '_'
    return slug
