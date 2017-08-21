class ImagePlot:
    def __init__(self,figsize=0):      
        self.imgList = []
        size = figsize * 5
            
        plt.figure(figsize=(size,size))
        
    def ReshapeImage(self, img):        
        if len(img.shape) == 4:
            w = img.shape[1]
            h = img.shape[2]
        elif len(img.shape) == 3:
            w = img.shape[1]
            h = img.shape[2]
        elif len(img.shape) == 2:
            w = img.shape[0]
            h = img.shape[1]
        img = img.reshape([w,h])    
        return img
    
    def AddPlot(self,img):
        img = self.ReshapeImage(img)        
        self.imgList.append([img,None,0.0])
    
    def AddPlot2(self,img,overlay,alpha=0.3):
        img = self.ReshapeImage(img)
        overlay = self.ReshapeImage(overlay)        
        self.imgList.append([img,overlay,alpha])
    
    def Show(self):
        for i,imgInfo in enumerate(self.imgList):
            img = imgInfo[0]
            overlay = imgInfo[1]
            alpha = imgInfo[2]
            plt.subplot(1,len(self.imgList),i+1)
            
            plt.imshow(img, cmap='gray')            
            if overlay is not None:
                overlay = np.ma.masked_where(overlay <= 0, overlay)
                plt.imshow(overlay,alpha=alpha)
            plt.xticks([])
            plt.yticks([])
        plt.tight_layout()
        plt.show()            

        
imgplt = ImagePlot(3)
imgplt.AddPlot2(teX, teYpixel)

for j in range(1,6,1):        
    imgplt.AddPlot2(teX, prob[0,:,:,j] > 0.3)
imgplt.Show()
