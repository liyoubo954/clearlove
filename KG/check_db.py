import pymysql

# 数据库连接信息
host = '172.16.105.12'
user = 'root'
password = '123456'
database = 'zstp'
port = 13366

# 连接数据库
try:
    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port,
        charset='utf8mb4'
    )
    cursor = conn.cursor()
    print("数据库连接成功！")
except Exception as e:
    print(f"数据库连接失败: {e}")
    exit()

# 检查各表中的数据量
tables = ['entity_types', 'entities', 'relationship_types', 'triple']

for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"表 {table} 中有 {count} 条记录")

# 查看每个表的前5条记录
print("\n查看各表的前5条记录:")

print("\nentity_types表:")
cursor.execute("SELECT * FROM entity_types LIMIT 5")
results = cursor.fetchall()
for row in results:
    print(row)

print("\nentities表:")
cursor.execute("SELECT * FROM entities LIMIT 5")
results = cursor.fetchall()
for row in results:
    print(row)

print("\nrelationship_types表:")
cursor.execute("SELECT * FROM relationship_types LIMIT 5")
results = cursor.fetchall()
for row in results:
    print(row)

print("\ntriple表:")
cursor.execute("SELECT * FROM triple LIMIT 5")
results = cursor.fetchall()
for row in results:
    print(row)

# 关闭连接
cursor.close()
conn.close()
print("\n数据库连接已关闭。")