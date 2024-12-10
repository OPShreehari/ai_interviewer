import sys
import io
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def execute_code(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')  # Get code from POST request

        # Redirect stdout to capture the output
        old_stdout = sys.stdout
        result = io.StringIO()
        sys.stdout = result

        try:
            # Execute the Python code (dangerous in production, secure it with sandboxing)
            exec(code)
            output = result.getvalue()  # Capture the output
        except Exception as e:
            output = f"Error: {e}"  # Capture any errors

        sys.stdout = old_stdout  # Reset stdout
        return JsonResponse({'output': output})  # Return the output to the frontend
