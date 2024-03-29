import cv2
import numpy as np

class smoothing_processing():
    def Gmagnitude(image):
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      
        # Giam nhieu ban bo loc Gaussian
        img = cv2.GaussianBlur(img, (5, 5), 1.4)
      
        # tinh gradient anh theo 2 phuong x va y
        gx = cv2.Sobel(img, cv2.CV_32F, 0, 1, 3)
        gy = cv2.Sobel(img, cv2.CV_32F, 1, 0, 3)
     
        # Tinh magnitude va angle
        mag, ang = cv2.cartToPolar(gx, gy, angleInDegrees = True)
        return mag

    # Canny method detect edge
    def image_CannyDectectEdge1(image, t1 = 100, t2 = 200):
        # chuyen anh sang anh xam
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      
        # Giam nhieu ban bo loc Gaussian
        img = cv2.GaussianBlur(img, (5, 5), 1.4)
      
        # tinh gradient anh theo 2 phuong x va y
        gx = cv2.Sobel(np.float32(img), cv2.CV_64F, 1, 0, 3)
        gy = cv2.Sobel(np.float32(img), cv2.CV_64F, 0, 1, 3)
    
        # Tinh magnitude va angle
        mag, ang = cv2.cartToPolar(gx, gy, angleInDegrees = True)
      
        # Lay size cua anh
        height, width = img.shape
      
        # Duyet toan bo pixels anh
        # Duyet toan bo pixels anh
        for i_x in range(width):
            for i_y in range(height):
              
                grad_ang = ang[i_y, i_x]
                grad_ang = abs(grad_ang-180) if abs(grad_ang)>180 else abs(grad_ang)
              
                # selecting the neighbours of the target pixel
                # according to the gradient direction
                # In the x axis direction
                if grad_ang<= 22.5:
                    neighb_1_x, neighb_1_y = i_x-1, i_y
                    neighb_2_x, neighb_2_y = i_x + 1, i_y
             
                # top right (diagonal-1) direction
                elif grad_ang>22.5 and grad_ang<=(22.5 + 45):
                    neighb_1_x, neighb_1_y = i_x-1, i_y-1
                    neighb_2_x, neighb_2_y = i_x + 1, i_y + 1
             
                # In y-axis direction
                elif grad_ang>(22.5 + 45) and grad_ang<=(22.5 + 90):
                    neighb_1_x, neighb_1_y = i_x, i_y-1
                    neighb_2_x, neighb_2_y = i_x, i_y + 1
             
                # top left (diagonal-2) direction
                elif grad_ang>(22.5 + 90) and grad_ang<=(22.5 + 135):
                    neighb_1_x, neighb_1_y = i_x-1, i_y + 1
                    neighb_2_x, neighb_2_y = i_x + 1, i_y-1
             
                # Now it restarts the cycle
                elif grad_ang>(22.5 + 135) and grad_ang<=(22.5 + 180):
                    neighb_1_x, neighb_1_y = i_x-1, i_y
                    neighb_2_x, neighb_2_y = i_x + 1, i_y
              
                # Triet tieu phi toi da
                if width>neighb_1_x>= 0 and height>neighb_1_y>= 0:
                    if mag[i_y, i_x]<mag[neighb_1_y, neighb_1_x]:
                        mag[i_y, i_x]= 0
                        continue
  
                if width>neighb_2_x>= 0 and height>neighb_2_y>= 0:
                    if mag[i_y, i_x]<mag[neighb_2_y, neighb_2_x]:
                        mag[i_y, i_x]= 0
  
        # Double Thresholding
        for i_x in range(width):
            for i_y in range(height):
             
                grad_mag = mag[i_y, i_x]
             
                if grad_mag<t1:
                    mag[i_y, i_x]= 0
                elif t2>grad_mag>= t1:
                    mag[i_y, i_x]= 75
                else:
                    mag[i_y, i_x]= 255
        #return mag

        # Hysteresis Edge Tracking
        for i_x in range(1,width-1):
            for i_y in range(1,height-1):
                if mag[i_y][i_x] == 75:
                    if((mag[i_y+1][i_x] == 255) or (mag[i_y-1][i_x] == 225)
                    or (mag[i_y][i_x+1] == 255) or (mag[i_y][i_x-1] == 225)
                    or (mag[i_y+1][i_x+1] == 255) or (mag[i_y-1][i_x-1] == 225)
                    or (mag[i_y+1][i_x-1] == 255) or (mag[i_y-1][i_x+1] == 225)):
                        mag[i_y][i_x] = 255
                    else:
                        mag[i_y][i_x] = 0

        return mag      

    def image_CannyDectectEdge2(image, t1, t2):
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        img = cv2.Canny(img, threshold1=t1, threshold2=t2)
        return img

    
    

