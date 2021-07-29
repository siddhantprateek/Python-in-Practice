class Tagcloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag, 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag, 0)


cloud = Tagcloud()

cloud.add("py")
cloud.add("py")
cloud.add("py")

print(cloud.tags)
