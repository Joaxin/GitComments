
# coding: utf-8

# ## Ajax

# ### Weibo

# ### Find ID

# In[ ]:


- https://weibo.com/sjorchid

- https://weibo.com/p/aj/recommendlist?ajwvr=6&mid=sjorchid&location=page_230673_home&oid=1410812623&__rnd=1521034792889

- https://m.weibo.cn/u/1410812623


# ### Create Database

# In[65]:


import psycopg2

conn = psycopg2.connect(database="demo", user="lysql", password="123456", host="127.0.0.1", port="5432")
try:  
    cursor = conn.cursor()
    transaction = cursor.execute("""CREATE TABLE orchid(
    ID  SERIAL PRIMARY KEY NOT NULL,
    UID  BIGINT NOT NULL,
    TEXT    TEXT NOT NULL,
    ATTITUDES    TEXT NOT NULL,
    COMMENTS   TEXT NOT NULL,
    REPOSTS    INT NOT NULL,
    SCHEME    TEXT NOT NULL);
       """)
    print('Successful')
    conn.commit()
except (Exception, psycopg2.DatabaseError) as error:
        print(error)
finally:
        print(conn)
        if conn is not None:
            conn.close()


# ### TEST

# In[ ]:


import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq

base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/1410812623',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

max_page = 100

def get_page(page):
    params = {
        'type': 'uid',
        'value': '1410812623',
        'containerid': '1076031410812623',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

# get_page(1)


# ### Paese Page

# In[ ]:


def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            weibo = {}
            weibo['scheme'] = item.get('scheme')
            item = item.get('mblog')
            weibo['uid'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo
def save_orchid(data):
    conn = psycopg2.connect(database="demo", user="lysql", password="123456", host="127.0.0.1", port="5432")
    table = "orchid"
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
    try:  
        cursor = conn.cursor()
        cursor.execute(sql, tuple(data.values()));
        conn.commit()
        print ("Records created successfully");
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
            if conn is not None:
                conn.close()


# ###  Scrap

# In[63]:


for page in range(2, max_page+1):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)
            save_orchid(result)


# In[ ]:




