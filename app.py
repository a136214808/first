from flask import Flask,request
#request全局对象
app = Flask(__name__)

'''
url = http[80]/https[443]://www.xx.com
#url与视图 -> path与视图
'''


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/profile')
def profile():
    return '我是个人中心'

@app.route('/blog/list')
def blog_list():
    return '我是个人列表'

#定义有参函数(URL)
'''
定义类型：<int：blog_id>
str/int/float/unid/any
'''
#将参数固定到path中
@app.route('/blog/<blog_id>')
def blog_detail(blog_id):
    return '你访问的博客是：{}'.format(blog_id)


#查询字符串方式传参
#文章列表 /book/list:返回第一页的数据
#/book/list/?page=2返回第二页的数据
@app.route('/book/list')
def book_list():
    #request.args:类似字典
    page = request.args.get('page',1,type=int)
    return '你获取的是第{}页列表'.format(page)





if __name__ == '__main__':
    app.run()
