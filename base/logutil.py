import logging
from functools import wraps

logger = logging.getLogger('request_response')

def loggable(view_func):
    @wraps(view_func)
    def _wrapped_view_func(request, *args, **kwargs):
        method=request.method
        path=request.path
        username=request.user.username
        params = request.GET
        if method=='POST':
            params = request.POST
        logger.info("",extra={'username':username,'path':path,'method':method,'params':params})
        response = view_func(request, *args, **kwargs)
        return response

    return _wrapped_view_func