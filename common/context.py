#name
import  re
from API_0419.common.config import config
import configparser
class Context:
    loan_id = None

def replace(data):
    p = "#(.*?)#"
    while re.search(p, data):
        # print(data)
        m = re.search(p, data)
        g = m.group(1)
        try:
            v = config.get('data', g)
        except configparser.NoOptionError as e:
            if hasattr(Context,g):
                # print('参数化的值')
                v = getattr(Context,g)
                # print(type(v),v)
            else:
                print('找不到参数化的值')
                raise e

        data = re.sub(p, v, data, count=1)
        # print('标ID',type(Context.loan_id),Context.loan_id)
    return data
# replace("{'id':'#loan_id#','status':'4'}")
# replace("{'mobilephone':'#admin_user#','pwd':'#admin_pwd#'}")
