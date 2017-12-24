#!/usr/bin/env python3
def main():
    import dlib
    import os
    from skimage import io
    from scipy.spatial import distance
    from findfaceproject.Applications.Search.models import Output
    from findfaceproject.Applications.Search.forms import forms
    from findfaceproject.Applications.Search.forms import OutputForm
    from findfaceproject.Applications.Search import views
    sp = dlib.shape_predictor('/home/igor/PycharmProjects/PhotoComparsion/shape_predictor_68_face_landmarks.dat')
    facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
    detector = dlib.get_frontal_face_detector()

    images = Output.objects.all()

    #for i in images:
        #if i.img1 == :
    img = io.imread('/home/igor/python_environments/findfaceproject/findfaceproject/media/img/deimon.jpg')#TOD

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

    #print(face_descriptor1)

    img = io.imread('/home/igor/python_environments/findfaceproject/findfaceproject/media/img/Spectorsky1.jpg')
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


    global a
    a = distance.euclidean(face_descriptor1, face_descriptor2)
    print(a)

    if (a > 0.6):
        print("Different persons")
    else:
        print("Same persons")

    #wait = input("Input Enter to continue")
    def GetResult():
        return a

if __name__ == '__main__':
    main()