class DataBase:
    def __init__(self):
        self.LinksDB = {}

    def addLink(self, Link):
        if Link.short_url in [Link.short_url for Link in self.LinksDB.values()]:
            return False
        self.LinksDB[Link.id] = Link
        return Link

    def searchLink(self, id):
        return self.LinksDB[id] if id in self.LinksDB else None

    def editLink(self, Link):
        if Link.id in self.LinksDB:
            self.LinksDB[Link.id] = Link
        else:
            return None
        return Link

    def deleteLink(self, id):
        if id in self.LinksDB:
            del self.LinksDB[id]
        else:
            return None
        return id

    def searchLinkByShortUrl(self, short_url):
        for Link in self.LinksDB.values():
            if Link.short_url == short_url:
                return Link
        return None

    def addView(self, id):
        if id in self.LinksDB:
            self.LinksDB[id].views += 1
        else:
            return None
        return id
