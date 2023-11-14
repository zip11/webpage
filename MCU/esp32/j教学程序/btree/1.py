
import btree

# First, we need to open a stream which holds a database
#首先，我们需要打开一个包含数据库的流
# This is usually a file, but can be in-memory database
#这通常是一个文件，但可以在内存数据库中
# using uio.BytesIO, a raw flash partition, etc.
#使用uio。BytesIO、原始闪存分区等。
# Oftentimes, you want to create a database file if it doesn't
#通常，如果数据库文件没有
# exist and open if it exists. Idiom below takes care of this.
#存在并打开（如果存在）。下面的白痴会处理这个问题。
# DO NOT open database with "a+b" access mode.
#不要使用“a+b”访问模式打开数据库。

try:
    f = open("mydb", "r+b")
except OSError:
    f = open("mydb", "w+b")

# Now open a database itself
db = btree.open(f)

# The keys you add will be sorted internally in the database
#您添加的密钥将在数据库中进行内部排序
db[b"3"] = b"three"
db[b"1"] = b"one"
db[b"2"] = b"two"

# Assume that any changes are cached in memory unless
#假设任何更改都缓存在内存中，除非
# explicitly flushed (or database closed). Flush database
#显式刷新（或关闭数据库）。刷新数据库
# at the end of each "transaction".
#在每次“交易”结束时。
db.flush()

# Prints b'two'
print(db[b"2"])

# Iterate over sorted keys in the database, starting from b"2"
#从b“2”开始对数据库中已排序的键进行迭代
# until the end of the database, returning only values.
#直到数据库结束，只返回值。
# Mind that arguments passed to values() method are *key* values.
#请注意，传递给values（）方法的参数是*key*值。
# Prints:
#打印：
#   b'two'
#   b'three'
for word in db.values(b"2"):
    print(word)

del db[b"2"]

# No longer true, prints False
print(b"2" in db)

# Prints:
#  b"1"
#  b"3"
for key in db:
    print(key)

db.close()

# Don't forget to close the underlying stream!
#别忘了关闭下面的流！
f.close()
