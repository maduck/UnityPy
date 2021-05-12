from .NamedObject import NamedObject
from .PPtr import PPtr


class AssetInfo:
    def __init__(self, reader):
        self.preload_index = reader.read_int()
        self.preload_size = reader.read_int()
        self.asset = PPtr(reader)


class AssetBundle(NamedObject):
    def __init__(self, reader):
        super().__init__(reader=reader)
        preload_table_size = reader.read_int()
        self.m_PreloadTable = [PPtr(reader) for _ in range(preload_table_size)]
        container_size = reader.read_int()
        self.m_Container = {}
        # TODO - m_Container is a multi-dict, multiple values can have the same key
        for i in range(container_size):
            key = reader.read_aligned_string()
            asset_info = AssetInfo(reader)
            new_key = f'{asset_info.asset.type}-{key}'
            self.m_Container[new_key] = asset_info
