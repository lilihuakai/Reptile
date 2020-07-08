# from mitmproxy import http
from mitmproxy import ctx

def request(flow):
    request = flow.request
    # info = ctx.log.info
    # url = "http://httpbin/get"
    # flow.request.url = url
    info(request.url)
    # info(str(request.headers))
    # info(str(request.cookies))
    # info(request.host)
    # info(request.method)
    # info(str(request.port))
    # info(request.scheme)

    # flow.request.headers['User-Agent'] = 'MitmProxy'
    # 白色
    # ctx.log.info(str(flow.request.headers))
    # 黄色
    # ctx.log.warn(str(flow.request.headers))
    # 红色
    # ctx.log.error(str(flow.request.headers))

    # print(flow.request.headers)

def response(flow):
    response = flow.response
    info = ctx.log.info
    info(str(response.status_code))
    info(str(response.headers))
    info(str(response.cookies))
    info(str(response.text))
