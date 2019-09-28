# import cv2
# #加载图片
# image = cv2.imread("C:/Users/19845/Desktop/1.jpg")
# #创建窗口
# cv2.namedWindow("window")
# #定义函数实现鼠标点击事件
# def draw(event,x,y,flags,param):
#     #判断鼠标事件类型
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print("鼠标--------->按下")
#     elif event == cv2.EVENT_MOUSEMOVE:
#         print("鼠标--------->滑动")
#     elif event == cv2.EVENT_LBUTTONUP:
#         print("鼠标--------->抬起")
# #监听鼠标事件
# cv2.setMouseCallback("window",draw)
# #展示窗口
# cv2.imshow("window",image)
# #解决窗口闪退,无限等待
# cv2.waitKey(0)
# #优化，销毁窗口
# cv2.destroyAllWindows()


# #图片模糊
# import cv2
# #加载图片
# image = cv2.imread("C:/Users/19845/Desktop/1.jpg")
# #图片模糊 模糊对象，模糊程度,值越大越模糊
# image_dst = cv2.blur(image,(15,15))
# #创建窗口
# cv2.namedWindow("window")
# cv2.imshow("window",image_dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



#图片美颜
import cv2
#加载图片
image = cv2.imread("C:/Users/19845/Desktop/1.jpg")
#图片美颜 对象，美颜程度,值越大效果越大
value = 28
image_dst = cv2.bilateralFilter(image,value,value*2,value/2)
#美颜后图片
cv2.imwrite("C:/Users/19845/Desktop/11.jpg",image_dst)


#创建窗口
cv2.namedWindow("window")
cv2.imshow("window",image_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
