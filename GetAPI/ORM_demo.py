import os
import numbers
import pymysql

# 连接数据库
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="******", db="model")
# 创建一个游标
cursor = conn.cursor()

class Field(object):
    pass

class IntegerField(Field):
    def __init__(self, col=None, minvalue=None, maxvalue=None):
        self._value = None
        self.col = col
        if not isinstance(maxvalue, numbers.Integral):
            raise ValueError("'maxvalue'需要一个整数")
        self.maxvalue = maxvalue or 100
        if not isinstance(minvalue, numbers.Integral):
            raise ValueError("'minvalue'需要一个整数")
        self.minvalue = minvalue or 0

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("'age'需要一个整数")
        if not self.minvalue < value <= self.maxvalue:
            raise ValueError("'age'的取值范围在[%s, %s]" % (self.minvalue, self.maxvalue))

        self._value = value

class CharField(Field):
    def __init__(self, col=None, maxlen=None):
        self._value = None
        self.col = col
        if not (isinstance(maxlen, numbers.Integral) and maxlen > 0):
            raise ValueError
        self.maxlen = maxlen or 10

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not (isinstance(value, str) and len(value) < self.maxlen):
            raise ValueError
        self._value = value


class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        # 如果是模板基类，不做处理
        if name == "ModelBase":
            return super().__new__(cls, name, bases, attrs)

        # 用文件名伪造模板名
        attrs.update(__module__=os.path.basename(__file__)[:-3])  # 构建模板名

        # 如果存在Meta属性，且设置了属性dbTable的值，则dbTable的值为数据库中表的名字
        meta = attrs.pop("Meta", {})
        dbTable = getattr(meta, "dbTable", None)
        # 否则，自动设置名字。格式："模板名_类名"。
        if dbTable is None:
            dbTable = attrs["__module__"] + "_" + name

        # 将与数据库相关内容存放进fields字段中
        fields = {}
        for k, v in attrs.items():
            # 利用父类Field对其子类统一管理
            if isinstance(v, Field):
                fields[k] = v

        attrs["dbTable"] = dbTable
        attrs["fields"] = fields
        return super().__new__(cls, name, bases, attrs)

class ModelBase(metaclass=ModelMeta):
    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def save(self):
        table = self.dbTable

        fields = []
        for k, v in self.fields.items():
            # 如果col为有效值，则列明为col对的键值，否则用属性名作为列名
            fields.append(getattr(v, "col") or k)

        # 构建sql语句
        values = [getattr(self, field) for field in fields]
        valuesStrList = ["'"+str(item)+"'" for item in values]
        sql = "INSERT INTO {table}({fields}) VALUES({values})".format(table=table,
                                                                      fields=",".join(fields),
                                                                      values=", ".join(valuesStrList))
        create_table(table)
        try:
            if cursor.execute(sql):
                conn.commit()
                print("保存成功")
        except Exception:
            conn.rollback()
            raise

class Student(ModelBase):
    name = CharField(col="", maxlen=10)
    age = IntegerField(col="", minvalue=12, maxvalue=19)

    class Meta:  # 表名
        dbTable = "school"


def create_table(name):
    """创建表"""
    try:
        cursor.execute("CREATE TABLE %s(name VARCHAR (10) NOT NULL , age INT DEFAULT 0)" % name)
        conn.commit()
        print("创建【%s】成功" % name)
    except pymysql.err.InternalError as e:
        if "exists" in e.args[1]:
            pass

def drop_table(name):
    """删除表"""
    try:
        cursor.execute("DROP TABLE %s" % name)
        conn.commit()
        print("删除【%s】成功" % name)
    except pymysql.err.InternalError as e:
        if "Unknown table" in e.args[1]:
            pass


# if __name__ == "__main__":
# 	"""测试代码"""
#     s = Student(name="zty", age=18)
#     s.save()

#     f = Student()
#     f.name = "guanf"
#     f.age = 18
#     f.save()

#     # drop_table("school")
#     conn.close()
