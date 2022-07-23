def yolov4_predict(image, cfg, weights):

    import cv2
    import numpy as np

    img = cv2.imread(image)
    print(img.shape)

    img_width = img.shape[1]
    img_height = img.shape[0]

    img_blob = cv2.dnn.blobFromImage(img, 1/255, (416,416), (0,0,0), True, crop=False) #    yolo ile nesne tespiti yapabilmek için resmi yoloya vermemiz gerekir

    labels = ["arac","insan","UAP","UAI"]
    print("toplam label sayımız", len(labels))

    colors = ["0,255,255","0,0,255","255,0,0","255,255,0","0,255,0"]
    colors = [np.array(color.split(",")).astype("int") for color in colors] 

    colors = np.array(colors)
    colors = np.tile(colors,(18,1)) 
    print(colors)

    model = cv2.dnn.readNetFromDarknet(cfg, weights)

    layers = model.getLayerNames() 
    output_layer = [layers[layer-1] for layer in model.getUnconnectedOutLayers()]

    model.setInput(img_blob)  
    detection_layers =  model.forward(output_layer)

    predicted_id_non_max = []
    predicted_box_non_max = []
    predicted_conf_non_max = []

    for detection_layer in detection_layers:
        for object_detection in detection_layer:    
            scores = object_detection[5:]   
            predicted_id = np.argmax(scores)                              

            confidence = scores[predicted_id]   
            if confidence > 0.35:   
                label = labels[predicted_id]   
                bounding_box = object_detection[0:4]*np.array([img_width,img_height,img_width,img_height]) 
                                                                                                            
                (box_center_x,box_center_y,box_width,box_height) = bounding_box.astype("int")   
                                                                                                
                start_x = int(box_center_x - (box_width/2))     
                start_y = int(box_center_y - (box_height/2))    
                
                predicted_id_non_max.append(predicted_id)   
                predicted_conf_non_max.append(float(confidence))    
                predicted_box_non_max.append([start_x,start_y,int(box_width),int(box_height)])  

    max_ids = cv2.dnn.NMSBoxes(predicted_box_non_max,predicted_conf_non_max,0.5,0.4)   

    for max_id in max_ids:
        
        max_id = [max_id]
        max_class_id = max_id[0]   
        box = predicted_box_non_max[max_class_id]

        start_x = box[0]
        start_y = box[1]
        box_width = box[2]
        box_height = box[3]

        predicted_id = predicted_id_non_max[max_class_id]
        label = labels[predicted_id]
        confidence = predicted_conf_non_max[max_class_id]

        end_x = start_x + box_width
        end_y = start_y + box_height
        
        box_color = colors[predicted_id]    
        box_color = [int(each) for each in box_color]   

        label = "{}: {:.2f}%".format(label,confidence*100) 
        #label = "{}".format(label)
        print("predicted object {}".format(label)) 

        cv2.rectangle(img,(start_x,start_y),(end_x,end_y),box_color,3)

    print(label)   
        
    return img, start_x, start_y, end_x, end_y, label


