"""
    中间件，是一个轻量级的插件系统，可以介入django的请求和响应处理，修改django的输入和输出
    使用场景：某些操作在请求或者相应的时候都需要执行的操作，放在中间件中，再把中间件添加在请求上
        比如：每次POST请求的时候都进行CSRF验证，就把CSRF验证写在中间件中，不需要每次请求都独立写CSRF验证
"""

"""
    自定义的中间件，至少实现1-6个父类方法，从init创建中间件到请求再到响应一整套流程

    自定义的中间件还需要在settins中注册，多个中间件如果都执行相同的重写方法，那么先注册的后执行，也就是说后注册的先响应

"""