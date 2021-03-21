__all__ = ["SerializerViewSetMixin"]


class SerializerViewSetMixin:
    serializer_class_map = {
        # 'create': None,
        # 'list': None,
        # 'retrieve': None,
        # 'update': None,
        # 'partial_update': None,
    }

    def get_serializer_class(self):
        serializer = self.serializer_class_map.get(self.action, None)
        self.serializer_class = serializer or self.serializer_class

        return self.serializer_class
