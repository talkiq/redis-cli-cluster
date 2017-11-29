import rediscluster


class StrictRedisCluster(rediscluster.StrictRedisCluster):
    # pylint: disable=too-few-public-methods
    def __init__(self, host, port):
        super().__init__(host=host, port=port, decode_responses=True)
