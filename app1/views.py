import io
import os
from django.conf import settings
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from PIL import Image


# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'upload.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')



from django.shortcuts import render
from .forms import ImageUploadForm
from PIL import Image
from .forms import ImageUploadForm
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np

@login_required(login_url='login')
def upload_image(request):
    
    if 'image_url' in request.session:
        del request.session['image_url']
    if 'image_path' in request.session:
        del request.session['image_path']
    model_path = os.path.join(os.path.dirname(__file__), 'model_weights', 'chest_xray.h5')
    if request.method == 'POST':
        
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the image (e.g., resize or convert to grayscale)
            images = request.FILES['image']
            images_path = os.path.join(settings.MEDIA_ROOT, 'input_image.png')
            with open(images_path, 'wb+') as f:
                for chunk in images.chunks():
                    f.write(chunk)

            # save the image URL to the session for display in the template
            image_url = os.path.join(settings.MEDIA_URL, 'input_image.png')
            print(image_url)
            print(images_path)
            request.session['image_url'] = image_url
            request.session['image_path'] = images_path
            uploaded_image = form.cleaned_data['image']
            image_path = form.cleaned_data['image_path']
            print(image_path)
            # if hasattr(uploaded_image, 'temporary_file_path'):
            #     # File is on disk, you can use temporary_file_path
            #     img_path = uploaded_image.temporary_file_path()
            # else:
            #     # File is in memory, read it from memory
            #     img_data = uploaded_image.read()
            #     img_path = io.BytesIO(img_data)
            # img = Image.open(uploaded_image)
            # Perform pneumonia detection with your VGG16 model here
            model=load_model(model_path) 
            # path = uploaded_image.temporary_file_path()
            img_file=image.load_img(images_path,target_size=(224,224))
            x=image.img_to_array(img_file)
            x=np.expand_dims(x, axis=0)
            img_data=preprocess_input(x)
            classes=model.predict(img_data)
            result=classes
            if result[0][0]>0.5:
                res= "Result is Normal"
            else:
                res = "Affected By PNEUMONIA"
            # print(uploaded_image)
            # print(img_path)
            
            # print(uploaded_image.image.url)
            # Render the results page
            return render(request, 'results.html', {'uploaded_image': image_url, 'result': res})

    else:
        form = ImageUploadForm()

    return render(request, 'upload.html', {'form': form})
