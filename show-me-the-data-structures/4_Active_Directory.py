from data_structures import BinaryTree

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []
        self.users_b = BinaryTree()

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)
        self.users_b.insert(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):

    if user == group.get_name():
        return True
    if group.get_users() and group.users_b.search(user):
        return True
    for g in group.get_groups():
        return is_user_in_group(user, g)

    else: return  False


if __name__ == '__main__':
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    assert is_user_in_group("child", child) == True, 'Failed'
    assert is_user_in_group("", child) == False, 'Failed'
    assert is_user_in_group("sub_child_user", parent)  == True, 'Failed'
