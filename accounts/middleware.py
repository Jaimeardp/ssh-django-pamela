class SimpleMiddleware(object):
    def __init__(self, get_response):
        print('SERVER ON!!')
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        print('PER PETICION')
        # Code to be executed for each request before
        # the view (and later middleware) are called.
	print(request.POST.items())
	secret = request.POST.get('password', None)
	response = self.get_response(request)
	if secret:
		print('flag sensible')
		#request.set_cookie('code', secret)
		response.set_cookie('code',secret)
	
        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
	if getattr(request,'POST', False):
		return None
	print('view function ' ,callback.__name__)
	if getattr(callback,'loginpam',False):
		print('View defined')
		return None
	print('Paramentos del formulario ', request.POST.items())
	return None

    def process_template_response(self, request, response):
        print('Middleware ')
	#print(request.POST.items())
        if response.status_code == 200:
            request.session['username'] = 'Jaime'
            request.session['color'] = 'red'
            print(' -------> ', request.session.keys())
            return response
        return response
