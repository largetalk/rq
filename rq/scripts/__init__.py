import redis
from rq import use_connection


def add_standard_arguments(parser):
    parser.add_argument('--host', '-H', default='localhost',
            help='The Redis hostname (default: localhost)')
    parser.add_argument('--port', '-p', type=int, default=6379,
            help='The Redis portnumber (default: 6379)')
    parser.add_argument('--db', '-d', type=int, default=0,
            help='The Redis database (default: 0)')
    parser.add_argument('--passwd', '-pwd', default=None,
            help='The Redis password (default: None)')

def setup_redis(args):
    redis_conn = redis.Redis(host=args.host, port=args.port, db=args.db, password=args.passwd)
    use_connection(redis_conn)
