import sys
import io
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ProgrammingQuestion  # Import the ProgrammingQuestion model

# View to list all programming questions
def question_list(request):
    questions = ProgrammingQuestion.objects.all()  # Get all programming questions from the database
    return render(request, 'questions/question_list.html', {'questions': questions})  # Render the question list page

# View to add a new question (this is a placeholder function for now)
def add_question(request):
    # You can implement this later (e.g., form submission or API endpoint for adding questions)
    pass

# View to render Monaco Code Editor for writing code
def editor(request):
    return render(request, 'questions/editor.html')  # Render the Monaco editor template

# View to execute the submitted code
@csrf_exempt  # Temporarily exempting CSRF protection for testing; use secure methods in production
def execute_code(request):
    if request.method == 'POST':  # Only handle POST requests
        try:
            # Read the JSON payload from the request
            body = json.loads(request.body)
            code = body.get('code', '')  # Extract the 'code' key from the JSON body

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

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    else:
        # Return an error if the request method is GET or something else
        return JsonResponse({'error': 'Only POST requests are allowed for code execution.'}, status=405)
