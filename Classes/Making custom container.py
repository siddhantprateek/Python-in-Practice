# list , dictionary,sets and so on.  these data structures are container types
# and are useful and sufficient for most cases .But there are times we want to create
# our own custom container types.

# through the class we can keep track of the number of various tags in a block.

# to create your own custom container types
class TagCloud:
    def __init__(self):
        self.tags = {}  # initializing tags attribute to an empty dictionary

    def add(self, tag):  # we have to check wheather the tag is in our dictionary , if we don't have it we set it's value to 1 or increment by 1
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1
    #      all tags to lower           we use 'get' method to get items by 'tag' key
    #                            (tag, <supply a default value for this key> 0)
    # the 'tag' takes the value or input and convert it into lower case seen in the expression.

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    # we have to do is to use one of the built in function to get
    # iter object. A Iterator object is an object that wants a container and
    # gets one item at a time.
    def __iter__(self):
        return iter(self.tags)


# programme is to make it more smarter than a typical dictionary
cloud = TagCloud()
# to read the count of tag
cloud["python"] = 10
# cloud.
print(cloud.tags)
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)
