from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact(request):
    if request.method == 'POST':
        # Capture the form data
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number', '')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to the database
        # Contact.objects.create(
        #     full_name=full_name,
        #     email=email,
        #     mobile_number=mobile_number,
        #     subject=subject,
        #     message=message,
        # )
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('home')     

    return render(request, 'home.html')





# def contact(request):
#     if request.method == 'POST':
#         # Capture the form data
#         full_name = request.POST.get('full_name')
#         email = request.POST.get('email')
#         mobile_number = request.POST.get('mobile_number', '')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         # Compose the email content
#         email_subject = f"Contact Form Submission: {subject}"
#         email_body = f"""
#         Name: {full_name}
#         Email: {email}
#         Mobile Number: {mobile_number}

#         Message:
#         {message}
#         """

#         # Send the email
#         try:
#             send_mail(
#                 email_subject,
#                 email_body,
#                 settings.DEFAULT_FROM_EMAIL,  # Sender's email (defined in settings.py)
#                 [settings.CONTACT_EMAIL],     # Recipient's email (defined in settings.py)
#                 fail_silently=False,
#             )
#             messages.success(request, 'Your message has been sent successfully!')
#         except Exception as e:
#             messages.error(request, f"Failed to send your message. Error: {str(e)}")
        
#         return redirect('home')     

#     return render(request, 'home.html')