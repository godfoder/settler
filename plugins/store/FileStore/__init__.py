from settler.lib.plugins import Store

class FileStore(Store):
    pass

def setup(registry):
    registry.register(FileStore)