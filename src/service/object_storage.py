import logging

from swiftclient.service import SwiftService, SwiftUploadObject, SwiftError
from swiftclient.exceptions import ClientException


class ObjectStorage:
    def __init__(self, config):
        self.config = config

        logging.basicConfig(level=logging.ERROR)
        logging.getLogger("swiftclient").setLevel(logging.CRITICAL)
        self.logger = logging.getLogger(__name__)

    def upload(self, container, source, object_name):
        obj = SwiftUploadObject(source, object_name)

        with SwiftService(options=self.config) as swift:
            try:
                for result in swift.upload(container=container, objects={obj}):
                    if not result["success"]:
                        raise result["error"]
            except SwiftError as e:
                self.logger.error(e.value)

    def list(self, container):
        with SwiftService(options=self.config) as swift:
            try:
                result = swift.list(container=container)
                for page in result:
                    if page["success"]:
                        return page["listing"]
                    else:
                        raise page["error"]
            except SwiftError as e:
                self.logger.error(e.value)
            except ClientException as e:
                self.logger.error(e.msg)
