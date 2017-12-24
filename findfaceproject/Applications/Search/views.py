from django.shortcuts import render
from .forms import *
import dlib
from skimage import io
from scipy.spatial import distance
from findfaceproject.Applications.Signup.forms import *
from django.contrib.auth import *
from findfaceproject.Applications.Login import views
# Create your views here.
def ResponseForSearch(request):

    obj = Subscriber.objects.all()
    images = Output.objects.all()

    prev_form = OutputForm()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form1 = SubscriberForm(request.POST)
        form = OutputForm(request.POST, request.FILES)
        #user = authenticate(username = form1.username, password = form1.password)
        # check whether it's valid:
        if form.is_valid() and request.session['user'] == True:

            form.save()

            sp = dlib.shape_predictor('/home/yaroslav/PycharmProjects/FindFace/shape_predictor_68_face_landmarks.dat')
            facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
            detector = dlib.get_frontal_face_detector()


            for i in images:
                img = io.imread('/home/yaroslav/PycharmProjects/FindFace/findfaceproject/' + i.img1.url)

            win1 = dlib.image_window()
            win1.clear_overlay()
            win1.set_image(img)

            dets = detector(img, 1)

            for k, d in enumerate(dets):
                print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                    k, d.left(), d.top(), d.right(), d.bottom()))
                shape = sp(img, d)
                win1.clear_overlay()
                win1.add_overlay(d)
                win1.add_overlay(shape)

            face_descriptor1 = facerec.compute_face_descriptor(img, shape)

            # print(face_descriptor1)
            for j in images:
                img = io.imread('/home/yaroslav/PycharmProjects/FindFace/findfaceproject/' + i.img2.url)

            win2 = dlib.image_window()
            win2.clear_overlay()
            win2.set_image(img)
            dets_webcam = detector(img, 1)

            for k, d in enumerate(dets_webcam):
                print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                    k, d.left(), d.top(), d.right(), d.bottom()))
                shape = sp(img, d)
                win2.clear_overlay()
                win2.add_overlay(d)
                win2.add_overlay(shape)

            face_descriptor2 = facerec.compute_face_descriptor(img, shape)

            a = distance.euclidean(face_descriptor1, face_descriptor2)
            print(a)

            if (a > 0.5):
                result = "Different persons"
            else:
                result = "Same persons"

                #return HttpResponseRedirect("http://127.0.0.1:8000/home/")
    else:
        form = Output()

    return render(request, 'search.html', locals())



