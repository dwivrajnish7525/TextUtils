from django.http import HttpResponse
from django.shortcuts import render;

def index(request):
    return render(request,'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    newline_remover = request.POST.get('newline_remover', 'off')
    capitalize = request.POST.get('capitalize_option', 'off')
    space = request.POST.get('space_remover', 'off')
    extra = request.POST.get('exter_space_remover', 'off')
    counter = request.POST.get('Element_counter', 'off')
    analyzed = djtext   # start with original text
    purpose = []        # collect all operations done

    # 1. Remove Punctuation
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = "".join([char for char in analyzed if char not in punctuations])
        purpose.append("Removed Punctuations")

    # 2. Capitalize
    if capitalize == "on":
        analyzed = analyzed.upper()
        purpose.append("Capitalized Text")

    # 3. New Line Remover
    if newline_remover == "on":
        analyzed = "".join([char for char in analyzed if char != "\n" and char != "\r"])
        purpose.append("Removed New Lines")

    # 4. Space Remover
    if space == "on":
        analyzed = "".join([char for char in analyzed if char != " "])
        purpose.append("Removed All Spaces")

    # 5. Extra Space Remover
    if extra == "on":
        analyzed = " ".join(analyzed.split())  # ✅ simpler way
        purpose.append("Removed Extra Spaces")

    # 6. Counter
    if counter == "on":
        analyzed = f"Total characters: {len(analyzed)}"
        purpose.append("Character Count")

    # Final response
    if purpose:   # if at least one option was selected
        params = {
            "Analyzed_text": analyzed,
            "Title": " | ".join(purpose)
        }
        return render(request, 'Next.html', params)
    else:
        return HttpResponse("Error: Please select at least one checkbox <br><a href='/'>Back</a>")
