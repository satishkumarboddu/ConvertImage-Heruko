
import streamlit as st 
from PIL import Image
import cv2    
import numpy as np


kernal = np.ones((5,5),np.uint8)

st.title("Upload + Convertion")

uploaded_file = st.file_uploader("Upload an image...", type="jpg")


if uploaded_file is not None:
    # image = uploaded_file
    our_image = Image.open(uploaded_file)
    st.text('Original Image')
    st.image(our_image)


convert = st.selectbox('Convert to',('Original', 'Gray-Scale', 'GaussianBlur','Canny','Dilate','Erode'))


if convert == 'Original':
    our_image = Image.open(uploaded_file)
    st.text('Original Image')
    st.image(our_image)


if convert == 'Gray-Scale':
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    st.text(convert + ' image')
    st.image(gray)


elif convert == 'GaussianBlur':
    new_img = np.array(our_image.convert('RGB'))
    imgBlur = cv2.GaussianBlur(new_img,(5,5),2)
    st.text(convert + ' image')
    st.image(imgBlur)
    
elif convert == 'Canny':
    new_img = np.array(our_image.convert('RGB'))
    imgCanny = cv2.Canny(new_img,120,110)
    st.text(convert + ' image')
    st.image(imgCanny)
    
elif convert == 'Dilate':
    new_img = np.array(our_image.convert('RGB'))
    imgDilate = cv2.dilate(new_img,kernal,iterations = 1)
    st.text(convert + ' image')
    st.image(imgDilate)
    
elif convert == 'Erode':
    new_img = np.array(our_image.convert('RGB'))
    imgEroded = cv2.erode(new_img,kernal,iterations=1)
    st.text(convert + ' image')
    st.image(imgEroded)




   
