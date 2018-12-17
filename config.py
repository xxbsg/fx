# 配置
import logging
from redis import StrictRedis


class peiz(object):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI="mysql://root:mysql@localhost:3306/f_db" #数据数据库
    SQLALCHEMY_TRACK_MODIFICATIONS=False#数据数据库
        #session
    SESSION_TYPE='redis'#session使用redis数据库
    SESSION_REDIS=StrictRedis(host='192.168.47.128',port=6379,db=1)#session链接数据库
    SESSION_USE_SIGNER=True#session加密
    SECRET_KEY='dyh123'
    PERMANENT_SESSION_LIFETIME=360
    LOG_LEVEL=logging.DEBUG
    REDIS_HOST='192.168.47.128'
    REDIS_PORT=6379
class tiaoshi(peiz):
    DEBUG = True
class xianshang(peiz):
    DEBUG = False



zd={'ts':tiaoshi,'xs':xianshang}